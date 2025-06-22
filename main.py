import copy

from lide.clovek import Clovek

adam = Clovek("Adam",100)

tomas = Clovek("Tomas",20)

tomas = adam

pepa = copy.copy(adam)

print(pepa.pozdrav())

if adam is tomas:
    print("stejne")

