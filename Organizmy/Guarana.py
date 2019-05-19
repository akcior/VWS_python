from Organizmy.Roslina import Roslina
from Gatunki import Gatunki


class Guarana(Roslina):
    def __init__(self, s, p):
        super().__init__(s, Gatunki.GUARANA, p)

    def kolizja(self, other_org):
        other_org.add_sila(3)
        self.umrzyj()
        #TODO narracja smierci
        return True

    def plec(self):
        return "a"