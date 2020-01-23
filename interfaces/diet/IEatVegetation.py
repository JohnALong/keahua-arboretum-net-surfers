

class IEatVegetation:
    def __init__(self):
        try:
            self.diet += [ "Trout", "Mackarel", "Salmon", "Sardine" ] 
        except AttributeError:
            self.diet = ["Trout", "Mackarel", "Salmon", "Sardine" ]