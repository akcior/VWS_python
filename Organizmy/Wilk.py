from .Zwierze import Zwierze
from Gatunki import Gatunki


class Wilk(Zwierze):
    def __init__(self, s, p):
        super().__init__(s, Gatunki.WILK, p)
        self._sila = 9
        self._inicjatywa = 5

    def plec(self):
        return ""
