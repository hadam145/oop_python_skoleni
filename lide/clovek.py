#Trida Clovek (predpis objektu)
from abc import ABC, abstractmethod


class Clovek(ABC):

    #Konstruktor, prejima parametry jmeno, vek
    def __init__(self, jmeno, vek):
        self.__jmeno = jmeno
        self._vek = vek

    def get_jmeno(self):
        return self.__jmeno

    def get_vek(self):
        return self.vek

    def set_vek(self,novy_vek):
        if (novy_vek>0):
            self.vek = novy_vek
        else:
            print("Nelze nastavit zaporny vek")

    @abstractmethod
    def vypis_povolani(self):
        pass

    #Metoda pozdrav, prejima parametr pozdrav
    def pozdrav(self, pozdrav = "Hello world"):

        return(f"{pozdrav} jak se mas, "
              f"jsem {self.__jmeno},mam {self._vek} let")

    def __str__(self):
        return f"Jsem {self.__jmeno} a mam {self._vek}"

