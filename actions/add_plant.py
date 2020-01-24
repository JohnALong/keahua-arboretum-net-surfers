from plants import Silversword
from plants import Rainbow_Eucalyptus_Tree
from plants import Blue_Jade_Vine
from plants import Mountain_Apple_Tree


def add_plant(arboretum):
    plant = None

    print("1. Mountain Apple Tree")
    print("2. Silversword")
    print("3. Rainbow Eucalyptus Tree")
    print("4. Blue Jade Vine")

    plant_choice = input("Choose plant to cultivate > ")

    if plant_choice == "1":
        plant = Mountain_Apple_Tree()
    if plant_choice == "2":
        plant = Silversword()
    if plant_choice == "3":
        plant = Rainbow_Eucalyptus_Tree()
    if plant_choice == "4":
        plant = Blue_Jade_Vine()
    if plant_choice != "5":
        pass

    for index, habitat in enumerate(plant.habitats):
        print(f"{index + 1}. {habitat}")

    habitat_choice = input("Choose you habitat type > ")

    chosen_habitat = plant.habitats[int(habitat_choice) - 1]

    if len(arboretum.biomes[chosen_habitat]) == 0:
        print("No biomes of that type exist. Return to main menu.")
        input()
        return

    for index, biome in enumerate(arboretum.biomes[chosen_habitat]):

        print(f"{index + 1}. {biome.name}")

    # for index, biome in enumerate(arboretum.biomes[chosen_habitat]):

    #     print(f"{index + 1 }. {biome.name}")

    biome_choice = input("Choose your biome > ")

    arboretum.biomes[chosen_habitat][int(biome_choice - 1)].plants.append(plant)

    # for index, river in enumerate(arboretum.rivers):
    #     print(f'{index + 1}. River {river.id}')

    # print("Release the animal into which biome?")
    # choice = input("> ")

    # arboretum.rivers[int(choice) - 1].animals.append(animal)
