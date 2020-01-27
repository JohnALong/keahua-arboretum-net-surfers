import os

from animals import RiverDolphin
from animals import GoldDustDayGecko
from animals import HawaiianHappyfaceSpider
from animals import NeneGoose
from animals import Opeapea
from animals import Ulae
from animals import Kikakapu
from animals import Pueo

def redo_feed_animal(arboretum):
    os.system('cls' if os.name == 'nt' else 'clear')
    biome_exist = 0
    animal_exist = 0
    # check for existing biomes
    for biome in arboretum.biomes:
        if len(arboretum.biomes[biome]) > 0:
            biome_exist += 1
            # check for existing animals
            for this in arboretum.biomes[biome]:
                for animal in this.animals:
                    if len(this.animals) > 0:
                        animal_exist += 1

    if biome_exist == 0:
        input("I think you're lost.  This is still the parking lot.  Please return to the main menu and create a biome.")
        return
                    
    if animal_exist == 0:
        input("You can't feed an imaginary animal.  Please return to the main menu and release some!")
        return

    # looping through existing biomes and animals
    for biome_list in arboretum.biomes:
        if len(arboretum.biomes[biome_list]) > 0:
            print(biome_list)

            for biome in arboretum.biomes[biome_list]:
                if len(biome.animals) > 0:
                    print("test test")

                    for animal in biome.animals:
                        print(animal.species)

    # animal_eating = input("Who gets to eat today?\n>")

    

    # selected_dict = dict()
    # my_count = 0
    # habitats_count = 0
    # animals_count = 0

    # for index, habitat in enumerate(animal.habitats):
    #     if len(arboretum.biomes[habitat]) == 0:
    #         continue
    #     else:
    #         my_count += 1
    #         habitats_count += 1
    #         selected_dict[my_count - 1] = habitat
    #         print(f'{my_count}. {habitat} and {animal.species}')
    #         input("steve")

    # if habitats_count == 0:
    #     input("You must create a biome for that animal to live in first.  Press enter to return to the main menu and add one...")
    #     return
    
    animal = None

    print("1. Gold Dust Day Gecko")
    print("2. River Dolphin")
    print("3. Nene Goose")
    print("4. Kīkākapu")
    print("5. Pueo")
    print("6. 'Ulae")
    print("7. Ope'ape'a")
    print("8. Happy-Face Spider")

    animal_eating = input("Who gets to eat today?\n>")