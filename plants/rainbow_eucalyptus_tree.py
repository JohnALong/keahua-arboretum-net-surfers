from .plant import Plant
from interfaces.lives_in import IForest

class Rainbow_Eucalyptus_Tree(Plant, IForest):

    def _init_(self):
        Plant.__init__(self, "Rainbow Eucalyptus Tree", "Full", 8, "Low", season)
        IForest.__init__(self)