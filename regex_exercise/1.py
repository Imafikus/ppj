#!usr/bin/python3
import sys
import re


def main():
    if len(sys.argv) < 2 or re.match(r'^.*\.txt$', sys.argv[1]) is None:
        sys.exit('usage 1.py .txt')

    try:
        with open(sys.argv[1], 'r') as f:
            data = f.read()
    
    except IOError:
        sys.exit("Open failed")
    
    regex = re.compile(r'\b(d|D)([a-z]|[A-Z])+', re.S)
    for match in regex.finditer(data):
        print(match.group())




if __name__ == "__main__":
    main()
