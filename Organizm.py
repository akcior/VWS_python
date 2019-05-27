# from Organizmy import Roslina
from Punkt import Punkt
from abc import ABC, abstractmethod
from random import *
from Gatunki import Gatunki


class Organizm:
    def __init__(self, swiat, gat, poz=None, plik=None):
        self._swiat = swiat
        self._gatunek = gat
        self._pozycja = Punkt(0, 0)
        self._zyje = True
        if poz != None:
            self._pozycja = poz
            self._wiek = 0
            self._sila = 0
            self._inicjatywa = 0
            self._zasieg = 1
            self._szansa_rozmnozenia = 1
        elif plik != None:
            self._pozycja.x = int(plik.readline())
            self._pozycja.y = int(plik.readline())
            self._wiek = int(plik.readline())
            self._sila = int(plik.readline())
            self._inicjatywa = int(plik.readline())
            self._zasieg = int(plik.readline())
            self._szansa_rozmnozenia = float(plik.readline())

        else:
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
    def kolizja(self, other_org):
        pass

    def sproboj_sie_rozmnozyc(self):
        return random() < self._szansa_rozmnozenia

    def _rozmnoz_sie(self):
        k = self._swiat.get_losowy_wolny_kier_wokol(self.get_pozycja)
        if k != Punkt(0, 0):
            k.translacja(self._pozycja.x, self._pozycja.y)
            self._swiat.stworz_organizm(self._gatunek, k)
            self._swiat.narrator.org_rozmnozyl_sie(self)

    def zablokuj_atak(self, other_org):
        return False

    def silniejszy_od(self, other):
        return self._sila >= other.get_sila

    def zabij_wszystkich_wokol(self, tylko_zwierzeta=False, ex=None):
        from Organizmy import Roslina as ros
        orgs = self._swiat.get_wszystkie_org_wokol(self._pozycja)
        for o in orgs:
            if o.get_gatunek == self._gatunek:
                continue
            if tylko_zwierzeta:
                if isinstance(o, ros.Roslina):
                    continue
            if o.get_gatunek in ex:
                continue
            o.umrzyj()
            self._swiat.narrator.org_umarl_przez_org(o, self)

    def umrzyj(self):
        self._zyje = False
        self._swiat.usun_organizm(self)

    def zapisz(self, plik):
        plik.write(self._gatunek.name + "\n")
        plik.write(str(self._pozycja.x) + "\n")
        plik.write(str(self._pozycja.y) + "\n")
        plik.write(str(self._wiek) + "\n")
        plik.write(str(self._sila) + "\n")
        plik.write(str(self._inicjatywa) + "\n")
        plik.write(str(self._zasieg) + "\n")
        plik.write(str(self._szansa_rozmnozenia) + "\n")

    @property
    @abstractmethod
    def plec(self):
        pass

    def __str__(self):
        return self._gatunek.name[0] + self._gatunek.name[
                                       1:].lower() + " na pozycji:" + str(self._pozycja)
