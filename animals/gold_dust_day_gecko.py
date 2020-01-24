from animals import Animal
from interfaces import IForest

class GoldDustDayGecko(Animal, IForest):
    def __init__(self):
        Animal.__init__(self, "Gold Dust Day Gecko")
        IForest.__init__(self)