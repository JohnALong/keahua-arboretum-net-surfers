import os

from animals import RiverDolphin
from animals import GoldDustDayGecko
from animals import HawaiianHappyfaceSpider
from animals import NeneGoose
from animals import Opeapea
from animals import Ulae
from animals import Kikakapu
from animals import Pueo

def feed_animal(arboretum):
    os.system('cls' if os.name == 'nt' else 'clear')
    biome_exist = 0
    animal_exist = 0
    for biome in arboretum.biomes:
        if len(arboretum.biomes[biome]) > 0:
            biome_exist += 1

    if biome_exist == 0:
            input("I think you're lost.  This is still the parking lot.  Please return to the main menu and create a biome.")
            return

    for biome in arboretum.biomes[biome]:
        print(biome)
        for animal in biome.animals[animal]:
            if len(biome.animals) > 0:
                animal_exist += 1

    if animal_exist == 0:
        input("You can't feed an imaginary animal.  Please return to the main menu and release some!")
        return

        # for animal in biome.animals:
        #     print(animal.species)

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

    os.system('cls' if os.name == 'nt' else 'clear')

    if animal_eating == "1":
        animal = GoldDustDayGecko()
    if animal_eating == "2":
        animal = RiverDolphin()
    if animal_eating == "3":
        animal = NeneGoose()
    if animal_eating == "4":
        animal = Kikakapu()
    if animal_eating == "5":
        animal = Pueo()
    if animal_eating == "6":
        animal = Ulae()
    if animal_eating == "7":
        animal = Opeapea()
    if animal_eating == "8":
        animal = HawaiianHappyfaceSpider()
    if animal_eating != "9":
        pass

    for index, diet in enumerate(animal.diet):
        print(f'{index + 1}. {diet}')

    food_choice = input("Pick a meal >")

    os.system('cls' if os.name == 'nt' else 'clear')

    selected_meal = animal.diet[int(food_choice) - 1]
    input(animal.new_feed(selected_meal))
    input('\n\nPress any key to return to main menu...')


    # input(f'The {animal.species} had {selected_meal} today.')