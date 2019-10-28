#!/usr/bin/python3

import sys
import re

def main():
    poruka = 'Danas je divan dan'
    #ignorisi velika/mala slova, nadji sve alfanumerike vise puta
    match = re.match(r'(?i)(\w+\s+)+', poruka)    

    if match:
        print(match.group())
    else:
        print('nema poklapanja')

    # trazim prvu rec koje pocinju na d
    m = re.search(r'\bd([a-z]+)', poruka)
    if m:
        print(m.group())

    # trazim sve reci koje pocinju na d, sad mora u zagradu
    m = re.findall(r'\b(d([a-z]+))', poruka)
    if m:
        print(m)
    
    # prosto menjanje stringa
    print(poruka.replace('Danas', 'Sutra'))

if __name__ == "__main__":
    main()