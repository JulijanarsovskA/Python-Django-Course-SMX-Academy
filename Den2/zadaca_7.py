"""7.Da se napravi programa vo koja korisnikot ke napolni prazna niza, 
da se najde najgolemiot i najmaliot broj, 
i tie da se pomonozat megju sebe.
"""

lista = []

vnes = int(input("Vnesi vkupno elementi"))

for element in range(vnes):
    broj = int(input("vnesete broj"))
    lista.append(broj)

print(lista)

min = min(lista)
max = max(lista)

proizvod = min * max 
print(proizvod)
