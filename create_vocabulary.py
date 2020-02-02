from classes import Kanji, Word
import csv


'''
    JAPANESE VOCABULARY TOOL

    To use:
    1. Create a Kanji.csv file with the following fields
        - sequence
        - kanji
        - meaning
        - status
    2. Create a Vocabulary.csv file with the following fields
        - kana
        - kanji
        - english
        - category
        - status
    3. Execute create_vocabulary.py
    4. Open New_Vocabulary.csv for the vocabulary with updated statuses
    5. Open Kanji_Needing_Words.csv for the kanji that you need to learn a word
'''


kanji_list = []
vocabulary_list = []

###############################################################################
#   EXTRACTING
###############################################################################

with open('Kanji.csv', encoding='utf-8-sig') as kanji_file:
    csv_reader = csv.DictReader(kanji_file, delimiter=',')
    for row in csv_reader:
        kanji_list.append(
            Kanji(
                row['sequence'],
                row['kanji'],
                row['meaning'],
                row['status']
            )
        )

kanji_known = [kanji.kanji for kanji in kanji_list if  kanji.status != 'unknown']

print(f'You know {len(kanji_known)} kanji.')

with open('Vocabulary.csv', encoding='utf-8-sig') as vocabulary_file:
    csv_reader = csv.DictReader(vocabulary_file, delimiter=',')
    for row in csv_reader:
        vocabulary_list.append(
            Word(
                row['kana'],
                row['kanji'],
                row['english'],
                row['category'],
                ''
            )
        )

print(f'Extracted {len(kanji_list)} kanji characters.')
print(f'Extracted {len(vocabulary_list)} words.')

###############################################################################
#   DETERMINE WHICH WORDS TO ADD TO SRS SYSTEM
###############################################################################

for word in vocabulary_list:
    if word.kanji == '':
        word.status = 'to add to SRS'
    elif word.is_containing_kanjis_in_list(kanji_known):
        word.status = 'to add to SRS'

words_to_learn = [w for w in vocabulary_list if w.status == 'to add to SRS']

print(f'Need to add {len(words_to_learn)} words to SRS.')

###############################################################################
#   DETERMINE WHICH KANJI NEEDS A WORD
###############################################################################

all_kanji_to_add_to_srs = ''.join([word.pure_kanji() for word in words_to_learn])
kanji_needs_word = [kanji for kanji in kanji_known if kanji not in all_kanji_to_add_to_srs]

print(f'Need to add words for {len(kanji_needs_word)} kanji characters.')

###############################################################################
#   WRITE TO CSV FILE
###############################################################################'

with open('New_Vocabulary.csv', 'w', newline='', encoding='utf-8-sig') as csvfile:
    fieldnames = ['kana', 'kanji', 'english', 'category', 'status']
    
    writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
    writer.writeheader()

    for word in vocabulary_list:
        writer.writerow({
            'kana': word.kana,
            'kanji': word.kanji,
            'english': word.english,
            'category': word.category,
            'status': word.status,
        })

with open('Kanji_Needing_Words.csv', 'w', newline='', encoding='utf-8-sig') as csvfile:
    fieldnames = ['kanji']
    
    writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
    writer.writeheader()

    for kanji in kanji_needs_word:
        writer.writerow({'kanji': kanji})
