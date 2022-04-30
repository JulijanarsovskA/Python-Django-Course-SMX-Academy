"""3. Da se kreira klasa User vo koja ke moze da se cuvaat 
ime, prezime, data na ragjanje, email, password, username za odreden korisnik. 
Da ima get i set metodi za sekoj parametar. 

Da ima login metod kade korisnikot ke treba da gi dade usernameot i passwordot kako parametri 
ako se tocni da se napise poraka logiran ste, 
ako se gresni da mu se dade moznost do 3 pati da moze da gi zgresi.
Ako se zgreseni 3 pati da se izbrise objektot / korisnikot
Da ima metod so koj ke moze da se promene passwordot, ama ovaa operacija da e dostapna samo ako korisnikot e logiran

I da se odlogira ako saka da se odlogira
"""   

class User:
    def __init__(self, ime, prezime, data, email, password, username, x=3):
        self.ime = ime
        self.prezime = prezime
        self.data = data
        self.email = email
        self.password = password
        self.username = username
        self.x = x

#GET metodi       
    def getIme(self):
        return self.ime

    def getPrezime(self):
        return self.prezime

    def getData(self):
        return self.data

    def getEmail(self):
        return self.email

    def getPassword(self):
        return self.password

    def getUsername(self):
        return self.username

#SET metodi
    def setIme(self, novoIme):
        self.ime = novoIme
        return self.ime

    def setPrezime(self, novoPrezime):
        self.prezime = novoPrezime
        return self.prezime

    def setData(self, novaData):
        self.data = novaData
        return self.data

    def setEmail(self, novEmail):
        self.email = novEmail
        return self.email

    def setPassword(self, novPassword):
        self.password = novPassword

#login metod
    def login(self):
        count = 0
        for logUser in range(3):
            username1 = input("Vnesete go vaseto korisnicko ime: ")#za
            password1 = input("Vnesete go vasiot password: ")
            if username1 == self.username and password1 == self.password:
                print("Logiran/a ste ")#zac 
            else:
                count += 1
                return ("Obidete se poctorno")
                

user1_ime = input("Vnesete go vaseto ime: ")
user1_prezime = input("Vnesete go vaseto prezime: ")
user1_email = input("Vnesete go vaseto email: ")
user1_data= input("Vnesete go vasiot datum na raganje: ")
user1_username = input("Vnesete go vaseto korisnicko ime: ")
user1_password = input("Vnesete go vasiot password: ")

user1 = User(user1_ime, user1_prezime, user1_data, user1_email, user1_password, user1_username)

user1_log_name = user1.loginUsernamePassword()
print(user1_log_name)






"""Da ima login metod kade korisnikot ke treba da gi dade usernameot i passwordot kako parametri 
ako se tocni da se napise poraka logiran ste, 
ako se gresni da mu se dade moznost do 3 pati da moze da gi zgresi.
Ako se zgreseni 3 pati da se izbrise objektot / korisnikot
""" 