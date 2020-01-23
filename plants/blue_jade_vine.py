from .plant import Plant
from interfaces.lives_in import ISwamp, IGrassland

class Blue_Jade_Vine(Plant, ISwamp, IGrassland):

    def _init_(self):
        Plant.__init__(self, "Blue Jade Vine", sunlight, seeds_produced, insecticide_resistance, season)
        ISwamp.__init__(self)
        IGrassland.__init__(self)