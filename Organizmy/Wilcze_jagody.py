from Organizmy.Roslina import Roslina
from Gatunki import Gatunki


class Wilcze_jagody(Roslina):
    def __init__(self, s, p=None, plik=None):
        super().__init__(s, Gatunki.WILCZE_JAGODY, p, plik)
        if p != None:
            self._sila = 99

    def kolizja(self, other_org):
        self.umrzyj()
        self._swiat.narrator.org_umarl_przez_org(self, other_org)
        return False

    def plec(self):
        return "y"
