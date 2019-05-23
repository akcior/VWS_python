from enum import Enum, auto


class Gatunki(Enum):
    @classmethod
    def list(cls):
        return list(map(lambda c: c.name, cls))

    CZLOWIEK = auto()
    WILK = auto()
    OWCA = auto()
    LIS = auto()
    ZOLW = auto()
    ANTYLOPA = auto()
    TRAWA = auto()
    MLECZ = auto()
    GUARANA = auto()
    WILCZE_JAGODY = auto()
    BARSZCZ_SOSNOWSKIEGO = auto()
