import re
import xlrd
from classes import Kanji

HIRAGANA = '[あいうえおかきくけこさしすせそたちつてとなにぬねのはひふへほまみむめもやゆよらりるれろわをゃゅょぁぃぅぇぉっがぎぐげござじずぜぞだぢづでどばびぶべぼぱぴぷぺぽん]'
KATAKANA = '[アァカサタナハマヤャラワガザダバパイィキシチニヒミリヰギジヂビピウゥクスツヌフムユュルグズヅブプエェケセテネヘメレヱゲゼデベペオォコソトノホモヨョロヲゴゾドボポヴッン]'
SPECIAL_CHARS = '[・ーヽヾ、。～々]'

def strip_kana(japanese_string):
    japanese_string = re.sub(HIRAGANA, '', japanese_string)
    japanese_string = re.sub(KATAKANA, '', japanese_string)
    return japanese_string


def strip_special_chars(japanese_string):
    return re.sub(SPECIAL_CHARS, '', japanese_string)


def load_kanji_list(filepath):
    kanji_list = []
    workbook = xlrd.open_workbook(filepath)
    sheet = workbook.sheet_by_index(0)

    for row in range(1, sheet.nrows):
        kklc_sequence = sheet.cell_value(row, 0)
        kanji = sheet.cell_value(row, 1)
        meaning = sheet.cell_value(row, 2)
        freq_sequence = sheet.cell_value(row, 3)
        status = sheet.cell_value(row, 4)
        kanji_list.append(Kanji(
            kklc_sequence=kklc_sequence,
            freq_sequence=freq_sequence,
            kanji=kanji,
            meaning=meaning,
            status=status
        ))
    
    workbook.release_resources()

    return kanji_list

if __name__ == '__main__':
    print(strip_special_chars(strip_kana('中国ありがとう日本カタカナ～教える')))
