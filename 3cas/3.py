#!/usr/bin/python3

import sys
import re

def main():
    # imamo html fajl sa poenima, imenima, itd... treba da iscupamo broj poena za svakog studenta
    # single line mode koristimo kada imamo podatke u vise redova (npr u html fajlu)
    # DEFAULT JE MULTILINE !!!

    if len(sys.argv) < 2:
        sys.exit("Fale argumenti")

    # trazi sve sa .txt ekstenzijom, ignorise velika/mala slova (IGNORECASE)
    if re.match(r'^.+\.html$', sys.argv[1], re.I) is None:
        sys.exit("Losa ekstenzija")

    try:
        with open(sys.argv[1], 'r') as f:
            podaci = f.read()
    except IOError:
        sys.exit('fajl ne postoji')
    
    ri = re.compile(
        r'<tr>' + # trazimo tr
        r'\s*<td>\s*(?P<ime>[A-Z][a-z]+(\s+[A-Z][a-z]+)+)\s*</td>' + # trazimo td koji moze da ima proizvoljan broj razmaka sa obe strane, ?P je ime i ignorise se
        r'\s*<td>\s*(?P<prakticni>\d|[1-9]\s|100)\s*</td>' + # broj poena, moze biti od 0-99 i 100 
        r'\s*<td>\s*(?P<teorija>\d|[1-9]\s|100)\s*</td>' + 
        r'\s*</tr>',
        re.S # Single line mode
    )
    studenti = []
    poeni = []

    #? Ovo ispod se ne koristi
    # m = ri.search(podaci)
    
    # while m is not None:
    #     studenti.append(m.group('ime'))
    #     ukupno = int(m.group('prakticni') + int(m.group('teorija'))) / 2
    #     poeni.append(ukupno)

    #     m = ri.search(podaci, m.end())
    
    for m in ri.finditer(podaci):
        studenti.append(m.group('ime'))
        ukupno = int(m.group('prakticni') + int(m.group('teorija'))) / 2
        poeni.append(ukupno)

    parovi = sorted(zip(poeni, studenti)) # sortira po prvoj koloni
    parovi.reverse() # obrnemo da bude rastuce
    for p, s, in parovi:
        print(p, s)
if __name__ == "__main__":
    # ? Videti sto ne radi!
    main()