"""Da se vnesat tri golemini na agli 
i da se proveri dali moze da se napravi ptriagolnik so tie dimenzii na agli. 
Dali zbirot na aglite e 180."""

a = int(input("Vnesete golemina na agol 'a' "))
b = int(input("Vnesete golemina na agol 'b' "))
c = int(input("Vnesete golemina na agol 'c' "))

triagolnik = a+b+c

if triagolnik == 180:
    print("So vnesenite dimenzii moze da napravite triagolnik")
else:
    print("So vnesenite dimenzii ne  moze da napravite triagolnik. Obidete se povtorno!")