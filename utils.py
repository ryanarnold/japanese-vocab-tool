import re

HIRAGANA = '[あいうえおかきくけこさしすせそたちつてとなにぬねのはひふへほまみむめもやゆよらりるれろわをゃゅょぁぃぅぇぉっがぎぐげござじずぜぞだぢづでどばびぶべぼぱぴぷぺぽん]'
KATAKANA = '[アァカサタナハマヤャラワガザダバパイィキシチニヒミリヰギジヂビピウゥクスツヌフムユュルグズヅブプエェケセテネヘメレヱゲゼデベペオォコソトノホモヨョロヲゴゾドボポヴッン]'
SPECIAL_CHARS = '[・ーヽヾ、。～々]'

def strip_kana(japanese_string):
    japanese_string = re.sub(HIRAGANA, '', japanese_string)
    japanese_string = re.sub(KATAKANA, '', japanese_string)
    return japanese_string


def strip_special_chars(japanese_string):
    return re.sub(SPECIAL_CHARS, '', japanese_string)

if __name__ == '__main__':
    print(strip_special_chars(strip_kana('中国ありがとう日本カタカナ～教える')))
