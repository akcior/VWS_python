from Organizm import Organizm


class Roslina(Organizm):
    def akcja(self):
        pass

    def kolizja(self, other_org):
        #TODO narracja smierci
        pass

    def __init__(self,swiat,gat,poz=None,plik=None):
        super().__init__(swiat,gat,poz,plik)
        self._szansa_rozmnozenia = 0.4

