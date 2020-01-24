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
        biome_options = []

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

    for index, habitat in enumerate(animal.habitats):
        print(f'{index + 1}. {habitat}')

    
    # for index, river in enumerate(arboretum.rivers):
    #     print(f'{index + 1}. River {river.id}')

    print(f'Select a biome type to release the {animal.species} into.')
    choice = input("> ")

    for index, biome in enumerate(arboretum.biomes[choice]):
        if len(arboretum.biomes[choice]) == 0:
            print(f'No {choice} in your arboretum yet.')
            input("\n\nPress any key to return to main menu...")
            return
        print(f'{index + 1}. {biome.name}')

    print(f'Select the specific {choice[:-1]} to release the animal!')
    new_home = input("> ")

    arboretum.biomes[choice][new_home].append(animal)

    # arboretum.rivers[int(choice) - 1].animals.append(animal)


