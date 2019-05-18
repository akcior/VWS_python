#from Organizmy import Roslina
from Punkt import Punkt
from abc import ABC, abstractmethod
from random import *
from Gatunki import Gatunki


class Organizm:
    def __init__(self, swiat, gat, poz=None, plik=None):
        self._swiat = swiat
        self._gatunek = gat
        # self._pozycja = Punkt(0, 0)
        if poz != None:
            self._pozycja = poz
            self._zyje = True
            self._wiek = 0
            self._inicjatywa = 0
            self._sila = 0
            self._zasieg = 1
            self._szansa_rozmnozenia = 1
        else:
            # TODO wczytywanie organizmu z pliku
            return NotImplemented

    @property
    def zyje(self):
        return self._zyje

    @property
    def get_pozycja(self):
        return self._pozycja.get_lokacja

    @property
    def get_sila(self):
        return self._sila

    def add_sila(self, ilosc):
        self._sila += ilosc

    @property
    def get_inicjatywa(self):
        return self._inicjatywa

    @property
    def get_gatunek(self):
        return self._gatunek

    @property
    def get_wiek(self):
        return self._wiek

    def add_wiek(self, w):
        self._wiek += w

    @abstractmethod
    def akcja(self):
        pass

    @abstractmethod
    def kolizja(self, other_organizm):
        pass

    def sproboj_sie_rozmnozyc(self):
        return random() < self._szansa_rozmnozenia

    def rozmnoz_sie(self):
        # TODO rozmnazanie
        pass

    def zablokuj_atak(self):
        return False

    def silniejszy_od(self, other):
        return self._sila >= other.get_sila

    def zabij_wszystkich_wokol(self, tylko_zwierzeta):
        from Organizmy import Roslina
        orgs = self._swiat.get_wszystkie_org_wokol(self._pozycja)
        for o in orgs:
            if o.get_gatunek == self._gatunek:
                continue
            if tylko_zwierzeta:
                if isinstance(o, Roslina):
                    continue
            o.umrzyj()
            # TODO narracja o smierci

    def umrzyj(self):
        self._zyje = False
        # TODO usuniecie organizmu ze swiata
        pass

    def zapisz(self,zap):
        #TODO zapis do pliku
        pass
