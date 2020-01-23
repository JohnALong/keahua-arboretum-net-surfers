from animals import Animal
from interfaces import Identifiable

class GoldDustDayGecko(Animal, Identifiable):
    def __init__(self):
        Animal.__init__(self, "Gold Dust Day Gecko")
        Identifiable.__init__(self)