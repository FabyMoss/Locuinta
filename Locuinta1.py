class Imobil:
    def __init__(self, nume_proprietar, nr_cam, pret_vanzare, dimensiune, poze, client_poten, valoare_oferta):
        self.nume_proprietar = nume_proprietar
        self.nr_cam = nr_cam
        self.pret_vanzare = pret_vanzare
        self.dimensiune = dimensiune
        self.poze = poze
        self.client_poten = client_poten
        self.valoare_oferta = valoare_oferta


class Teren(Imobil):
    def __init__(self, nume_proprietar, locatie, nr_cam, pret_vanzare, dimensiune, poze, client_poten, valoare_oferta):
        super().__init__(nume_proprietar, nr_cam, pret_vanzare, dimensiune, poze, client_poten, valoare_oferta)
        self.locatie = locatie
class Apartament(Imobil):
    def __init__(self, nume_proprietar, locatie, nr_cam, pret_vanzare, etaj, dimensiune, poze, client_poten, valoare_oferta):
        super().__init__(nume_proprietar, nr_cam, pret_vanzare, dimensiune, poze, client_poten, valoare_oferta)
        self.etaj = etaj
class Casa(Imobil):
    def show(self):
        print(f"{self.pret_vanzare}")



class Persoana:
    def __init__(self, nume, varsta, email, telefon):
        self.nume = nume
        self.varsta = varsta
        self.email = email
        self.telefon = telefon

class Proprietar(Persoana):
    def show(self):
        print(f"Eu ma numesc {self.nume}, am {self.varsta}, email-ul {self.email} si nr de telefon {self.telefon} si sunt proprietarul locuintei")
        return Proprietar.show(self)
class Agent(Persoana):
    def show(self):
        print(f"Eu ma numesc {self.nume}, am {self.varsta}, email-ul {self.email} si nr de telefon {self.telefon} si sunt agentul de vanzare al locuintei")
        return Agent
class Client(Persoana):
    def __init__(self, nume, varsta, email, telefon, buget, locatii):
        super().__init__( nume, varsta, email, telefon)
        self.buget = buget
        self.locatii = locatii
        print(self.nume, self.varsta, self.email, self.telefon, self.buget, self.locatii)
s = Agent('sd', )
p = Proprietar('Mos', 18, 'faby', '0755')
p.show()
a = Agent('Alex', 19, 'alex@', '0766')
a.show()
c = Client('Art', 20, 'oop@', '099', 1000, 'Centru')

class Poze:
    def __init__(self, URL, nr_ord, desc):
        self.URL = URL
        self.nr_ord = nr_ord
        self.desc = desc
    def show(self):
        print(self.URL, self.nr_ord, self.desc)

poza = Poze('Imgur.com', 76, 'da')
poza.show()
