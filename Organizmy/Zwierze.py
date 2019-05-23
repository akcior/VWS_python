from Organizm import Organizm
from Punkt import Punkt
import random
from Organizmy.Roslina import Roslina


class Zwierze(Organizm):
    def __init__(self, s, gat, poz=None, plik=None):
        super().__init__(s, gat, poz, plik)
        if poz !=None:
            self._szansa_ucieczki = 0
        elif plik != None:
            self._szansa_ucieczki = float(plik.readline())

    def akcja(self):
        self._wiek += 1
        if self._zyje:
            for i in range(self._zasieg):
                if not self._zrob_ruch():
                    break
        if not self._zyje:
            self.umrzyj()
            return False
        return True

    def _zrob_ruch(self):
        kier = self._znajdz_kier_do_ruchu()
        if kier == Punkt(0, 0):
            return False
        kier.translacja(self.get_pozycja.x, self.get_pozycja.y)
        if self._swiat.miesci_sie_w_planszy(kier):
            o = self._swiat.get_organizm_na_pozycji(kier)
            if o == None:
                self._pozycja = kier.get_lokacja
                return True
            else:
                if self.kolizja(o):
                    self._pozycja = kier.get_lokacja
                    return True
        return False

    def _znajdz_kier_do_ruchu(self):
        k = []
        for i in range(-1, 2):
            for j in range(-1, 2):
                if self._swiat.miesci_sie_w_planszy(self.get_pozycja + Punkt(i, j)):
                    if i * j == 0 and (i != 0 or j != 0):
                        k.append(Punkt(i, j))
        if len(k) > 0:
            # return k[random.randint(0, len(k))]
            return random.choice(k)
        else:
            return Punkt(0, 0)

    def kolizja(self, other_org):
        if isinstance(other_org, Zwierze):
            # jesli ten sam gatunek, zwierze zostaje na swojej pozycji i rozmnaza sie
            if self._gatunek == other_org.get_gatunek:
                if self._wiek > 5 and other_org.get_wiek > 5:
                    if (self.sproboj_sie_rozmnozyc()):
                        self._rozmnoz_sie()
                    return False
            else:
                if self.silniejszy_od(other_org):
                    if not other_org.zrob_unik():
                        if not other_org.zablokuj_atak(other_org):
                            other_org.umrzyj()
                            self._swiat.narrator.org_umarl_przez_org(other_org, self)
                            return True
                else:
                    self._zyje = False
                    self._swiat.narrator.org_umarl_przez_org(self, other_org)
                    return False
        elif isinstance(other_org, Roslina):
            # kolizja roslin moze zmieniac parametry zwierzecia ktore je zjadlo
            if other_org.kolizja(self):  # jesli kolizja = true -> zwierze przezylo
                return True
            else:
                self._zyje = False
                self._swiat.narrator.org_umarl_przez_org(self, other_org)
                return False
        return False

    def zrob_unik(self):
        if random.random() < self._szansa_ucieczki:
            k = self._swiat.get_losowy_wolny_kier_wokol(self.get_pozycja)
            # jesli p == 0,0 oznacza to ze nie znaleziono wolnego kierunki, organizm wiec nie ma gdzie uciec
            if k == Punkt(0, 0):
                return False
            self._pozycja.translacja(k.x, k.y)
            return True
        return False

    def zapisz(self, plik):
        super().zapisz(plik)
        plik.write(str(self._szansa_ucieczki) + "\n")