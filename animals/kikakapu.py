from animals import Animal
from interfaces import ISwamp
from interfaces import IRiver
from interfaces import IEatFish
class Kikakapu(Animal, ISwamp, IRiver, IEatFish):
    def __init__(self):
        Animal.__init__(self, "Kīkākapu")
        ISwamp.__init__(self)
        IRiver.__init__(self)
        IEatFish.__init__(self)