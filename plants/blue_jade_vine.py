from .plant import Plant
from interfaces.lives_in import ISwamp, IGrassland

class Blue_Jade_Vine(Plant, ISwamp, IGrassland):

    def _init_(self):
        Plant.__init__(self, "Blue Jade Vine", "Partial", 0, "Medium", season)
        ISwamp.__init__(self)
        IGrassland.__init__(self)