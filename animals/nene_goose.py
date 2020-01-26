from animals import Animal
from interfaces import IGrassland
from interfaces import IEatVegetation

class NeneGoose(Animal, IGrassland, IEatVegetation):
    def __init__(self):
        Animal.__init__(self, "Nene Goose")
        IGrassland.__init__(self)
        IEatVegetation.__init__(self)