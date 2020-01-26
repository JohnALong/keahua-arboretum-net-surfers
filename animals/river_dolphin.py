from animals import Animal
from interfaces import IRiver
from interfaces import ICoastline
from interfaces import IEatFish

class RiverDolphin(Animal, IRiver, ICoastline, IEatFish):

    def __init__(self):
        Animal.__init__(self, "River dolphin")
        IRiver.__init__(self)
        ICoastline.__init__(self)
        IEatFish.__init__(self)

    @property
    def prey(self):
        return self.__prey

    def feed(self, prey):
        if prey in self.__prey:
            print(f'The dolphin ate {prey} for a meal')
        else:
            print(f'The dolphin rejects the {prey}')


    def __str__(self):
        return f'Dolphin {self.id}. Eeee EeeEEeeeeEE!'
