from interfaces import Identifiable
from interfaces import IContainsAnimals
from interfaces import IContainsPlants

class Biome(IContainsAnimals, IContainsPlants, Identifiable):

    def __init__(self, name, max_plants, max_animals):
        Identifiable.__init__(self)
        IContainsAnimals.__init__(self)
        IContainsPlants.__init__(self)
        self.name = name
        self.max_plants = max_plants
        self.max_animals = max_animals
        

    def __str__(self):
        return f"{self.name}"