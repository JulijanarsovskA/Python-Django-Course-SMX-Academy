"""-korisnikot da moze da gi vnesuva broevite
	-na funkcijata za delenje na vtoriot parametar dodelete defaultna vrednost 1
"""
n1 = int(input("Vnesi br: "))
n2 = int(input("Vnesi br: "))

def sobiranje(n1, n2):
    zbir = n1 + n2
    print("{} + {} = {}".format(n1, n2, zbir))

def odzemanje(n1, n2):
    razlika = n1 - n2
    print("{} - {} = {}".format(n1, n2, razlika))

def mnozenje(n1, n2):
    proizvod = n1 * n2
    print("{} * {} = {}".format(n1, n2, proizvod))

def delenje(n1, n2=1):
    kolicnik = n1 / n2
    print("{} / {} = {}".format(n1, n2, kolicnik))

sobiranje(n1, n2)
odzemanje(n1, n2)
mnozenje(n1, n2)
delenje(n1)