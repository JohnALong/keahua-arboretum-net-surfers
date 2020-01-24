

class ISwamp:
    def __init__(self):
        try:
            self.habitats += ["Swamps"]
        except AttributeError:
            self.habitats = ["Swamps"]