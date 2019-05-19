from Organizm import Organizm


class Roslina(Organizm):
    def __init__(self, swiat, gat, poz=None, plik=None):
        super().__init__(swiat, gat, poz, plik)
        self._szansa_rozmnozenia = 0.2

    def akcja(self):
        if self._wiek > 1:
            if self.sproboj_sie_rozmnozyc():
                self._rozmnoz_sie()
        self._wiek += 1
        return True

    def kolizja(self, other_org):
        self.umrzyj()

        # TODO narracja smierci
        return True
