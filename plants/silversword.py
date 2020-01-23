from .plant import Plant
from interfaces.lives_in import IGrassland

class Silversword(Plant, IGrassland):

    def _init_(self):
        Plant.__init__(self, "Silversword", "Shade", 22, "High", season)
        IGrassland.__init__(self)