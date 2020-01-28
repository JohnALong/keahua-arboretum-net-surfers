from environments import Biome

class Mountain(Biome):
    def __init__(self, name):
        Biome.__init__(self, f"{name} Mountain", 4, 6)