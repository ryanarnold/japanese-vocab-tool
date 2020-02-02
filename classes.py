from utils import strip_kana, strip_special_chars
import re

class Word(object):
    def __init__(self, kana, kanji, english, category, status):
        self.kana = kana
        self.kanji = kanji
        self.english = english
        self.category = category
        self.status = status


    def is_containing_kanjis_in_list(self, kanji_list):
        pure_kanji = self.pure_kanji()

        for k in pure_kanji:
            if k not in kanji_list:
                return False

        return True


    def pure_kanji(self):
        return strip_special_chars(strip_kana(self.kanji))


class Kanji(object):
    def __init__(self, sequence, kanji, meaning, status):
        self.sequence = sequence
        self.kanji = kanji
        self.meaning = meaning
        self.status = status
