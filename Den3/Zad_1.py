"""1. Da se napravi programa vo koja korisnikot ke moze 
da vnese 5 elementi vo set"""

set = set() # ako stavam {} vakvi zagradi Python misli deka pravam dictionary i zatoa go koristam zborot set so obicni zagradi

for i in range (5):
    i = int(input("Vnesete element "))
    set.add(i)

print(set)
