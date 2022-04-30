"""3. Da se napravi programa vo koja korisnikot ke moze da vnese 4 broevi, 
da se najde zbirot na tie 4 broevi 
i da se presmeta prosekot, 
i zbirot i prosekot da se zacuvaat vo dictionary
"""

num = {}

b1 = int(input("Prv broj: "))
b2 = int(input("Prv broj: "))
b3 = int(input("Prv broj: "))
b4 = int(input("Prv broj: "))

num['num1'] = b1
num['num2'] = b2
num['num3'] = b3
num['num4'] = b4
num['zbir'] = num['num1'] + num['num2'] + num['num3'] + num['num4']
num['prosek'] = num['zbir'] / len(num)

print("Zbirot na vnesenite broevi iznesuva {}, a prosekot e {}.".format(num['zbir'], num['prosek']))