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
    select_dict = dict()
    real_count = 0
    habitats_count = 0


    for index, biome_list in enumerate(arboretum.biomes):
        if len(arboretum.biomes[biome_list]) == 0:
            continue
        else:
            real_count += 1
            habitats_count += 1
            select_dict[real_count - 1] = biome_list
            print(f'{real_count}. {biome_list}')

    print(f'Select a biome to see animals to feed')
    choice = input("> ")

    try:
        biome_type = select_dict[int(choice) -1]
    except (KeyError, ValueError):
        input("Invalid input.  Return to main menu")
        return

    for index, biome in enumerate(arboretum.biomes[biome_type]):
        print(f'{index + 1}. {biome.name}')

    print(f'Which {biome_type[:-1]} do you want to feed animals?')
    choice = input("> ")

    try:
        this_biome = arboretum.biomes[select_dict[int(choice) -1]][int(choice) - 1]
        print({this_biome})
    except (KeyError, ValueError):
        input("Invalid input.  Return to main menu")
        return

    for index, animal in enumerate(this_biome.animals):
        print(f'{index + 1}. {animal.species}')

    print(f'Which {animal.species} would you like to feed?')
    choice = input("> ")

    fed_animal = ""
    fed_animal = this_biome.animals[int(choice) -1]

    # calling food menu
    for index, diet in enumerate(animal.diet):
        print(f'{index + 1}. {diet}')

    food_choice = input("Pick a meal >")

    os.system('cls' if os.name == 'nt' else 'clear')

    selected_meal = animal.diet[int(food_choice) - 1]

    print(fed_animal.new_feed(selected_meal))
    input('\n\nPress any key to return to the main menu...')

    

 