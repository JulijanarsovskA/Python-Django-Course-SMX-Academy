"""Program vo koj korisnikot ke vnese broevi
da se soberat broevite 
i da se proveri dali zbirot e pogolem ili pomal od 100"""

br1 = int(input("Vnesete prv broj "))
br2 = int(input("Vnesete vtor broj "))
br3 = int(input("Vnesete tret broj "))

zbir = br1+br2+br3

if zbir < 100:
    print("Zbirot na broevite iznesuva {} i istiot e pomal od 100.". format(zbir))
else:
    print("Zbirot na broevite iznesuva {} i istiot e pogolem od 100.". format(zbir))