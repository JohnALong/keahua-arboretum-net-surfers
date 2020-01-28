import os
from utilities import clear_screen

def print_animals_and_plants(biome):
    if len(biome.animals) > 0:
        print("Animals: ")
                    #loop through an individual biome's animals
        for animal in biome.animals:
            print(animal.species, f"Id: ({str(animal.id)[:8]})")
                #check if there are any plants in a specific biome
    if len(biome.plants) > 0:
            print("Plants: ")
            for plant in biome.plants:
                print(plant.species, f"Id: ({str(plant.id)[:8]})")


def build_full_report(arboretum):
    print("Keahua Arboretum:")
    print("-----------------")
    print("-----------------")
    #loop through the different types of biomes
    for biome_list in arboretum.biomes:
        #check whether each type of biome has any actually biomes in the arboretum
        if len(arboretum.biomes[biome_list]) > 0:
            print(biome_list,":")
            #loop through a list of biomes of a distinct type
            for biome in arboretum.biomes[biome_list]:
                print (biome, f"Id: [{str(biome.id)[:8]}]")
                #check if there are any animals in a specific biome
                print_animals_and_plants(biome)
                print("-----------")
            print("-------------------------------")
    os.system('say here is your report')
    input("\n\nPress enter to return to main menu....")
    return


def build_single_report(arboretum):
    index_dict = dict()
    for biome_type in arboretum.biomes:
        if len(arboretum.biomes[biome_type]) > 0:
            print(f"({biome_type[:1]}) {biome_type}")
            index_plus_one = 1
            for index, biome in enumerate(arboretum.biomes[biome_type]):
                print(f"{index_plus_one}. {biome}")
                index_dict[f"{biome_type[:1]}{index_plus_one}"] = [biome_type, index]
    print("Q. Exit")
    choice = input("Enter the letter and number corresponding to your choice in this format: LetterNumber > ")
    exit_possible = choice.upper()
    if exit_possible == "Q":
        return
    try:
        letter_choice = choice[:1].upper()
        number_choice = choice[1:2]
        uppercase_choice = f"{letter_choice}{number_choice}"
        index_info = index_dict[uppercase_choice]
        biome = arboretum.biomes[index_info[0]][index_info[1]]
    except KeyError:
        print("Invalid Entry")
        clear_screen()
        build_single_report(arboretum)
        return
    print("Single Biome Report")
    print(f"--------------------")
    print(f"Name: {biome.name}")
    print(f"-----------------------------")
    print_animals_and_plants(biome)
    print(f"-----------------------------")
    input("press enter to return to the main menu")
    return
    


def build_facility_report(arboretum):
    clear_screen()
    print("Would you like a full report, or a single biome report?")
    print("1. Full")
    print("2. Single")
    print("Q. Exit")

    choice = input(" >>  ")
    exit_possible = choice.upper()

    if choice == "1":
        build_full_report(arboretum)
    
    elif choice == "2":
        build_single_report(arboretum)

    elif exit_possible == "Q":
        return

    else:
        clear_screen()
        build_facility_report(arboretum)