#!/usr/bin/python3

import sys
import re
import os

def main():
    # Obilazimo direktiorijume i trazimo sta imaju, direktorijumi u alas formatu
    if(len(sys.argv > 1)):
        homedir = sys.argv:
    else:
        homedir = '.'

    re_dir = re.compile(
        r'^(m[mnvrlia]|a[aif])' + 
        r'(0[5-9]|1[0-9])''
        r'(00[1-9]|0[1-9]\d|[1-5]\d{2}))$') # alas format
    re_file = re.compile(r'^[1-9]\.(pas|c|cpp|java)$', re.I)

    for f in os.listdir(homedir): # svi direktorijumi
        dir_path = os.path.join(homedir, f)
        match = re_dir.match(f)
        if os.path.isdir(dir_path) and match is not None: # svi direktorijumi koji odgovaraji
            print('\n' + m.group())
            for sf in os.listdir(dirpath): # svi fajlovi
                file_path = os.path.join(dir_path, sf)
                m = re_file.match(sf)
                if os.path.isfile(file_path) and m is not None: # svi fajlovi koji odgovaraju
                    print('\t' + m.group())
                
if __name__ == "__main__":
    #? Nije proban!
    main()