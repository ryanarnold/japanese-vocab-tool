
'''
This script will update Vocabulary.xlsx. It will set the following status,
depending on the corresponding condition:

ready to learn : if all kana OR if all kanji in the word is already learned
to learn kanji : if the word contains an unknown kanji

'''

import xlrd
import openpyxl
from utils import strip_kana, strip_special_chars
from classes import Kanji, Word


def has_unknown_kanji(word, unknown_kanji_list):
    word = strip_special_chars(strip_kana(word))
    
    if word == '':
        return False
    
    for c in word:
        if c in unknown_kanji_list:
            return True
    
    return False


if __name__ == '__main__':

    ###########################################################################
    # Determine unknown kanjis

    kanji_list = []
    workbook = xlrd.open_workbook('..\Kanji.xlsx')
    sheet = workbook.sheet_by_index(0)

    for row in range(1, sheet.nrows):
        kanji = sheet.cell_value(row, 1)
        status = sheet.cell_value(row, 4)
        kanji_list.append(Kanji(kanji=kanji, status=status))
    
    workbook.release_resources()

    unknown_kanji_list = [k.kanji for k in kanji_list if k.status == 'unknown']

    ###########################################################################
    # Read Vocabulary.xlsx to determine which words has unknown kanji
    
    word_list = []
    workbook = xlrd.open_workbook('..\Vocabulary.xlsx')
    sheet = workbook.sheet_by_index(0)

    with open('words_with_unknown_kanji.txt', 'w', encoding='utf-8') as output:
        for row in range(1, sheet.nrows):
            word_kanji = sheet.cell_value(row, 0)

            word = Word(kanji=word_kanji)
            
            if has_unknown_kanji(word.kanji, unknown_kanji_list):
                word.status = 'to learn kanji'
            else:
                word.status = 'ready to learn'
            
            word_list.append(word)
    
    workbook.release_resources()

    words_with_unknown_kanji = [w.kanji for w in word_list if w.status == 'to learn kanji']
    print(f"{len(words_with_unknown_kanji)} words has unknown kanji")

    ###########################################################################
    # Update Vocabulary.xlsx

    workbook = openpyxl.load_workbook(filename='..\Vocabulary.xlsx')
    sheet = workbook.worksheets[0]

    for row in range(2, sheet.max_row+1):
        kanji = sheet['A' + str(row)].value
        
        if kanji in words_with_unknown_kanji:
            sheet['E' + str(row)] = 'need to learn kanji'
        else:
            sheet['E' + str(row)] = 'ready to learn'

    workbook.save(filename='..\Vocabulary.xlsx')
