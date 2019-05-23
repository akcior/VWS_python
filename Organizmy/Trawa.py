from .Roslina import Roslina
from Gatunki import Gatunki


class Trawa(Roslina):
    def __init__(self, s, p=None, plik=None):
        super().__init__(s, Gatunki.TRAWA, p, plik)

    def plec(self):
        return "a"
