from animals import Animal
from interfaces import Identifiable

class Kikakapu(Animal, Identifiable):
    def __init__(self):
        Animal.__init__(self, "Kīkākapu")
        Identifiable.__init__(self)