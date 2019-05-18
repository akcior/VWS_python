from Organizm import Organizm


class Roslina(Organizm):
    def __init__(self,swiat,gat,poz=None,plik=None):
        super().__init__(swiat,gat,poz,plik)
        self._szansa_rozmnozenia = 0.4

