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

    os.system('cls' if os.name == 'nt' else 'clear')
    # create dictionary to allow iterable functionality and look for biomes selected animal could live in - if it doesn't exist then there can't be any of that animal

    selected_dict = dict()
    my_count = 0
    habitats_count = 0
    animals_count = 0

    for index, habitat in enumerate(animal.habitats):
        if len(arboretum.biomes[habitat]) == 0:
            continue
        else:
            my_count += 1
            habitats_count += 1
            selected_dict[my_count - 1] = habitat
            print(f'{my_count}. {habitat}')

    if habitats_count == 0:
        input("You must create a biome for that animal to live in first.  Press enter to return to the main menu and add one...")
        return

    


    os.system('cls' if os.name == 'nt' else 'clear')
    # food animal can eat
    for index, diet in enumerate(animal.diet):
        print(f'{index + 1}. {diet}')

    food_choice = input("Pick a meal >")

    os.system('cls' if os.name == 'nt' else 'clear')

    selected_meal = animal.diet[int(food_choice) - 1]
    print(animal.new_feed(selected_meal))
    input('\n\nPress any key to return to main menu...')
