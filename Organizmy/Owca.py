from .Zwierze import Zwierze
from Gatunki import Gatunki


class Owca(Zwierze):
    def __init__(self, s, p=None, plik=None):
        super().__init__(s, Gatunki.OWCA, p, plik)
        if p != None:
            self._sila = 4
            self._inicjatywa = 4

    def plec(self):
        return "a"
