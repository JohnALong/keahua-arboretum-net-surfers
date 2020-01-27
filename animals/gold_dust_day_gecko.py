from animals import Animal
from interfaces import IForest
from interfaces import IEatInsects

class GoldDustDayGecko(Animal, IForest, IEatInsects):
    def __init__(self):
        Animal.__init__(self, "Gold Dust Day Gecko")
        IForest.__init__(self)
        IEatInsects.__init__(self)