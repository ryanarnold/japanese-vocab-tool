
class Word(object):
    def __init__(self, kana='', kanji='', english='', category='', status=''):
        self.kana = kana
        self.kanji = kanji
        self.english = english
        self.category = category
        self.status = status


class Kanji(object):
    def __init__(self, kklc_sequence='', freq_sequence='', kanji='', meaning='', status=''):
        self.kklc_sequence = kklc_sequence
        self.freq_sequence = freq_sequence
        self.kanji = kanji
        self.meaning = meaning
        self.status = status
