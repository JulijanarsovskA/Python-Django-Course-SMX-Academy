"""1. Da se napravi programa vo koja ke imate dictionary so licni podatoci za nekoj korisnik
(ime, prezime, mesto na ziveenje, datum na ragjanje, pol)

	- Da moze da se ispecati poraka vo format: "Korisnikot so {ime} {prezime}, koj zivee na {mesto na ziveenje} e roden na {datum na ragjanje}"
	*BONUS* - Da se ispecatat site klucevi 
    i korisnikot da izbere koj podatok da se ispecati vo format: kluc: podatok
    4.3. i korisnikot gi vnesuva podatocite na kraj za site 
"""
podatoci = {'ime':'Todor', 'prezime':'Todorovski', 'grad':'Veles', 'datum_r':1986, 'pol':'M'}

"""ime = podatoci.get('ime')
prezime = podatoci.get('prezime')
grad = podatoci.get('grad')
datum_r = podatoci.get("datum_r")
pol = podatoci.get('pol')"""

podatoci2 = {}

ime = input("Vnesete 'ime': ")
podatoci2.update({"ime":ime})
prez = input("Vnesete 'prezime': ")
podatoci2.update({"prezime":prez})
grad = input("Vnesete klucen zbor za 'grad': ")
datum = input("Vnesete klucen zbor za 'datum': ")

imeV = input("Vnesete vrednost za klucniuot zbor ime: ")
podatoci2.update({'imeK)
prezime = podatoci.get('prezime')
grad = podatoci.get('grad')
datum_r = podatoci.get("datum_r")
pol = podatoci.get('pol')

#print("Korisnikot so ime {} i prezime {}, koj zivee vo {} e roden vo {} god".format(ime, prezime, grad, datum_r))

klucevi = podatoci.keys()
print(klucevi)

"""izbor_kluc = input("Izberete kluc")
print(podatoci.keys(izbor_kluc))

izbor_vednost= input("Izberete vrednost")
print(podatoci.values(izbor_vrednost))"""

