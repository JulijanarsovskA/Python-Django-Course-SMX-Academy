"""4. Da se napravi programa vo koja korisnikot ke moze da vnese odredeni broevi, 
parnite broevi da se dodadat vo edna niza, ne parnite vo druga. 
Parnite broevi da se soberat i da se pomnozat po brojot na ne parnite
"""

try:
    broevi = int(input("Kolku broevi sakate da vnesete? "))
except ValueError:
    print("Vnesovte zbor, a treba da vnesete broj")
    broevi = int(input("Kolku broevi sakate da vnesete? "))

parni = []
neparni = []

for broj in range(broevi):
    try:
        broj = int(input("Vnesete broj: "))
    except ValueError:
        print("Vnesovte zbor, a treba da vnesete broj")
        broj = int(input("Vnesete broj: "))
    
    if broj % 2 == 0 and broj % 2 != 0:
        parni.append(broj)
    else:
        neparni.append(broj)
    
zbir_parni = sum(parni)
vk_neparni = len(neparni)

rezultat = zbir_parni * vk_neparni
print("Gi vnesovte slednite parni broevi {}, neparni broevi {}. Proizvodot pomegu zbirot na parnite broevi i neparnite broevi e {}.".format(parni, neparni, rezultat))

