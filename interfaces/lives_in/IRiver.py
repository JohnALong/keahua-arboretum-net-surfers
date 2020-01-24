

class IRiver:
    def __init__(self):
        try:
            self.habitats += ["Rivers"]
        except AttributeError:
            self.habitats = ["Rivers"]