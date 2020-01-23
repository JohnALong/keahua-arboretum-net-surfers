from .plant import Plant
from interfaces.lives_in import IGrassland

class Silversword(Plant, IGrassland):

    def _init_(self, species, season):
        Plant.__init__(self, species, season)
        IGrassland.__init__(self)