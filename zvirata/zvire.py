from abc import abstractmethod, ABC


class Zvire(ABC):

    def __init__(self, hmotnost):
        self._hmotnost = hmotnost

    @property
    def leta(self):
        return self._hmotnost<9

    def nakrm(self, jidlo):
        self._hmotnost += jidlo

    #Vraci zvuk ( prazdny retezec)
    @abstractmethod
    def vrat_zvuk(self):
        pass

    #Magicka metoda pro vypis instance do konzole (prevod na text)
    #Vypisuje typ tridy podle instance
    def __str__(self):
        return f"{type(self).__name__} s hmotnosti {self._hmotnost}"



    def vypis(self):
        print(f"{type(self).__name__} leta: {self.leta}")