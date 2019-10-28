
import sys

def main():
    stanje = 'P'
    zavrsno = 'P'
    prelaz = {
        ('P', '0'): 'N',
        ('P', '1'): 'P',
        ('N', '0'): 'P',
        ('N', '1'): 'N'
    }
        
    c = input('Unesite 0 ili 1')

    if c != '0' and c != '1':
        sys.exit('Pogresan unos!')

    if prelaz.get(stanje, c) is not None:
        stanje = prelaz[(stanje, c)]
    else:
        sys.exit('Nepostojece stanje')

    if stanje == zavrsno:
        print('Unet je paran broj nula')
    else:
        print('Unet je neparan broj nula')

if __name__ == "__main__":
    main()