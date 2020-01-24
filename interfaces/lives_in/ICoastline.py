

class ICoastline:
    def __init__(self):
        try:
            self.habitats += ["Coastlines"]
        except AttributeError:
            self.habitats = ["Coastlines"]