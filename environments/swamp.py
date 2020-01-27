import sys
sys.path.append('../')

from environments import Biome
# from interfaces.habitats import IStagnant



class Swamp(Biome):
    def __init__(self, name):
        Biome.__init__(self, f"{name} Swamp", 12, 8)
      

    def animal_count(self):
        return "This place has a bunch of animals in it"

    def addInhabitant(self, item):
        if not isinstance(item, IStagnant):
            raise TypeError(f"{item} is not of type IStagnant")
        self.inhabitants.append(item)
