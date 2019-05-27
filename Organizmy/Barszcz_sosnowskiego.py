from Organizmy.Roslina import Roslina
from Gatunki import Gatunki


class Barszcz_sosnowskiego(Roslina):
    def __init__(self, s, p=None, plik=None):
        super().__init__(s, Gatunki.BARSZCZ_SOSNOWSKIEGO, p, plik)
        self._sila = 10

    def akcja(self):
        super().akcja()
        self.zabij_wszystkich_wokol(tylko_zwierzeta=True, ex=[Gatunki.CYBER_OWCA])
        return True

    def kolizja(self, other_org):
        self.umrzyj()
        if other_org.get_gatunek == Gatunki.CYBER_OWCA:
            return True
        return False

    def plec(self):
        return ""
