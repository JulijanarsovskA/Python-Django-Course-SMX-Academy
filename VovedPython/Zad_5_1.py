"""1. Da se napravi programa koja ke go prasuva korisnikot 
da vnese broj se dodeka brojot koj ke go vnese e pogolem od deset a e pomal od 100"""

broj = 11 #ako pocetnata vrednost e 0, programata nema da startuva, nema ni da se pojavi "Vnesete broj"
#broj = int(input("Vnesete broj ")) # moze da raboti i vaka 

while broj > 10 and broj <100:
    broj = int(input("Vnesete broj "))
    print(broj)