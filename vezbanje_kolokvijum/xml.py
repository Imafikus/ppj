import sys
import re


def main():

    if len(sys.argv) != 2:
        sys.exit("bad params")

    try:
        with open(sys.argv[1], 'r') as f:
            data = f.read()
        
    except IOError:
        sys.exit("Error on file open")


    regex = re.compile(
        r'\s*<PLANT>' + 
        r'(?=((?!</PLANT>).)*?<BOTANICAL>\s*(?P<botanical>[A-Za-z ]+)\s*</BOTANICAL>)' +
        r'(?=((?!</PLANT>).)*?<COMMON>\s*(?P<common>[A-Za-z]+)\s*</COMMON>)' + 
        r'(?=((?!</PLANT>).)*?<LIGHT>\s*(?P<light>([A-Z][A-Za-z]+) ([A-Z][A-Za-z]+))\s*</LIGHT>)' + 
        r'(?=((?!</PLANT>).)*?<PRICE>\s*(?P<price>\$[1-9][0-9]*\.[0-9]{2})\s*</PRICE>)' + 
        r'(?=((?!</PLANT>).)*?<AVAILABILITY>\s*(?P<availability>[0-9]{6})\s*</AVAILABILITY>)' + 
        r'.*?' #+ 
        r'\s+</PLANT>'        
        ,re.S
    )

    for m in regex.finditer(data):
        print(m.group('common'))
        print(m.group('botanical'))
        print(m.group('light'))
        print(m.group('price'))
        print(m.group('availability'))
        print(" ")
    
    
if __name__ == "__main__":
    main()