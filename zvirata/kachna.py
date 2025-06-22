from zvirata.zvire import Zvire


class Kachna(Zvire):

    def __init__(self, hmotnost, peri):
        super().__init__(hmotnost)
        self._peri = peri

    # Vraci zvuk (podle toho co dane zvire dela - polymorfismus)
    def vrat_zvuk(self):
        return "GAGA U LA LA"
