from .Zwierze import Zwierze
from Gatunki import Gatunki


class Owca(Zwierze):
    def __init__(self, s, p):
        super().__init__(s, Gatunki.OWCA, p)
        self._sila = 4
        self._inicjatywa = 4

    @property
    def plec(self):
        return "a"
