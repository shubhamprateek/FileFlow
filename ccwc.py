import sys
import argparse
from utils.byte_counter import ByteCounter
from utils.line_counter import LineCounter
from utils.word_counter import WordCounter

def main():
    parser = argparse.ArgumentParser(description="ccwc - File operations")
    parser.add_argument("-c", "--count", metavar="FILE", help="Count the number of bytes in the specified file", required=False)
    parser.add_argument("-l", "--lines", metavar="FILE", help="Count the number of lines in the specified file", required=False)
    parser.add_argument("-w", "--words", metavar="FILE", help="Count the number of words in the specified file", required=False)

    args = parser.parse_args();

    if args.count:
        byte_counter = ByteCounter(args.count)
        byte_count = byte_counter.count_bytes()
        if byte_count == -1:
            print(f"ccwc {args.count} : No such file or directory")
        else:
            print(f"{byte_count} {args.count}")

    if args.lines:
        line_counter = LineCounter(args.lines)
        line_count = line_counter.count_lines()
        if line_count == -1:
            print(f"ccwc {args.lines} : No such file or directory")
        else:
            print(f"{line_count} {args.lines}")

    if args.words:
        word_counter = WordCounter(args.words)
        word_count = word_counter.count_words()
        if word_count == -1:
            print(f"ccwc {args.words} : No such file or directory")
        else:
            print(f"{word_count} {args.words}")

if __name__ == '__main__':
    main()

