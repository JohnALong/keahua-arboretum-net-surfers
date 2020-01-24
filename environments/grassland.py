from environments import Biome

class Grassland(Biome):
    def __init__(self, name):
        Biome.__init__(self, f"{name} Grassland")