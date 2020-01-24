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
    print('4. Kīkākapu')
    print("5. Pueo")
    print("6. 'Ulae")
    print("7. Ope'ape'a")
    print("8. Happy-Face Spider")

    choice = input("Choose animal to release > ")

    if choice == "1":
        animal = GoldDustDayGecko()

    if choice == "2":
        animal = RiverDolphin()

    if choice == "3":
        animal = NeneGoose()

    if choice == "4":
        animal = Kikakapu()

    if choice == "5":
        animal = Pueo()

    if choice == "6":
        animal = Ulae()

    if choice == "7":
        animal = Opeapea()

    if choice == "8":
        animal = HawaiianHappyfaceSpider()

    os.system('cls' if os.name == 'nt' else 'clear')
    # setup dict and display ONLY biomes that the animal choice can go in based on requirements
    choice_dict = dict()
    actual_count = 0
    habitats_count = 0
    for index, habitat in enumerate(animal.habitats):
        if len(arboretum.biomes[habitat]) == 0:
            actual_count += index
            continue
        else:
            habitats_count += 1
            choice_dict[actual_count] = habitat
            print(f'{actual_count + 1}. {habitat}')

    # user selects biome type
    if habitats_count == 0:
        input('No biomes created that this animal can live in. Press any key to return to main menu to add one...')
        return

    print(f'Select a biome type to release the {animal.species} into.')
    choice = input("> ")

    os.system('cls' if os.name == 'nt' else 'clear')
    selected_biome = choice_dict[int(choice) - 1]

    # targets specific previously created biome list in arboretum
    for index, biome in enumerate(arboretum.biomes[selected_biome]):
        print(f'{index + 1}. {biome.name}')

    print(f'Select the specific {selected_biome[:-1]} to release the animal!')
    choice = input("> ")

    os.system('cls' if os.name == 'nt' else 'clear')
    new_home = arboretum.biomes[selected_biome][int(choice) - 1]

    new_home.animals.append(animal)
    print(f'{new_home.name} Animals')
    print('-------------')
    for animal in new_home.animals:
        print(animal.species)
    
    input('\n\nPress any key to return to main menu...')