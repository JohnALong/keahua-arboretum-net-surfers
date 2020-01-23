from interfaces import Identifiable


class Plant:

    '''
    Attributes for Plant (all string unless noted):
    species, sunlight, seed_produced (int), insecticide_resistance, season
    '''

    def __init__(self, species, sunlight, seeds_produced, insecticide_resistance, season):

        Identifiable.__init__(self)
        self.species = species
        self.sunlight = sunlight
        self.seeds_produced = seeds_produced
        self.insecticide_resistance = insecticide_resistance
        self.peak_season = season
