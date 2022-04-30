"""3. Da se napravi proggrama vo koja ke imame funkcija koja od 3 broevi ke go najde najgolemiot, 
ke go vrati vo promenliva i ke se ispecati soodvetna poraka
"""

#moze i so funkcija max

x = int(input("Vnesete broj: "))
y = int(input("Vnesete broj: "))
z = int(input("Vnesete broj: "))

def najgolemBroj(x, y, z):
    if x > y and x > z:
        print("Brojot {} e najgolem".format(x))
        return x
    elif y > x and y > z:
        print("Brojot {} e najgolem".format(y))
        return y
    else:
        print("Brojot {} e najgolem".format(z))
        return z

najgolemBroj(x, y, z)
