from interfaces import identifiable

class Plant:

    def __init__(self, species, season):

        Identifiable.__init__(self)
        self.species = species
        self.sunlight = ""
        self.seeds_produced = 0
        self.insecticide_resistance = ""
        self.peak_season = season
