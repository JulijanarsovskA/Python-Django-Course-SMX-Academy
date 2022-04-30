"""3. Da se napravi programa vo koja korsnikot ke moze da vnese proizvolen broj na broevi, 
da se prebrojat kolku broevi ke se parni, a kolku ke se ne parni, 
parnite broevi da se pomnozat, a ne parnite da se stepenuvaat megju sebe 
i na kraj da se napravi sporedba koj rezultat e pogolem 
i da se ispecati kolku se bile parni 
a kolku s bile ne parni"""

brojac = 0
brojac_parni = 2
parni_proizvod = 1
brojac_neparni = 0
neparni_stepen = 1

# while broj > 0: - vaka i so def.var 0 ne se startuva programata5

broj = int(input("Kolku broja sakate da vnesete? "))
while brojac < broj:
    vnes = int(input("Vnesete broj: "))
    print(vnes)
    if vnes %2 == 0:
        brojac_parni += 1
        parni_proizvod = vnes * parni_proizvod
        print("Vnesovte {} parni broevi, cii proizvod e {}.".format(brojac_parni, parni_proizvod))
    else:
        brojac_neparni += 1
        neparni_stepen = vnes ** neparni_stepen
        print("Vnesovte {} neparni broevi, cii stepen e {}.".format(brojac_neparni, neparni_stepen))
print(brojac_parni)
print(brojac_neparni)
