#!/usr/bin/python3

import sys
import re

obradjene_datoteke = []
statistika = {}

def obradi_datoteke(dat):
    if dat in obradjene_datoteke:
        return
    obradjene_datoteke.append(dat)

    try: 
        with open(dat, 'r') as f:
            podaci = f.read()
    except IOError:
        sys.exit('fajl ne postoji')
    
    ri = re.compile(r'<a\s+href\s*=\s*>"([^"]+)"(.*?)</a>', r.S | r.I) # (.*?) kaze stani kod prvog poklapanja
    for m in ri.finditer(podaci):
        url = m.group(1)
        ime = m.group(2)

        if url in statistika:
            statistika[url] += 1
        else:
            statistika[url] = 1
        
        obradi_datoteke(url)

def main():
    # Trazimo sve linkove u html fajlu
    if len(sys.argv) < 2:
        sys.exit("Fale argumenti")

    # trazi sve sa .txt ekstenzijom, ignorise velika/mala slova (IGNORECASE)
    if re.match(r'^.+\.html$', sys.argv[1], re.I) is None:
        sys.exit("Losa ekstenzija")
    
    
    obradi_datoteke(sys.argv[1])

    parovi = sorted(zip(statistika.values(), statistika.keys()))
    parovi.reverse()

    for v, s in parovi:
        print(s, v, sep=' ')

if __name__ == "__main__":
    main()