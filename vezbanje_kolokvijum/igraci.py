import re
import sys

def main():
    if len(sys.argv) < 3:
        sys.exit("Wrong num of params")
    
    if sys.argv[2] not in ('-g', '-t'):
        sys.exit("Wrong options")

    if(sys.argv[2] == '-t' and len(sys.argv) < 4):
        sys.exit("Wrong options")

    try:
        with open(sys.argv[1]) as f:
            # data = f.readlines()
            data = f.read()
    except IOError:
        sys.exit("Bad file open")
    
    regex = re.compile(
        r'(?P<ime_igraca>[A-Z][a-z]+(\s+[A-Za-z]*\s+|\s+)[A-Z][a-z]+)' +
        r',\s+(?P<drzava>[A-Z][a-z]+)' + 
        r'(,\s+(?P<broj_golova>([1-9][0-9]*)){1})' +
        r'(,\s+(?P<broj_utakmica>([1-9][0-9]*)){1})' +
        r'(,\s+(?P<godina_pocetak>[12][0-9]{3})-(?P<godina_kraj>([12][0-9]{3})?))' + 
        r'(?P<klubovi>(,\s+[A-Z][A-Za-z0/9 ]*)+)',
        re.S
    )

    # for line in data:
    #     m = regex.match(line)
    #     if m:
    svi_igraci = []
    for m in regex.finditer(data):
        igrac = {}
        igrac['ime_igraca'] = m.group('ime_igraca')
        igrac['drzava'] = m.group('drzava')
        igrac['broj_golova'] = float(m.group('broj_golova'))
        igrac['broj_utakmica'] = float(m.group('broj_utakmica'))
        igrac['godina_pocetak'] = m.group('godina_pocetak')
        igrac['godina_kraj'] = m.group('godina_kraj')
        igrac['klubovi'] = m.group('klubovi').split(', ')[1:]

        svi_igraci.append(igrac)

    if(sys.argv[2] == '-g'):
        for igrac in svi_igraci:
            print(igrac['ime_igraca'], round(igrac['broj_golova'] / igrac['broj_utakmica'], 2), sep='\t')

    if(sys.argv[2] == '-t'):
        club_name = ""
        for part in sys.argv[3:]:
            club_name += part + " "
        club_name = club_name.strip()

        for igrac in svi_igraci:
            print(igrac)
            if club_name in igrac['klubovi']:
        
                godina_kraj = igrac['godina_kraj']
        
                if godina_kraj == "": godina_kraj = 2018
                
                duzina_karijere = int(godina_kraj) - int(igrac['godina_pocetak'])
                print(igrac['ime_igraca'], igrac['godina_pocetak'], duzina_karijere, sep='\t')




    #logika za flegove

if __name__ == "__main__":
    main()