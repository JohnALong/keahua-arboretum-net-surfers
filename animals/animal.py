## PURPOSE: Base/super class for that all animal classes inherit from
from interfaces import Identifiable
class Animal:

    def __init__(self, species):
        Identifiable.__init__(self)
        self.species = species
        self.age = 0

    def move(self, propulsion, speed):
        return f"{self. species} moves at {speed} meters/sec by {propulsion}"
