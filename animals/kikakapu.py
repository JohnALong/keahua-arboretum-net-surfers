from animals import Animal
from interfaces import ISwamp
from interfaces import IRiver
class Kikakapu(Animal, ISwamp, IRiver):
    def __init__(self):
        Animal.__init__(self, "Kīkākapu")
        ISwamp.__init__(self)
        IRiver.__init__(self)