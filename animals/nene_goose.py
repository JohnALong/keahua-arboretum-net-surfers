from animals import Animal
from interfaces import IGrassland

class NeneGoose(Animal, IGrassland):
    def __init__(self):
        Animal.__init__(self, "Nene Goose")
        IGrassland.__init__(self)