from Organizmy.Roslina import Roslina
from Gatunki import Gatunki


class Barszcz_sosnowskiego(Roslina):
    def __init__(self, s, p):
        super().__init__(s,Gatunki.BARSZCZ_SOSNOWSKIEGO, p)
        self._sila = 10

    def akcja(self):
        super().akcja()
        self.zabij_wszystkich_wokol(tylko_zwierzeta=True)
        return True

    def kolizja(self, other_org):
        self.umrzyj()
        return False

    def plec(self):
        return ""