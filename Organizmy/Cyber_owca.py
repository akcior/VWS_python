from .Zwierze import Zwierze
from Gatunki import Gatunki
from Punkt import Punkt


class Cyber_owca(Zwierze):

    def __init__(self, s, p=None, plik=None):
        super().__init__(s, Gatunki.CYBER_OWCA, p, plik)
        if p != None:
            self._sila = 11
            self._inicjatywa = 4

    def plec(self):
        return "a"

    def _znajdz_kier_do_ruchu(self):
        import random
        najblizszy_cel = self._swiat.get_najblizszy_org_z_gatunku(self.get_pozycja, Gatunki.BARSZCZ_SOSNOWSKIEGO)
        k = []

        if najblizszy_cel != Punkt(0, 0):
            if najblizszy_cel.x - self.get_pozycja.x > 0:
                k.append(Punkt(1, 0))
            elif najblizszy_cel.x - self.get_pozycja.x < 0:
                k.append(Punkt(-1, 0))

            if najblizszy_cel.y - self.get_pozycja.y > 0:
                k.append(Punkt(0, 1))
            elif najblizszy_cel.y - self.get_pozycja.y < 0:
                k.append(Punkt(0, -1))

            return random.choice(k)
        else:
            return super()._znajdz_kier_do_ruchu()
