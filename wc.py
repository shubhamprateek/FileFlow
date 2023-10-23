import sys
import argparse
def find_byte_count(path):
    try:
        with open(path, 'rb') as file:
            byte_count = len(file.read())
            return byte_count
    except FileNotFoundError:
        return -1
def main():
    parser = argparse.ArgumentParser(description="wc - Count the number of bytes in a file")
    parser.add_argument("-c", "--count", metavar="FILE", help="Count the number of bytes in the specified file", required=True)

    args = parser.parse_args();

    byte_count = find_byte_count(args.count);
    if byte_count == -1:
        print(f"wc {args.count} : No such file or directory")
    else:
        print(f"{byte_count} {args.count}")

if __name__ == '__main__':
    main()

