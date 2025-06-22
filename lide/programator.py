from lide.clovek import Clovek

#Trida programator dedi z tridy Clovek
class Programator(Clovek):

    #Konstruktor tridy programator, pridava navic jazyk
    def __init__(self,jmeno,vek, jazyk):
        #Zde se vola konstruktor predka (Clovek)
        super().__init__(jmeno,vek)

        jmeno = "x"

        self._jazyk = jazyk

    def vypis_povolani(self):
        print("Programuju")

    #Metoda pozdrav zdravi uzivatele
    def pozdrav(self, pozdrav = "Hello world"):
        #Nejdrive se vola metoda pozdrav z predka a pote
        #Se prida navic k retezci jazyk
        return super().pozdrav(pozdrav) + f" {self._jazyk}"