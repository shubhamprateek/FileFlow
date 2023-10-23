class ByteCounter:
    def __init__(self, path):
        self.path = path

    @staticmethod
    def find_byte_count(path):
        try:
            with open(path, 'rb') as file:
                byte_count = len(file.read())
                return byte_count
        except FileNotFoundError:
            return -1

    def count_bytes(self):
        return ByteCounter.find_byte_count(self.path)