from Punkt import Punkt
from Gatunki import Gatunki
from Organizm import Organizm
import random
import Organizmy
import Narrator


class Swiat:

    def __init__(self, rozmiar=Punkt(1, 1)):
        self._rozmiar = rozmiar
        self._organizmy = []
        self.narrator = Narrator.Narrator()
        self.nowa_gra(rozmiar)
        # self.stworz_organizm(Gatunki.WILK, Punkt(1, 5))
        # self.stworz_organizm(Gatunki.WILK, Punkt(9, 6))
        # self.stworz_organizm(Gatunki.OWCA, Punkt(6, 5))
        # self.stworz_organizm(Gatunki.LIS, Punkt(4, 8))
        # self.stworz_organizm(Gatunki.ZOLW, Punkt(5, 5))
        # self.stworz_organizm(Gatunki.ANTYLOPA, Punkt(3, 8))
        # self.stworz_organizm(Gatunki.MLECZ, Punkt(8, 8))
        # self.stworz_organizm(Gatunki.GUARANA, Punkt(8, 1))
        # self.stworz_organizm(Gatunki.WILCZE_JAGODY, Punkt(5, 1))
        # self.stworz_organizm(Gatunki.BARSZCZ_SOSNOWSKIEGO, Punkt(3, 1))

    def nowa_gra(self, rozmiar_gry):
        self._rozmiar = rozmiar_gry
        self._organizmy.clear()
        for gatunek in Gatunki:
            i = 0
            if gatunek == Gatunki.CZLOWIEK:
                #continue
                i = 1
            while i < 2:
                i += 1
                p = Punkt()
                for j in range(4):
                    p.x = random.randrange(self._rozmiar.x)
                    p.y = random.randrange(self._rozmiar.y)
                    if (self.get_organizm_na_pozycji(p) != None):
                        p.x = -1
                        p.y = -1
                    else:
                        break
                if p.x == -1:
                    continue
                self.stworz_organizm(gatunek, p)

    def nastepna_runda(self):
        self._organizmy.sort(key=lambda o: (o.get_inicjatywa, o.get_wiek), reverse=True)
        i = 0
        while i < len(self._organizmy):
            o = self._organizmy[i]
            if o.get_wiek > 0:
                o.akcja()
            else:
                o.add_wiek(1)

            # jesli organizm wczesniejszy zostal usuniety
            # zapobiega to ominieciu nastepnego organizmu
            if o in self._organizmy:
                i = self._organizmy.index(o)
                i += 1
        self.narrator.opowiadaj()

    def get_czlowiek(self):
        for org in self._organizmy:
            if org.get_gatunek == Gatunki.CZLOWIEK:
                return org
        return None

    def get_organizm_na_pozycji(self, p):
        for org in self._organizmy:
            if org.get_pozycja == p:
                return org
        return None

    def stworz_organizm(self, g, p):
        if self.miesci_sie_w_planszy(p):
            o = self.get_organizm_na_pozycji(p)
            if o != None:
                return False
            nazwa_org = g.name[0] + g.name[1:].lower()
            klasa_org = getattr(Organizmy, nazwa_org)
            self._organizmy.append(klasa_org(self, p))
        else:
            return False

    def usun_organizm(self, org):
        self._organizmy.remove(org)

    def get_wszystkie_organizmy(self):
        return self._organizmy

    def get_wszystkie_org_wokol(self, p):
        orgs = []
        for i in range(-1, 2):
            for j in range(-1, 2):
                if i != 0 or j != 0:
                    k = p.get_lokacja
                    k.translacja(i, j)
                    if self.miesci_sie_w_planszy(k):
                        o = self.get_organizm_na_pozycji(k)
                        if o != None:
                            orgs.append(o)
        return orgs

    def get_losowy_wolny_kier_wokol(self, p):
        kier = []
        for i in range(-1, 2):
            for j in range(-1, 2):
                if i * j == 0:
                    k = p.get_lokacja
                    k.translacja(i, j)
                    if self.miesci_sie_w_planszy(k):
                        o = self.get_organizm_na_pozycji(k)
                        if o == None:
                            kier.append(Punkt(i, j))
        if len(kier) > 0:
            return random.choice(kier)
        else:
            return Punkt(0, 0)

    @property
    def get_rozmiar(self):
        return self._rozmiar

    def zapisz(self, plik):
        # TODO zapis swiata
        pass

    def wczytaj(self, plik):
        # TODO wczytanie swiata
        pass

    def miesci_sie_w_planszy(self, p):
        if isinstance(p, Punkt):
            return p.x >= 0 and p.x < self._rozmiar.x and \
                   p.y >= 0 and p.y < self._rozmiar.y
