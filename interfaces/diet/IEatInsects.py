

class IEatInsects:
    def __init__(self):
        try:
            self.diet += ["grasshoppers", "crickets", "moths"]
        except AttributeError:
            self.diet = ["grasshoppers", "crickets", "moths"]
