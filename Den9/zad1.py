"""1. Da se napravi klasa Kvadrat vo koja 
ke moze da cuva stranata na kvadratot, 
da imame get i set methodi za stranata, 
da imame metodi za presmetuvanje na plostina i presmetuvanje na perimetar.

Da se kreiraat 2 objekti od Klasta Kvadrat so vrednosti koi ke gi kaze korisnikot, 
da se sporedat stranite od dvata objekti i da se ispecati koj objekt ima pogolema strana, 
da se presmetaat plostinite i perimetrite
"""

class Kvadrat:
    def __init__(self, strA):
        self.strA = strA        #dali ovoj metod e za zacuvuvanje na stranata?
    
    def getStrA(self):
        return self.strA   # ova e get metod

    def setA(self, strana):
        self.strA  = strana   # ova e set metod
    
    def Plostina(self):
        return self.strA ** 2   # ova e metod za plostina

    def Perimetar(self):
        return self.strA * 4    # ova e metod za perimetar

o1 = int(input("Vnesete broj za object 1: "))
object1 = Kvadrat(o1)
plostina = object1.Plostina()           #object1 e object, a plostina e funkcija ili metod
perimetar = object1.Perimetar()
print(perimetar)
print(plostina)

o2 = int(input("Vnesete broj za object 2: "))
object2 = Kvadrat(o2)
perimetar = object2.Perimetar()
plostina = object2.Plostina()
print(perimetar)
print(plostina)

if o1 > o2:
    print("Object 1 ima pogolema strana")
else:
    print("Object 2 ima pogolema strana")

