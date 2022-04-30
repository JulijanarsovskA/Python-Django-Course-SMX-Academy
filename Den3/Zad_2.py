""" 2. Da se napravi programa vo koja korisnikot ke moze da vnese proizvolen broj na elementi vo set,
 da se pomine niz elementite so setot i parnite da se dodadat vo drug set,
  a ne patnite vo drug"""

setBasic = set()
setP = set()
setN = set()
i=0
vkupnoElementi = int(input("kOLKU ELEMENTI SAKATE DA VNESETE?"))

"""ako sakame da koristime while loop, togas treba da vneseme opcija dali korisnikot da prodolzi da vnesuvva
so prodolzi == "da"""

for i in range(vkupnoElementi):
    i = int(input("Vnesete vkupno elementi"))
    elementi = setBasic.add(i)
    if i %2 == 0:
        setP.add(i)
    else:
        setN.add(i)    

print(setP)
print(setN)

