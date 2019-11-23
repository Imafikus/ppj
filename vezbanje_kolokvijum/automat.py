import sys

def main():
    stanje = "A"
    kranje_stanje = "E"

    prelaz = {
        ("A", "a"): "A",
        ("A", "b"): "B",

        ("B", "a"): "C",
        ("B", "b"): "B",

        ("C", "a"): "D",
        ("C", "b"): "B",

        ("D", "a"): "A",
        ("D", "b"): "E",

        ("E", "a"): "E",
        ("E", "b"): "E"
    }

    string = sys.argv[1]

    for char in string:
        if char not in ("a", "b"):
            exit("Bad char")
        
        stanje = prelaz[(stanje, char)]
    
    if stanje == kranje_stanje:
        print("string sadrzi 'baab'")
    else:
        print("kurcina")

if __name__ == "__main__":
    main()