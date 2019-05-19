from .Zwierze import Zwierze
from Gatunki import Gatunki
import random


class Zolw(Zwierze):
    def __init__(self, s, p):
        super().__init__(s, Gatunki.ZOLW, p)
        self._sila = 2
        self._inicjatywa = 1

    def akcja(self):
        if random.random() < 0.25:
            return super().akcja()
        else:
            self._wiek += 1
            return True

    def zablokuj_atak(self, other_org):
        if other_org.get_sila < 5:
            return True
        return False

    def plec(self):
        return ""