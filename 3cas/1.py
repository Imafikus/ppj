#!/usr/bin/python3

import sys
import re


def main():
    if len(sys.argv) < 2:
        sys.exit("Fale argumenti")

    # trazi sve sa .txt ekstenzijom, ignorise velika/mala slova (IGNORECASE)
    if re.match(r'^.+\.txt$', sys.argv[1], re.I) is None:
        sys.exit("Losa ekstenzija")

    # trazi samo reci koje se poklapaju pogledati 1.txt
    ri = re.compile(r'(\b[a-zA-z]+\b)\s+\1')

    try:
        f = open(sys.argv[1], 'r')
    except IOError:
        sys.exit('bad open')
    
    for line in f:
        match = ri.search(line) # trazi prvo poklapannje
        if match is not None:
            print('Poklapanje: %s\n groups: %s'%(match.group(), match.groups()) )
            print('Linija bez ponavljanja: ', ri.sub('bilo sta', line))
    f.close()

    try:
        f = open(sys.argv[1], 'r')
        data = f.read()
    except IOError:
        sys.exit('bad open')
    
    # finditer trazi sva poklapanja
    for m in re.finditer(r'(\b[a-zA-z]+\b)\s+\1', data, re.I):
        print(m.group())

if __name__ == "__main__":
    main()