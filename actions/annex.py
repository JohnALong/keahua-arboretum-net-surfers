import os
from environments import River
from environments import Grassland
from environments import Coastline
from environments import Forest
from environments import Swamp
from environments import Mountain

def annex_habitat(arboretum):
    os.system('cls' if os.name == 'nt' else 'clear')
    print("1. Mountain")
    print("2. Swamp")
    print("3. Grassland")
    print("4. Forest")
    print("5. River")
    print("6. Coastline")
    choice = input("Choose your habitat > ")
    name = input("What would you like to name it? > ")
    if choice == "1":
        mountain = Mountain(name)
        arboretum.biomes["Mountains"].append(mountain)
        os.system(f'say you have annexed {name} Mountain!')
    if choice == "2":
        swamp = Swamp(name)
        arboretum.biomes["Swamps"].append(swamp)
        os.system(f'say you have annexed {name} Swamp!')
    if choice == "3":
        grassland = Grassland(name)
        arboretum.biomes["Grasslands"].append(grassland)
        os.system(f'say you have annexed {name} grassland!')
    if choice == "4":
        forest = Forest(name)
        arboretum.biomes["Forests"].append(forest)
        os.system(f'say you have annexed {name} forest!')
    if choice == "5":
        river = River(name)
        arboretum.biomes["Rivers"].append(river)
        os.system(f'say you have annexed {name} river!')
    if choice == "6":
        coastline = Coastline(name)
        arboretum.biomes["Coastlines"].append(coastline)
        os.system(f'say you have annexed {name} coastline!')
