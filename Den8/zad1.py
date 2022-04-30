"""3. Da se napravi programa vo koja korisnikot ke moze da vnesuva otceni za nekoja ucenik, 
da se presmeta prosekot, 
i da se najde najvisokata otcena
"""
try:
    broj_oceni = int(input("Kolku oceni sakate da vnesete? "))
except ValueError:
    print("Vnesovte zbor, a treba da vnesete broj")
    broj_oceni = int(input("Kolku oceni sakate da vnesete? "))
except:
    print("Vnesovte 0, a takva ocenka ne postoi")

    broj_oceni = int(input("Kolku oceni sakate da vnesete? "))
oceni = []

for ocena in range(broj_oceni):
    vnes_ocena = int(input("Vnesete ocena na ucenikot: "))
    if vnes_ocena > 5:
        print("Vnesovte pogresna ocena") 
    else:
        oceni.append(vnes_ocena)

max_ocena = max(oceni)

zbir = sum(oceni)
prosek = zbir / len(oceni)
  
    
print("Ucenikot gi ima slednite oceni {}, so prosek {}, a najvisoka ocena e {}". format(oceni, prosek, max_ocena))



