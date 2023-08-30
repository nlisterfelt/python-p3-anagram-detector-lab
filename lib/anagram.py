class Anagram():
    def __init__(self, word):
        self.word = word
    def match(self, words_list):
        new_list = []
        for new_word in words_list:
            if set(new_word) == set(self.word):
                new_list.append(new_word)
        return new_list