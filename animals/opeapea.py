from animals import Animal
from interfaces import Identifiable

class Opeapea(Animal, Identifiable):
    def __init__(self):
        Animal.__init__(self, "Ope'ape'a")
        Identifiable.__init__(self)