from interfaces import Identifiable

class Biome(Identifiable):

    def __init__(self, name):
        self.name = name
        Identifiable.__init__(self)

    def __str__(self):
        return self.name