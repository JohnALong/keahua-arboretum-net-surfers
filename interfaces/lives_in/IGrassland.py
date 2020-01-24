

class IGrassland:
    def __init__(self):
        try:
            self.habitats += ["Grasslands"]
        except AttributeError:
            self.habitats = ["Grasslands"]