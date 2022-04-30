"""2. Da se napravi programa koja ke go prasuva korisnikot da vnese broj 
se dodeka brojot koj ke go vnese e ili paren ili pak e pogolem od 100, 
da se prebrojat kolku parni broevi ke se vnesat
i das e ispecati kolku parni broevi bile vneseni"""

broj = 2
parni = 0

while broj %2 == 0 or broj > 100:
    broj = int(input("Vnesete broj: "))
    if broj %2 == 0:
        parni +=1 # parni += broj # vaka gi sobira parnite proevi, 
        # dodeka parni +=1 dodava edinica na promenlivata parni koja sluzi kako brojac"""

print("Vnesovte {} parni broevi.".format(parni))
    
