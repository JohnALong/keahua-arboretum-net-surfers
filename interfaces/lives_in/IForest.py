

class IForest:
    def __init__(self):
        try:
            self.habitats += ["Forests"]
        except AttributeError:
            self.habitats = ["Forests"]