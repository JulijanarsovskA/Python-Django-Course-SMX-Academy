"""Napravi programa vo koja korisnikot ke vnese 3 broja i da presmeta r = (a+b) / a-c**b. Da se ispecati cel izraz!"""

a = int(input("Vnesete broj za 'a' "))
b = int(input("Vnesete broj za 'b' "))
c = int(input("Vnesete broj za 'c' "))

r = (a+b)/a-c**b

print(r)
print("{} = ({} + {}) / {} - {} ** {}". format(r, a, b, a, c, b))