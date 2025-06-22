class Nakladak:
    
    #Konstruktor s parametrem nakladak
    def __init__(self,naklad, nosnost):
        self._naklad = naklad
        self._nosnost = nosnost

    def naloz(self, hmotnost):
        """
        Metoda pro nakladani hmotnosti
        :param hmotnost: kolik ma byt nalozeno
        :return: Nalozeni nebo nenalozeni
        """

        if self._naklad + hmotnost <= self._nosnost:
            self._naklad += hmotnost
            print(f"Nalozil jsem {hmotnost} kilogramu")
        else:
            print("Nelze nalozit vic, prekrocil jsi nosnost")


    def vyloz(self,hmotnost):
        if self._naklad - hmotnost >= 0:
            self._naklad -= hmotnost
            print(f"Vylozil jsem {hmotnost} kilogramu")
        else:
            print(f"Nelze vylozit {hmotnost} kilogramu")


    def vypis(self):
        print(f"Aktualne mam nalozeno {self._naklad}"
              f" kilogramu.")