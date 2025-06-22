from zvirata.kachna import Kachna
from zvirata.kocka import Kocka
from zvirata.pes import Pes
from zvirata.zbarveni import Zbarveni
from zvirata.zvire import Zvire

# zviratko = Zvire(10)
kocka = Kocka(15, Zbarveni.MODRE)
lady_gaga = Kachna(70,True)
pes = Pes(2,False)

#Pole zvirat
zvirata = [
    kocka,
    lady_gaga,
    pes,
# zviratko
]

#Vypsani instance do konzole (vola se __str__
for zvire in zvirata:
    print(zvire)
    print("=============")

#Na kazde instanci zavolame vrat.zvuk() (Chova se jinak pro ruzne zvirata)
#A vypis()    ...
for zvire in zvirata:
    print(zvire.vrat_zvuk())
    zvire.vypis()
    print("=============")