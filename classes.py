
class Word(object):
    def __init__(self, kana, kanji, english, category, status):
        self.kana = kana
        self.kanji = kanji
        self.english = english
        self.category = category
        self.status = status


class Kanji(object):
    def __init__(self, sequence, kanji, meaning, status):
        self.sequence = sequence
        self.kanji = kanji
        self.meaning = meaning
        self.status = status
