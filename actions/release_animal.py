import os

from animals import RiverDolphin
from animals import GoldDustDayGecko
from animals import HawaiianHappyfaceSpider
from animals import NeneGoose
from animals import Opeapea
from animals import Ulae
from animals import Kikakapu
from animals import Pueo

def release_animal(arboretum):
    os.system('cls' if os.name == 'nt' else 'clear')
    current_biome_count = 0
    for biome in arboretum.biomes:
        if len(arboretum.biomes[biome]) > 0:
            current_biome_count += 1

    if current_biome_count == 0:
        input('No biomes created. Press any key to return to main menu to add one...')
        return

    animal = None

    print('1. Gold Dust Day Gecko')
    print('2. River Dolphin')
    print('3. Nene Goose')
    #print('4. Kīkākapu)
    print('4. Kikakapu')
    print("5. Pueo")
    print("6. 'Ulae")
    print("7. Ope'ape'a")
    print("8. Happy-Face Spider")
    print('\nEnter "Q" to return to Main Menu.')

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
        print(animal)

    elif choice == "8":
        animal = HawaiianHappyfaceSpider()

    elif choice.upper() != "Q":
        input('Invalid input... Press any key to try again.')
        release_animal(arboretum)
    else:
        return
                

    os.system('cls' if os.name == 'nt' else 'clear')
    # setup dict and display ONLY biomes that the animal choice can go in based on requirements
    choice_dict = dict()
    actual_count = 0
    habitats_count = 0
    for index, habitat in enumerate(animal.habitats):
        if len(arboretum.biomes[habitat]) == 0:
            continue
        else:
            actual_count += 1
            habitats_count += 1
            choice_dict[actual_count - 1] = habitat
            print(f'{actual_count}. {habitat}')

    # user selects biome type
    if habitats_count == 0:
        input('No biomes created that this animal can live in.\nPress any key and [Enter] to return to main menu to add one...')
        return

    print(f'Select a biome type to release the {animal.species} into.')
    choice = input("> ")

    # check for valid input choice and return to releas_animal menu if not
    try:
        biome_type = choice_dict[int(choice) - 1]
    except (KeyError, ValueError):
        input("Invalid input. Please try again")
        release_animal(arboretum)

    # if valid choice, clear screen and proceed with selecting a biome
    os.system('cls' if os.name == 'nt' else 'clear')

    # targets specific previously created biome list in arboretum
    for index, biome in enumerate(arboretum.biomes[biome_type]):
        print(f'{index + 1}. {biome.name}')

    print(f'Select the specific {biome_type[:-1]} to release the animal!')
    choice = input("> ")

    new_home = ""
    try:
        new_home = arboretum.biomes[biome_type][int(choice) - 1]
    except (IndexError, ValueError):
        input("Invalid input. Please try again")
        release_animal(arboretum)
        
    new_home.animals.append(animal)

    os.system('cls' if os.name == 'nt' else 'clear')
    
    print(f'{new_home.name} Animals')
    print('-------------')
    for animal in new_home.animals:
        print(animal.species)
    
    input('\n\nPress any key to return to main menu...')