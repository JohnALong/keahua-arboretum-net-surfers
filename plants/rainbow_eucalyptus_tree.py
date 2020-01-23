from .plant import Plant
from interfaces.lives_in import IForest

class Rainbow_Eucalyptus_Tree(Plant, IForest):

    def _init_(self, species, season):
        Plant.__init__(self, species, season)
        IForest.__init__(self)