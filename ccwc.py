import sys
import argparse
from utils.byte_counter import ByteCounter

def main():
    parser = argparse.ArgumentParser(description="wc - Count the number of bytes in a file")
    parser.add_argument("-c", "--count", metavar="FILE", help="Count the number of bytes in the specified file", required=True)

    args = parser.parse_args();
    byte_counter = ByteCounter(args.count)
    byte_count = byte_counter.count_bytes()
    if byte_count == -1:
        print(f"wc {args.count} : No such file or directory")
    else:
        print(f"{byte_count} {args.count}")

if __name__ == '__main__':
    main()

