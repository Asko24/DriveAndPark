# Importy
from random import randint

class Swiat():

    def __init__(self):
        self.lista_miast = []

        self.parametry_swiata = {
            "Chrzanow": 4,
            "Libiaz": 2,
            "Krakau": 4
        }

    def start(self):
        for nazwa_miasta in self.parametry_swiata:
            self.lista_miast.append(Miasto(nazwa_miasta, FabrykaParkingow.stworzenie_parkingow(self.parametry_swiata[nazwa_miasta])))
        print(">> Tworzenie swiata zakonczone")

class Miasto():

    def __init__(self, nazwa_miasta, lista_parkingow):
        self.nazwa_miasta = nazwa_miasta
        self.lista_parkingow = lista_parkingow

        print(f"> Stworzono miasto: {nazwa_miasta}")

    def __str__(self):
        return f'> Dane miasta:\n' \
               f'==== Miasto: {self.nazwa_miasta} ====\n' \
               f'Ilosc Parkingow: {len(self.lista_parkingow)}\n' \
               f'Parkingi: {self.lista_parkingow}\n' \
               f'>'

class Parking():

    def __init__(self, x, y):
        # wymiary parkingu - tablica dwuwymiarowa
        self.x = x
        self.y = y

        # model parkingu
        self.model_parkingu = self.narysuj_parking()

    def stworz_parking(self):
        #deklaracja tablicy dwuwymiarowej
        rysunek = []
        for x in range (0, self.x):
            ret = []
            for y in range (0, self.y):
                ret.append("X")
            rysunek.append(ret)

        #rysowanie
        for row in rysunek:
            print(row)


class MiejsceParkingowe():

    def __init__(self, x, y):
        self.wspolrzedna_x = x
        self.wspolrzedna_y = y
        self.wolne_miejsce = True


class Brama():

    def __init__(self, oplata):
        #oplaty
        self.czy_zaplacono = False
        self.oplata = oplata
        self.skarbona = 0
        self.obecnie_zaplacono = 0

        #status otwarcia
        self.procent_zamkniecia_bramy = 100
        self.stan_bramy = "Zamknieta"

    def otworz_brame(self):
        print(">> Próba otwarcia bramy")

        if self.czy_zaplacono == True:
            while self.procent_zamkniecia_bramy != 0:
                self.procent_zamkniecia_bramy -= 1

            if self.procent_zamkniecia_bramy == 0:
                self.stan_bramy = "Otwarta"
                print(f"Status bramy: {self.stan_bramy}")
                self.zamknij_brame()
        else:
            print("Brama nie zostala oplacona! ")


    def zamknij_brame(self):
        print(">> Zamykanie bramy")

        while (self.procent_zamkniecia_bramy != 100):
            self.procent_zamkniecia_bramy += 1

        if self.procent_zamkniecia_bramy == 100:
            self.stan_bramy = "Zamknieta"
        self.czy_zaplacono = False
        print(f"Status bramy: {self.stan_bramy}")


    def zaplac(self, kwota):
        self.obecnie_zaplacono += kwota
        if self.obecnie_zaplacono >= self.oplata:
            self.czy_zaplacono = True
            print("Zaplacono za brame")
            self.skarbona += kwota
            if self.obecnie_zaplacono > self.oplata:
                self.skarbona -= self.obecnie_zaplacono - kwota
                print (f">>> wydajemy reszte - {self.obecnie_zaplacono - self.oplata} zl")
            self.otworz_brame()
            self.obecnie_zaplacono = 0
        else:
            print(f">>> kurwa malo!!! zaplacono: {self.obecnie_zaplacono}, do zaplaty:  {self.oplata - self.obecnie_zaplacono} ")


class DuzyParking(Parking):

    def __init__(self):
        self.x = randint(12, 15)
        self.y = randint(12, 15)

class SredniParking(Parking):

    def __init__(self):
        self.x = randint(9, 12)
        self.y = randint(9, 12)

class MalyParking(Parking):

    def __init__(self):
        self.x = randint(6, 9)
        self.y = randint(6, 9)

class FabrykaParkingow():

    @staticmethod
    def stworz_parking(typ_parkingu):
        try:
            if typ_parkingu == "DuzyParking":
                return DuzyParking()
            if typ_parkingu == "SredniParking":
                return SredniParking()
            if typ_parkingu == "MalyParking":
                return MalyParking()
            raise AssertionError("Zly typ parkingu")
        except AssertionError as _e:
            print(_e)

    @staticmethod
    def stworzenie_parkingow(ilosc_miast):
        gotowy_zestaw = []
        for cykl in range(ilosc_miast):
            zestaw_parkingow = []

            PARKING = FabrykaParkingow.stworz_parking("MalyParking")
            zestaw_parkingow.append(PARKING)

            PARKING = FabrykaParkingow.stworz_parking("SredniParking")
            zestaw_parkingow.append(PARKING)

            PARKING = FabrykaParkingow.stworz_parking("DuzyParking")
            zestaw_parkingow.append(PARKING)

            gotowy_zestaw.append(zestaw_parkingow)

        return gotowy_zestaw