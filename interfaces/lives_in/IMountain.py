

class IMountain:
    def __init__(self):
        try:
            self.habitats += ["Mountains"]
        except AttributeError:
            self.habitats = ["Mountains"]