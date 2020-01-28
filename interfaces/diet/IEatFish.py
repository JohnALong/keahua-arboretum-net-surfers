

class IEatFish:
    def __init__(self):
        try:
            self.diet += ["trout", "mackarel", "salmon", "sardines"]
        except AttributeError:
            self.diet = ["trout", "mackarel", "salmon", "sardines"]
