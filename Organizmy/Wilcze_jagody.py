from Organizmy.Roslina import Roslina
from Gatunki import Gatunki


class Wilcze_jagody(Roslina):
    def __init__(self, s, p):
        super().__init__(s, Gatunki.WILCZE_JAGODY, p)
        self._sila = 99

    def kolizja(self, other_org):
        self.umrzyj()
        return False

    def plec(self):
        return "y"