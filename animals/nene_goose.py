from animals import Animal
from interfaces import Identifiable

class NeneGoose(Animal, Identifiable):
    def __init__(self):
        Animal.__init__(self, "Nene Goose")
        Identifiable.__init__(self)