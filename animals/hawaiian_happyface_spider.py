from animals import Animal
from interfaces import ISwamp

class HawaiianHappyfaceSpider(Animal, ISwamp):
    def __init__(self):
        Animal.__init__(self, "Hawaiian Happy-face Spider")
        ISwamp.__init__(self)