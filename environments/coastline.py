from environments import Biome

class Coastline(Biome):
    def __init__(self, name):
        Biome.__init__(self, f"{name} Coastline", 3, 15)