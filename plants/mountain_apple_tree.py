from .plant import Plant
from interfaces.lives_in import IMountain

class Mountain_Apple_Tree(Plant, IMountain):

    def _init_(self, species, season):
        Plant.__init__(self, species, season)
        IMountain.__init__(self)