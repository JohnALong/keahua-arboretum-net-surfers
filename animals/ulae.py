from animals import Animal
from interfaces import ICoastline

class Ulae(Animal, ICoastline):
    def __init__(self):
        Animal.__init__(self, "'Ulae'")
        ICoastline.__init__(self)