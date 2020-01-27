from animals import Animal
from interfaces import IForest
from interfaces import IMountain
from interfaces import IEatInsects
from interfaces import IEatVegetation

class Opeapea(Animal, IForest, IMountain, IEatInsects, IEatVegetation):
    def __init__(self):
        Animal.__init__(self, "Ope'ape'a")
        IForest.__init__(self)
        IMountain.__init__(self)
        IEatInsects.__init__(self)
        IEatVegetation.__init__(self)