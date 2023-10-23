class WordCounter:
    def __init__(self, path):
        self.path = path
    @staticmethod
    def find_word_count(path):
        try:
            with open(path, 'rb') as file:
                content = file.read()
                words = content.split()
                word_count = len(words)
                return word_count
        except FileNotFoundError:
            return -1

    def count_words(self):
        return WordCounter.find_word_count(self.path)
