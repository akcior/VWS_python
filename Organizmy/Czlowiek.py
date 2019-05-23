from Organizmy.Zwierze import Zwierze
from Gatunki import Gatunki
from Punkt import Punkt


class Czlowiek(Zwierze):
    def __init__(self, s, poz=None, plik=None):
        super().__init__(s, Gatunki.CZLOWIEK, poz, plik)
        if poz != None:
            self._nastepny_ruch = Punkt(0, 0)
            self._sila = 5
            self._inicjatywa = 4
            self._moc_czas_trwania = 5
            self._moc_czas_odnowy = 5
            self._moc_pozostaly_czas_trwania = 0
            self._moc_pozostaly_czas_odnowy = 0
        elif plik != None:
            self._nastepny_ruch = Punkt()
            self._nastepny_ruch.x = int(plik.readline())
            self._nastepny_ruch.y = int(plik.readline())
            self._moc_czas_trwania = int(plik.readline())
            self._moc_czas_odnowy = int(plik.readline())
            self._moc_pozostaly_czas_trwania = int(plik.readline())
            self._moc_pozostaly_czas_odnowy = int(plik.readline())
        else:
            return NotImplemented

    def akcja(self):
        if (super().akcja()):
            if self._moc_pozostaly_czas_trwania > 0:
                self.zabij_wszystkich_wokol(tylko_zwierzeta=False)
                self._moc_pozostaly_czas_trwania -= 1
                self._swiat.narrator.mocy_pozostalo("Calopalenie", self._moc_pozostaly_czas_trwania)
                if self._moc_pozostaly_czas_trwania == 0:
                    self._moc_pozostaly_czas_odnowy = self._moc_czas_odnowy
            elif self._moc_pozostaly_czas_odnowy > 0:
                self._moc_pozostaly_czas_odnowy -= 1
                if self._moc_pozostaly_czas_odnowy > 0:
                    self._swiat.narrator.moc_odnowi_sie_za("Calopalenie", self._moc_pozostaly_czas_odnowy)
                    pass
                else:
                    self._swiat.narrator.moc_odnowiona("Calopalenie")

                    pass
            return True
        return False

    def aktywuj_moc(self):
        if self._moc_pozostaly_czas_odnowy > 0 or self._moc_pozostaly_czas_trwania > 0:
            return False
        self._moc_pozostaly_czas_trwania = self._moc_czas_trwania
        self._swiat.narrator.org_uzyl_mocy(self, "Calopalenie")
        return True

    def _znajdz_kier_do_ruchu(self):
        p = self._nastepny_ruch.get_lokacja
        # wyzerowanie nastepnego ruchu
        self._nastepny_ruch = Punkt(0, 0)
        return p

    @property
    def get_moc_pozostaly_czas_trwania(self):
        return self._moc_pozostaly_czas_trwania

    @property
    def get_moc_pozostaly_czas_odnowy(self):
        return self._moc_pozostaly_czas_odnowy

    @property
    def get_nastepny_ruch(self):
        return self._nastepny_ruch

    def plec(self):
        return ""

    def set_nastepny_ruch(self, nast_ruch):
        self._nastepny_ruch = nast_ruch

    def zapisz(self, plik):
        super().zapisz(plik)
        plik.write(str(self._nastepny_ruch.x) + "\n")
        plik.write(str(self._nastepny_ruch.y) + "\n")
        plik.write(str(self._moc_czas_trwania) + "\n")
        plik.write(str(self._moc_czas_odnowy) + "\n")
        plik.write(str(self._moc_pozostaly_czas_trwania) + "\n")
        plik.write(str(self._moc_pozostaly_czas_odnowy) + "\n")
