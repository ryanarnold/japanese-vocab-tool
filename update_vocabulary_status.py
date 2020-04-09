
'''
This script will update Vocabulary.xlsx. It will set the following status,
depending on the corresponding condition:

ready to learn : if all kana OR if all kanji in the word is already learned
to learn kanji : if the word contains an unknown kanji

'''

import xlrd
from utils import strip_kana, strip_special_chars

class Kanji:

    def __init__(self, kanji, status):
        self.kanji = kanji
        self.status = status


def has_unknown_kanji(word, unknown_kanji_list):
    word = strip_special_chars(strip_kana(word))
    
    if word == '':
        return False
    
    for c in word:
        if c in unknown_kanji_list:
            return True
    
    return False


if __name__ == '__main__':
    kanji_list = []
    workbook = xlrd.open_workbook('..\Kanji.xlsx')
    sheet = workbook.sheet_by_index(0)

    for row in range(1, sheet.nrows):
        kanji = sheet.cell_value(row, 1)
        status = sheet.cell_value(row, 4)
        kanji_list.append(Kanji(kanji, status))
    
    workbook.release_resources()

    unknown_kanji_list = [k.kanji for k in kanji_list if k.status == 'unknown']

    
    workbook = xlrd.open_workbook('..\Vocabulary.xlsx')
    sheet = workbook.sheet_by_index(0)

    with open('words_with_unknown_kanji.txt', 'w', encoding='utf-8') as output:
        unknown_count = 0
        for row in range(1, sheet.nrows):
            word = sheet.cell_value(row, 0)
            
            if has_unknown_kanji(word, unknown_kanji_list):
                output.write(word + '\n')
                unknown_count += 1
    
    workbook.release_resources()

    print(f'{unknown_count} words has unknown kanji')
