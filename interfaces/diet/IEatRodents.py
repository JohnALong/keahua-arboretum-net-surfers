

class IEatRodents:
    def __init__(self):
        try:
            self.diet += ["rats", "mice", "voles"]
        except AttributeError:
            self.diet = ["rats", "mice", "voles"]
