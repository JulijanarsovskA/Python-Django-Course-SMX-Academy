"""1. Da se napravi funkcija koja ke gi ispecati site broevi koi se dellivi so 5 pomegju 2734 i 3000, 
da gi vrati kako lista, 

da se napravi druga funkcija koja ke gi kvadrira elementite od listata 
i ke vrati nova lista
"""

def dell_5():
    lista5 = []
    for i in range(2734, 3001):
        if i %5 == 0:
            lista5.append(i)
    return lista5

def kvadriranje(lista5):
    lista_2 = []
    for num in lista5:
        num2 = num**2
        lista_2.append(num2)
    return lista_2

x = dell_5()
y = kvadriranje(x)

print(x)
print(y)


