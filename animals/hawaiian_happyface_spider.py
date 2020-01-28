from animals import Animal
from interfaces import ISwamp
from interfaces import IEatInsects

class HawaiianHappyfaceSpider(Animal, ISwamp, IEatInsects):
    def __init__(self):
        Animal.__init__(self, "Hawaiian Happy-face Spider")
        ISwamp.__init__(self)
        IEatInsects.__init__(self)

    def no_thank_you(self, selected_meal):
        return (f"The {self.species} is watching re-runs of Hawaii 5-0 and can't be bothered with {selected_meal}")