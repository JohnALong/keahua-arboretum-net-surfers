from animals import Animal
from interfaces import Identifiable

class HawaiianHappyfaceSpider(Animal, Identifiable):
    def __init__(self):
        Animal.__init__(self, "Hawaiian Happy-face Spider")
        Identifiable.__init__(self)