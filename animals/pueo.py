from animals import Animal
from interfaces import IGrassland
from interfaces import IForest
from interfaces import IEatRodents

class Pueo(Animal, IGrassland, IForest, IEatRodents):
    def __init__(self):
        Animal.__init__(self, "Pueo")
        IGrassland.__init__(self)
        IForest.__init__(self)
        IEatRodents.__init__(self)