from environments import Biome

class Forest(Biome):
    def __init__(self, name):
        Biome.__init__(self, f"{name} Forest", 32, 20)
      