"""Da se napravi programa vo koja ke se podeli smetka. Korisnikot vnesuva cela suma i 
vnesuva kolku lica ke ja pokrijat smetkata, 
i da se opredeli sekoe lice kolku treba da plati"""

vkupna_suma = int(input("Vnesete vkupna suma na smetkata "))
lica = int(input("Vnesete kolku lica ke ja platat smetkata "))

individualna_suma = vkupna_suma / lica

print("Vasata smetka iznesuva {} denari. Smetkata ke ja pokrijat {} lica. Sekoj od niv treba da plati po {} denari. ".format(vkupna_suma, lica, individualna_suma))