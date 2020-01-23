from .plant import Plant
from interfaces.lives_in import IMountain

class Mountain_Apple_Tree(Plant, IMountain):

    def _init_(self):
        Plant.__init__(self, "Mountain Apple Tree", sunlight, seeds_produced, insecticide_resistance, season)
        IMountain.__init__(self)