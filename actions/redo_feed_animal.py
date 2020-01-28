import random

from animals import RiverDolphin
from animals import GoldDustDayGecko
from animals import HawaiianHappyfaceSpider
from animals import NeneGoose
from animals import Opeapea
from animals import Ulae
from animals import Kikakapu
from animals import Pueo

from utilities import clear_screen

def redo_feed_animal(arboretum):
    clear_screen()
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

    # find biomes already created and list for user to choose
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
    # ensure user selects valid biome to look in for animals
    clear_screen()
    try:
        biome_type = select_dict[int(choice) -1]
    except (KeyError, ValueError, IndexError):
        input("Invalid input.  Return to main menu")
        return
    # list biome types available to be selected
    for index, biome in enumerate(arboretum.biomes[biome_type]):
        print(f'{index + 1}. {biome.name}')

    print(f'Which {biome_type[:-1]} do you want to feed animals?')
    choice = input("> ")
    clear_screen()
    # ensure valid selection number
    if not choice.isdigit() or int(choice) <= 0:
        input("Invalid input")
        return
    
    try:
        this_biome = arboretum.biomes[biome_type][int(choice) - 1]
    except (KeyError, ValueError, IndexError):
        input("Invalid input.  Return to main menu")
        return
    #print showing whether animals is empty or not
    # print(f'test {arboretum.biomes[biome_type][int(choice) - 1].animals}')
    if len(arboretum.biomes[biome_type][int(choice) - 1].animals) > 0:
        for index, animal in enumerate(this_biome.animals):
            print(f'{index + 1}. {animal.species}')

    else:
        input("You have no animals to feed in this biome.  Please purchase some at the gift shop located on the main menu.")
        return

    print(f'Which animal would you like to feed?')
    choice = input("> ")
    clear_screen()

    if not choice.isdigit() or int(choice) <= 0:
        input("Invalid input")
        return

    fed_animal = ""
    try:
        fed_animal = this_biome.animals[int(choice) -1]

    except (KeyError, ValueError, IndexError):
        input("Invalid input.  Return to main menu")
        return

    # calling food menu
    for index, diet in enumerate(animal.diet):
        print(f'{index + 1}. {diet}')

    food_choice = input("Pick a meal >")

    clear_screen()

    if not food_choice.isdigit() or int(food_choice) <= 0:
        input("Invalid input")
        return

    try:
        selected_meal = animal.diet[int(food_choice) - 1]
    except (KeyError, ValueError, IndexError):
        input("Invalid input.  Return to main menu")
        return
    
    for x in range(1):
        random_value = random.randint(1,20)
 
    if random_value >= 4:
        print(fed_animal.new_feed(selected_meal))
    else:
        print(fed_animal.no_thank_you(selected_meal))
    input('\n\nPress any key to return to the main menu...')

    

 