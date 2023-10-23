class LineCounter:
    def __init__(self, path):
        self.path = path
    @staticmethod
    def find_line_count(path):
        try:
            with open(path, 'rb') as file:
                line_count = 0
                for line in file:
                    line_count += 1
                return line_count
        except FileNotFoundError:
            return -1

    def count_lines(self):
        return LineCounter.find_line_count(self.path)
