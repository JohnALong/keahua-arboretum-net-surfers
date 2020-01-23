from animals import Animal
from interfaces import Identifiable

class Ulae(Animal, Identifiable):
    def __init__(self):
        Animal.__init__(self, "'Ulae'")
        Identifiable.__init__(self)