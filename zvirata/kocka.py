from zvirata.zvire import Zvire


class Kocka(Zvire):


    def __init__(self,hmotnost, barva):
        super().__init__(hmotnost)
        self._barva = barva

    # Vraci zvuk (podle toho co dane zvire dela - polymorfismus)
    def vrat_zvuk(self):
        return "MEOWWWWWWWWWWWWWWWWW"