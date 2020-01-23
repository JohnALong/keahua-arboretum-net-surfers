import sys
sys.path.append('../')

from environments.biomes import Biome
from interfaces.habitats import IStagnant

from environments.environment import Environment
# TODO need to create environment parent class
from interfaces.habitats import IStagnant
# TODO need to create IStagnant among other interfaces for habitats
# from animals.


class Swamp(IContainsAnimals, IContainsPlants, Biome):

    def __init__(self, name):
      self.name = name
      self.inhabitants = []

    def animal_count(self):
        return "This place has a bunch of animals in it"

    def addInhabitant(self, item):
        if not isinstance(item, IStagnant):
            raise TypeError(f"{item} is not of type IStagnant")
        self.inhabitants.append(item)
