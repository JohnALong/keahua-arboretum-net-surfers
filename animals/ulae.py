from animals import Animal
from interfaces import ICoastline
from interfaces import IEatFish

class Ulae(Animal, ICoastline, IEatFish):
    def __init__(self):
        Animal.__init__(self, "'Ulae'")
        ICoastline.__init__(self)
        IEatFish.__init__(self)