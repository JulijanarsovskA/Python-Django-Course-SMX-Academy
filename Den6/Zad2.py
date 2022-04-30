"""
2. Da se napravi programa koja bi bila za potrebite na nekoj supermarket
	-da ima funkcija za dodavanje na produkti vo marketot
	-da ima funkcija za prodazba
	
*funkcijata za dodavanje na produkti ke treba da 
imeto na produktot, kolicina i cena da gi dodade vo lista ili dictionary(ostanuva na vas da odlucite sto)

*funkcijata za prodavanje ke treba da 
zema lista / dictionary so produkti i kolicini, 
da presmeta kolku klientot ke treba da plati i 
otkako ke plati da se odzemat tie kolicini od soodvetnite produkti
"""
"""
product={
    ime:leb
    leb:{kolicina:13, cena:30}
}

"""
def roba(product):
    artikl = input("Vnesete ime na produkt: ")
    product[artikl] = {}
    product[artikl]['kolicina'] = int(input("Vnesete kolicina na productot "))
    product[artikl]['cena'] = int(input("Vnesete cena na produktot "))
    return product 
x = {}
x = roba(x)

x = roba(x)
print(x)

def prodadeno():
    