class WordsFinder:
    def __init__(self, *args):
        self.file_names = args

    def get_all_words(self):
        all_words = {}
        for file_name in self.file_names:
            with open(file_name, 'r', encoding='utf-8') as file:
                text = file.read().lower()
                for char in [',', '.', '=', '!', '?', ';', ':', ' - ']:
                    text = text.replace(char, ' ')
                words = text.split() а
                all_words[file_name] = words
        return all_words

    def find(self, word):
        word = word.lower()
        result = {}
        for name, words in self.get_all_words().items():
            if word in words:
                result[name] = words.index(word)+1
        return result

    def count(self, word):
        word = word.lower()
        result = {}
    for name, words in self.get_all_words().items():
            result[name] = words.count(word)
        return result
