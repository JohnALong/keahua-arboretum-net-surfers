from .plant import Plant
from interfaces.lives_in import ISwamp, IGrassland

class Blue_Jade_Vine(Plant, ISwamp, IGrassland):

    def _init_(self, species, season):
        Plant.__init__(self, species, season)
        ISwamp.__init__(self)
        IGrassland.__init__(self)