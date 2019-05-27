from Organizmy.Roslina import Roslina
from Gatunki import Gatunki


class Guarana(Roslina):
    def __init__(self, s, p=None, plik=None):
        super().__init__(s, Gatunki.GUARANA, p, plik)

    def kolizja(self, other_org):
        other_org.add_sila(3)
        self.umrzyj()
        self._swiat.narrator.org_umarl_przez_org(self, other_org)
        return True

    def plec(self):
        return "a"
