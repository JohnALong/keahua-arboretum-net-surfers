from .plant import Plant
from interfaces.lives_in import IGrassland

class Silversword(Plant, IGrassland):

    def _init_(self):
        Plant.__init__(self, "Silversword", sunlight, seeds_produced, insecticide_resistance, season)
        IGrassland.__init__(self)