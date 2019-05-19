from Punkt import Punkt
from .Zwierze import Zwierze
from Gatunki import Gatunki


class Lis(Zwierze):
    def __init__(self, s, p):
        super().__init__(s, Gatunki.LIS, p)
        self._sila = 3
        self._inicjatywa = 7

    def _znajdz_kier_do_ruchu(self):
        for i in range(4):
            k = super()._znajdz_kier_do_ruchu()
            o = self._swiat.get_organizm_na_pozycji(self.get_pozycja + k)
            if o == None:
                return k
            else:
                if self.silniejszy_od(o) or o.get_gatunek == self.get_gatunek:
                    return k
        return Punkt(0, 0)

    def plec(self):
        return ""