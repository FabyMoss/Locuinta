class Imobil():
    def __init__(self, nume_proprietar, nr_cam, pret_vanzare, dimensiune, client_poten, valoare_oferta, ):
        self.nume_proprietar = nume_proprietar
        self.nr_cam = nr_cam
        self.pret_vanzare = pret_vanzare
        self.dimensiune = dimensiune
        self.client_poten = client_poten
        self.valoare_oferta = valoare_oferta
    def get_poze(self, other):
        print(other.URL, other.nr_ord, other.desc)



class Poze:
    def __init__(self, URL, nr_ord, desc):
        self.URL = URL
        self.nr_ord = nr_ord
        self.desc = desc
    def show(self):
        print(self.URL, self.nr_ord, self.desc)

poza = Poze('Imgur.com', 76, 'da')
#poza.show()
