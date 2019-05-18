from Organizm import Organizm
from Gatunki import Gatunki
class Wilk(Organizm):
    def __init__(self,s,p):
        super().__init__(s,Gatunki.WILK,p)
