import os
from environments import River
from environments import Grassland
from environments import Coastline
from environments import Forest
from environments import Swamp
from environments import Mountain

from utilities import menu_wrapper
from utilities import clear_screen

@menu_wrapper
def build_menu():
    print("1. Mountain")
    print("2. Swamp")
    print("3. Grassland")
    print("4. Forest")
    print("5. River")
    print("6. Coastline")
    return

def annex_habitat(arboretum):
    clear_screen()

    build_menu()
    choice = input("Choose your habitat > ")
    name = input("What would you like to name it? > ")
    if choice == "1":
        mountain = Mountain(name)
        arboretum.biomes["Mountains"].append(mountain)
    if choice == "2":
        swamp = Swamp(name)
        arboretum.biomes["Swamps"].append(swamp)
    if choice == "3":
        grassland = Grassland(name)
        arboretum.biomes["Grasslands"].append(grassland)
    if choice == "4":
        forest = Forest(name)
        arboretum.biomes["Forests"].append(forest)
    if choice == "5":
        river = River(name)
        arboretum.biomes["Rivers"].append(river)
    if choice == "6":
        coastline = Coastline(name)
        arboretum.biomes["Coastlines"].append(coastline)

    return