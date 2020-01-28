from plants import Silversword
from plants import Rainbow_Eucalyptus_Tree
from plants import Blue_Jade_Vine
from plants import Mountain_Apple_Tree
from utilities import clear_screen

#Set max populations for biomes
max_plant_pops = {"Mountains": 4, "Grasslands": 15, "Rivers": 6, "Forests": 32, "Swamps": 12, "Coastlines": 3}

#Function to add plant to biome
def add_plant(arboretum):
    clear_screen()

    plant = None

    print("1. Mountain Apple Tree")
    print("2. Silversword")
    print("3. Rainbow Eucalyptus Tree")
    print("4. Blue Jade Vine")
    print()
    plant_choice = input("Choose plant to cultivate > ")

    if plant_choice == "1":
        plant = Mountain_Apple_Tree()
    elif plant_choice == "2":
        plant = Silversword()
    elif plant_choice == "3":
        plant = Rainbow_Eucalyptus_Tree()
    elif plant_choice == "4":
        plant = Blue_Jade_Vine()
    else:
        print("No plant chosen. Press any key to return to main menu.")
        input()
        return

    clear_screen()
    #Loop over available biome types for selected plant
    for index, habitat in enumerate(plant.habitats):
        print(f"{index + 1}. {habitat}")

    print()
    habitat_choice = input("Choose your habitat type > ")

    #Set reference to chosen habitat
    try:
        chosen_habitat = plant.habitats[int(habitat_choice) - 1]
    except (IndexError, ValueError):
        input("Invalid input. Returning to main.")
        return

    #Print statement if no biomes of that type exist
    if len(arboretum.biomes[chosen_habitat]) == 0:
        print("No biomes of that type exist. Press any key to return to main menu.")
        input()
        return

    clear_screen()

    #Loop thru biomes of selected type unless all biomes are at max population
    open_biomes = False
    num_biomes = 0
    biome_loop_counter = 0
    biome_loops = len(arboretum.biomes[chosen_habitat])
    bad_choices = ["bad choices"]

    for index, biome in enumerate(arboretum.biomes[chosen_habitat]):

        biome_loop_counter += 1

        if len(biome.plants) < biome.max_plants:
            open_biomes = True
            num_biomes += 1
            print(f"{num_biomes}. {biome.name} ({len(biome.plants)}) plant(s), {biome.max_plants - len(biome.plants)} remaining capacity.")
        if len(biome.plants) >= biome.max_plants:
            num_biomes += 1
            bad_choices.append(num_biomes)
            print(f"{num_biomes}. THIS BIOME UNAVAILABLE. PLEASE DO NOT PRESS CORRESPONDING NUMBER BUTTON.")

            

    if open_biomes == False and biome_loop_counter == biome_loops:
        print()
        print("All biomes of that type are at maximum population. Press any key to return to main menu.")
        input()
        return

    print()
    biome_choice = input("Choose your biome > ")

    
    if int(biome_choice) in bad_choices:
        input("Told you not to press the button. Now you gotta go to the main menu lol.")
        return

    #Add plant to selected biome
    try:
        arboretum.biomes[chosen_habitat][int(biome_choice) - 1].plants.append(plant)
    except (IndexError, ValueError):
        input("Invalid input. Returning to main.")
        return
        
    clear_screen()
    print(f"{plant.species} has been added to {arboretum.biomes[chosen_habitat][int(biome_choice) - 1].name}. Press any key to return to main menu.")
    input()
