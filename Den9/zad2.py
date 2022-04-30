"""2.Da se napravi klasa Vozilo 
vo koja ke moze da se cuvaat Markata, modelot, godinata, bojata, kolicina, cena. 
Za sekoj podatok da ima poseben get i set metod, 
da ima metod koj ke presmeta kolku godini e staro voziloto, 
metod so koj ke se ispecati poraka koja ke gi sodrzi site podatoci, 
metod so koj ke moze da se startuva voziloto i ke se pecati poraka 
"Voziloto {marka} {model} se staruvase, 


metod so koj ke moze da se prodade vozilo, 
da se presmeta kolku treba da se plati i da se odzeme od kolicinata

Da se kreiraat 3 objekti so podatoci koi ke gi vnese korisnikot, i da se probaat site metodi...po vas izbor
"""

from sre_parse import GLOBAL_FLAGS


class Vozilo:
    def __init__(self, marka, model, godina, boja, kolicina, cena):
        self.marka = marka
        self.model = model
        self.godina = godina
        self.boja = boja
        self.kolicina = kolicina
        self.cena = cena
# get metod    
    def getmarka(self):
        print("markata na voziloto e {}.".format(self.marka))
        return self.marka
    def getmodel(self):
        print("Modelot na voziloto e {}.".format(self.model))
        return self.model
    def getgodina(self):
        print("Godinata na voziloto e {}.".format(self.godina))
        return self.godina
    def getboja(self):
        print("Bojata na voziloto e {}.".format(self.boja))
        return self.boja
    def getkolicina(self):
        print("Kolicinata na voziloto e {}.".format(self.kolicina))
        return self.kolicina
    def getcena(self):
        print("Godinata na voziloto e {}.".format(self.cena))
        return self.cena
# set metod
    def setnovaMarka(self, novaMarka):
        print("Novata markata na voziloto e {}.".format(self.marka)) # vaka ke ja isprinta starata vrednost
        self.marka = novaMarka
        print("Novata markata na voziloto e {}.".format(self.marka))  # tuka ostanuva self.marka, no ke ja vrati novata marka!!!
        return novaMarka # ne mora return da stoi, no ako stoi treba da se vraka samo novaMarka (bez da bide definirana kako promeliva)
    def setNovModel(self, NovModel):
        print("Modelot na voziloto e {}.".format(self.model))
        self.model = NovModel
    def getNovagodina(self, NovaGodina):
        print("Godinata na voziloto e {}.".format(self.godina))
        self.godina = NovaGodina
    def getNovaBoja(self, NovaBoja):
        print("Bojata na voziloto e {}.".format(self.boja))
        self.boja = NovaBoja
    def getNovaKolicina(self, NovaKolicina):
        print("Kolicinata na voziloto e {}.".format(self.kolicina))
        self.kolicina = NovaKolicina
    def getNovaCena(self, NovaCena):
        print("Godinata na voziloto e {}.".format(self.cena))
        self.cena = NovaCena
# starost na vozilio
    def starost(self):
        return 2022 - self.godina
# podatoci za vozilo
    def podatoci(self):
        print("Voziloto marka {}, model {}, e proizvedeno vo {}, ima {} boja, kolicina {} i kosta {}". format(self.marka, self.model, self.godina, self.boja, self.kolicina, self.cena))
# strartuvanje na vozilo    
    def startuvanje(self):
        print("Voziloto {} {} se staruvase.". format(self.marka, self.model))
# prodazba na vozilo
    def prodazba(self):
        return self.kolicina - 1
# nova kolicina posle porodazba    
    def setNovaKolicina2(self, NovaKolicina2):
        self.kolicina = NovaKolicina2
        print("Vzaliha ostanuvaat {} vozila.".format(self.kolicina))
        return NovaKolicina2
# da se presmeta kolku treba da se plati
    def plakanje(self):
        return self.cena 

#obj1_golf = Vozilo("Golf", "7", 2017, "crna", 19, 10000)
#obj2_pezo = Vozilo("Pezo", "6", 2012, "bela", 34, 5000)
#obj3_mercedes = Vozilo("Mercedes", "18", 2021, "crvena", 56, 15000)

#korisnikot vnesuva
marka_golf = input("Vnesi marka na vozilo: ")
model_7 = input("Vnesi model na vozilo: ")
godina_2017 = int(input("Vnesi godina na vozilo: "))
boja_crna = input("Vnesi boja na vozilo: ")
kolicina_19 = int(input("Vnesi kolicina na vozilo: "))
cena_10000 = input("Vnesi cena na vozilo: ")

#ova e povikuvanje na klasata?
obj1_golf = Vozilo(marka_golf, model_7 , godina_2017, boja_crna, kolicina_19, cena_10000)

# ova e povikuvanje na metod za starost na vozilo?
starost = obj1_golf.starost()
print(starost)

# ova e povikuvanje na metod za pecatenje na podatoci za volizo?
obj1_golf.podatoci()
obj1_golf.startuvanje()

prodadeno = obj1_golf.prodazba()
print(prodadeno)



