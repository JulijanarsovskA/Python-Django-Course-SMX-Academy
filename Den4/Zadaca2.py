"""2. Da se napravi programa vo koja korisnikot ke moze da vnese tri broja vo keys (brojEden, brojDva, brojTri)
 vo key zbir da se zacuva zbirot na prvite dva broevi, 
 vo key proizvod da se zacuva proizvodot na vtorite dva broevi, 
 a vo key pogolem da se zacuva pogolemiot od dvata rezultati. 
 Da se ispecatat site potrebni podatoci za programta. 
 Formatot ostanuva na vas
"""
programa = {}

broj1 = int(input("Vnesete eden broj: "))
broj2 = int(input("Vnesete vtor broj: "))
broj3 = int(input("Vnesete tret broj: "))

programa['broj1'] = broj1
programa['broj2'] = broj2
programa['broj3'] = broj3
programa['zbir_1_2'] = programa['broj1'] + programa['broj2']
programa['proizvod_2_3'] = programa['broj2'] * programa['broj3']

if programa['zbir_1_2'] > programa['proizvod_2_3']:
    print("Zbirot {} na prvite dva broja e pogolem od proizvodot {} na vtorite dva broja".format(programa['zbir_1_2'], programa['proizvod_2_3']))
else:
    print("Proizvodot {} na vorite dva broj e pogolem od zbirot {} na prvite dva broja ".format(programa['proizvod_2_3'], programa['zbir_1_2']))

