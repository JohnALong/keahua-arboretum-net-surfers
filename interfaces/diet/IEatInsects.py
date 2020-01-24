

class IEatInsects:
    def __init__(self):
        try:
            self.diet += ["grasshopper", "cricket", "moth"]
        except AttributeError:
            self.diet = ["grasshopper", "cricket", "moth"]
