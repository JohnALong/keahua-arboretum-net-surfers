class Arboretum:
    def __init__(self, name, address):
        self.name = name
        self.address = address
        self.biomes = dict()
        self.biomes["Rivers"] = []
        self.biomes["Grasslands"] = []
        self.biomes["Mountains"] = []
        self.biomes["Coastlines"] = []
        self.biomes["Forests"] = []
        self.biomes["Swamps"] = []
