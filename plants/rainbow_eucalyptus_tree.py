from .plant import Plant
from interfaces.lives_in import IForest

class Rainbow_Eucalyptus_Tree(Plant, IForest):

    def __init__(self):
        Plant.__init__(self, "Rainbow Eucalyptus Tree", "Full", 8, "Low")
        IForest.__init__(self)