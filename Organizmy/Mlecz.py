from .Roslina import Roslina
from Gatunki import Gatunki


class Mlecz(Roslina):
    def __init__(self, s, p=None, plik=None):
        super().__init__(s, Gatunki.MLECZ, p, plik)

    def akcja(self):
        for i in range(3):
            super().akcja()
            if i < 2:
                self._wiek -= 1
        return True

    def plec(self):
        return ""
