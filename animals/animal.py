## PURPOSE: Base/super class for that all animal classes inherit from
from interfaces import Identifiable
class Animal:

    def __init__(self, species):
        Identifiable.__init__(self)
        self.species = species
        self.age = 0

    def move(self, propulsion, speed):
        return f"{self. species} moves at {speed} meters/sec by {propulsion}"

    #feed animal function
    def new_feed(self, selected_meal):
        if selected_meal in self.diet:
            return (f'The {self.species} ate {selected_meal} for lunch')
        else:
            return (f'The {self.species} rejects the {selected_meal}')

    def no_thank_you(self, selected_meal):
        return (f'The {self.species} rejects the {selected_meal}')