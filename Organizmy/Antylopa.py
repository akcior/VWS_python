from .Zwierze import Zwierze
from Gatunki import Gatunki


class Antylopa(Zwierze):
    def __init__(self, s, p=None, plik=None):
        super().__init__(s, Gatunki.ANTYLOPA, p, plik)
        self._sila = 4
        self._inicjatywa = 4
        self._zasieg = 2
        self._szansa_ucieczki = 0.5

    def plec(self):
        return "a"
