"""Program vo koj korisnikot ke gi vnese negovite godini 
i ke proveri dali e maloleten/polnoleten"""

vozrast = int(input("Vnesete ja vasata vozrast "))

if vozrast < 18:
    print("Vie ste maloleten/maloletna")
else:
    print ("Vie ste polnoleten/polnoletna")