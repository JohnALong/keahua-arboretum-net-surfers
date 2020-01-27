from animals import Animal
from interfaces import ISwamp
from interfaces import IEatInsects

class HawaiianHappyfaceSpider(Animal, ISwamp, IEatInsects):
    def __init__(self):
        Animal.__init__(self, "Hawaiian Happy-face Spider")
        ISwamp.__init__(self)
        IEatInsects.__init__(self)