from animals import Animal
from interfaces import IGrassland
from interfaces import IForest

class Pueo(Animal, IGrassland, IForest):
    def __init__(self):
        Animal.__init__(self, "Pueo")
        IGrassland.__init__(self)
        IForest.__init__(self)