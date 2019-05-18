from Punkt import Punkt
from Gatunki import Gatunki
from Organizm import Organizm
import random
from Organizmy import Wilk


class Swiat:

    def __init__(self, rozmiar=Punkt(1, 1)):
        self._rozmiar = rozmiar
        self._organizmy = []
        self.narrator = None
        self._organizmy.append(Wilk.Wilk(self, Punkt(1, 2)))

    def nowa_gra(self, rozmiar_gry):
        self._rozmiar = rozmiar_gry
        self._organizmy.clear()
        for gatunek in Gatunki:
            i = 0
            if gatunek == Gatunki.CZLOWIEK:
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
            i = self._organizmy.index(o)
            i += 1

    def get_organizm_na_pozycji(self, p):
        for org in self._organizmy:
            if org.getPozycja() == p:
                return org
        return None

    def stworz_organizm(self, g, p):
        if self.miesci_sie_w_planszy(p):
            o = self.get_organizm_na_pozycji(p)
            if o != None:
                return False
            # TODO tworzenie organizmu
            # org_konstrukt = getattr()
            # self.organizmy.append(Organizm(self,Gatunki.WILK,Punkt(1,2)))
            org = Organizm(self, Gatunki.WILK, Punkt(1, 2))

        else:
            return False

    def usun_organizm(self, org):
        self._organizmy.remove(org)

    def get_wszystkie_organizmy(self):
        return self._organizmy

    def get_wszystkie_org_wokol(self, p):
        orgs = []
        for i in range(-1, 1):
            for j in range(-1, 1):
                if i != 0 or j != 0:
                    k = p.get_lokacja
                    k.translacja(i, j)
                    if self.miesci_sie_w_planszy(k):
                        o = self.get_organizm_na_pozycji(k)
                        if o != None:
                            self._organizmy.append(o)
        return orgs

    def get_losowy_wolny_kier_wokol(self, p):
        kier = []
        for i in range(-1, 1):
            for j in range(-1, 1):
                if i * j == 0:
                    k = p.get_lokacja
                    k.translacja(i, j)
                    if self.miesci_sie_w_planszy(k):
                        o = self.get_organizm_na_pozycji(k)
                        if o == None:
                            kier.append(Punkt(i, j))
        if len(kier) > 0:
            return kier[random.randint(0, len(kier))]
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
