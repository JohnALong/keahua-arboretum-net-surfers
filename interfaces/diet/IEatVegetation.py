

class IEatVegetation:
    def __init__(self):
        try:
            self.diet += ["grass", "oranges", "bamboo", "apples"]
        except AttributeError:
            self.diet = ["grass", "oranges", "bamboo", "apples"]
