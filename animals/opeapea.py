from animals import Animal
from interfaces import IForest
from interfaces import IMountain

class Opeapea(Animal, IForest, IMountain):
    def __init__(self):
        Animal.__init__(self, "Ope'ape'a")
        IForest.__init__(self)
        IMountain.__init__(self)