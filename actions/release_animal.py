from animals import RiverDolphin
from animals import GoldDustDayGecko
from animals import HawaiianHappyfaceSpider
from animals import NeneGoose
from animals import Opeapea
from animals import Ulae
from animals import Kikakapu
from animals import Pueo

def release_animal(arboretum):
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

    # setup dict and display ONLY biomes that the animal choice can go in based on requirements
    choice_dict = dict()
    for index, habitat in enumerate(animal.habitats):
        print(f'{index + 1}. {habitat}')
        choice_dict[index] = habitat

    # user selects biome type
    print(f'Select a biome type to release the {animal.species} into.')
    choice = input("> ")
    selected_biome = choice_dict[int(choice) - 1]

    # 
    if len(arboretum.biomes[selected_biome]) == 0:
        print(f'No {selected_biome} in your arboretum yet.')
        input("\n\nPress any key to return to main menu...")
        return

    # targets specific previously created biome list in arboretum
    for index, biome in enumerate(arboretum.biomes[selected_biome]):
        print(f'{index + 1}. {biome.name}')

    print(f'Select the specific {selected_biome[:-1]} to release the animal!')
    choice = input("> ")
    new_home = int(choice) - 1

    arboretum.biomes[selected_biome][new_home].animals.append(animal)
    for animal in arboretum.biomes[selected_biome][new_home].animals:
        print(animal.species)
    
    input('Wait...')

