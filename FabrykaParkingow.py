# Importy
from Classes import Parking
from random import randint

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