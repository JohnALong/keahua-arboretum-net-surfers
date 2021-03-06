from animals import RiverDolphin
from animals import GoldDustDayGecko
from animals import HawaiianHappyfaceSpider
from animals import NeneGoose
from animals import Opeapea
from animals import Ulae
from animals import Kikakapu
from animals import Pueo
import os

from utilities import clear_screen
from utilities import menu_wrapper

@menu_wrapper
def show_biome_animals(biome):

    print(f'{biome.name} Animals')
    print('-------------')
    for animal in biome.animals:
        print(animal.species, f"Id: ({str(animal.id)[:8]})")
    return

def check_for_biomes(arboretum):
    biomes_present = False
    for biome in arboretum.biomes:
        if len(arboretum.biomes[biome]) > 0:
            biomes_present = True

    if not biomes_present:
        input('No biomes created. Press any key to return to main menu to add one.')
    
    return biomes_present

@menu_wrapper
def build_menu():
    print('1. Gold Dust Day Gecko')
    print('2. River Dolphin')
    print('3. Nene Goose')
    print('4. Kīkākapu')
    # print('4. Kikakapu')
    print("5. Pueo")
    print("6. 'Ulae")
    print("7. Ope'ape'a")
    print("8. Happy-Face Spider")
    print('\nEnter "Q" to return to Main Menu.')
    return

@menu_wrapper
def build_biome_menu(arboretum, biome_dict, biome_type):

    # targets specific previously created biome list in arboretum
        # dictionary to store the user choice options ONLY if they have space remaining
    actual_count = 0 # container to hold the count
    for index, biome in enumerate(arboretum.biomes[biome_type]):
        num_current_animals = len(biome.animals)
        if num_current_animals == biome.max_animals: # skip this biome if it's already FULL
            continue
        else:             # add this BIOME to the available choices in biome_dict
            actual_count += 1  # this helps avoid a menu starting at '2' if a previous one was skipped
            biome_dict[actual_count - 1] = biome  # this still saves the biome to a zero-indexed dict
            print(f'{actual_count}. {biome.name} [{num_current_animals} animal(s), {biome.max_animals - num_current_animals} remaining capacity]')

    return biome_dict

@menu_wrapper
def build_species_biome_option_menu(arboretum, animal, choice_dict):
    actual_count = 0
    for _, habitat in enumerate(animal.habitats):
        if len(arboretum.biomes[habitat]) == 0:
            continue
        else:
            actual_count += 1
            choice_dict[actual_count - 1] = habitat
            print(f'{actual_count}. {habitat}')
    return choice_dict

def release_animal(arboretum):
    clear_screen()

    biomes_exist = check_for_biomes(arboretum)
    if not biomes_exist:
        return

    animal = None
    build_menu()

    choice = input("Choose animal to release > ")

    if choice == "1":
        animal = GoldDustDayGecko()

    elif choice == "2":
        animal = RiverDolphin()

    elif choice == "3":
        animal = NeneGoose()

    elif choice == "4":
        animal = Kikakapu()

    elif choice == "5":
        animal = Pueo()

    elif choice == "6":
        animal = Ulae()

    elif choice == "7":
        animal = Opeapea()

    elif choice == "8":
        animal = HawaiianHappyfaceSpider()

    elif choice.upper() == "Q":
        return

    else:
        input('Invalid input. Return to main menu.')
        return
                
    clear_screen()
    # setup dict and display ONLY biomes that the animal choice can go in based on requirements
    choice_dict = dict()

    build_species_biome_option_menu(arboretum, animal, choice_dict)

    # user selects biome type
    if not choice_dict:
        input('No biomes created that this animal can live in.\nPress any key and [Enter] to return to main menu to add one.')
        return

    print(f'Select a biome type to release the {animal.species} into.')
    choice = input("> ")

    # check for valid input choice and return to releas_animal menu if not
    try:
        biome_type = choice_dict[int(choice) - 1]
    except (KeyError, ValueError):
        input("Invalid input. Return to main menu.")
        # release_animal(arboretum)
        return

    # if valid choice, clear screen and proceed with selecting a biome
    clear_screen()

    biome_dict = dict()
    build_biome_menu(arboretum, biome_dict, biome_type)
    # print(biome_dict)
     # if ALL biomes of this type full, return to main menu after notification
    if not biome_dict:
        print(f'All biomes of this type are at max animal capacity.\nAnnex a new {biome_type[:-1]} habitat from the main menu.')
        os.system('say All biomes of this type are at max capacity' if os.name != 'nt' else '')
        input(' >> ')
        return

    print(f'Select the specific {biome_type[:-1]} to release the animal!')
    choice = input("> ")

    try:
        new_home = biome_dict[int(choice) - 1] # this gets the input choice and converts back to zero-indexed choice
    except (KeyError, ValueError, TypeError):
        input("Invalid input. Return to main menu.")
        # release_animal(arboretum)
        return
        
    if len(new_home.animals) < new_home.max_animals:
        new_home.animals.append(animal)
        os.system(f'say you just added a {animal.species} to your {new_home.name}' if os.name != 'nt' else '')
    else:
        print('No space for this animal. Press any key to show all the animals in this biome.')
        os.system(f'say no space for this animal' if os.name != 'nt' else '')
        input(' >> ')

    clear_screen()
    show_biome_animals(new_home)
    input('\nPress any key to return to main menu >>')

    return