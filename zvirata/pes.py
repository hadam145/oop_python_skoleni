from zvirata.zvire import Zvire


class Pes(Zvire):

    def __init__(self, hmotnost, obojek):
        super().__init__(hmotnost)
        self._obojek = obojek

    # Vraci zvuk (podle toho co dane zvire dela - polymorfismus)
    def vrat_zvuk(self):
        return "HAAAAAAAAAAAAAAF"

