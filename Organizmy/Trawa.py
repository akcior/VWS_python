from .Roslina import Roslina
from Gatunki import Gatunki


class Trawa(Roslina):
    def __init__(self, s, p):
        super().__init__(s, Gatunki.TRAWA, p)

    def plec(self):
        return "a"
