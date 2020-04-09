
'''
This script will update Vocabulary.xlsx.

For every word, it will write the highest frequency sequence of its kanji.
It will output 0 if it only contains kana.
'''

import openpyxl
from utils import kanji_only, load_kanji_list

def determine_freq_sequence(word, sequence_dict):
    word = kanji_only(word)
    
    if word == '':
        return 0
    
    sequences = []
    for c in word:
        sequences.append(sequence_dict[c])
    
    return max(sequences)


if __name__ == '__main__':

    ###########################################################################
    # Read Kanji.xlsx

    kanji_list = load_kanji_list('..\Kanji.xlsx')
    freq_sequence_dict = {}
    kklc_sequence_dict = {}
    for k in kanji_list:
        freq_sequence_dict[k.kanji] = k.freq_sequence
        kklc_sequence_dict[k.kanji] = k.kklc_sequence

    ###########################################################################
    # Update Vocabulary.xlsx

    workbook = openpyxl.load_workbook(filename='..\Vocabulary.xlsx')
    sheet = workbook.worksheets[0]

    for row in range(2, sheet.max_row+1):
        kanji = sheet['A' + str(row)].value
        sheet['F' + str(row)] = determine_freq_sequence(kanji, kklc_sequence_dict)
        sheet['G' + str(row)] = determine_freq_sequence(kanji, freq_sequence_dict)

    workbook.save(filename='..\Vocabulary.xlsx')
