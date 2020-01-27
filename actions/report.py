
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
                print("-----------")
            print("-------------------------------")

    input("\n\nPress any key to continue...")

def build_single_report(arboretum):
    index_dict = dict()
    for biome_type in arboretum.biomes:
        if len(arboretum.biomes[biome_type]) > 0:
            print(f"({biome_type[:1]}) {biome_type}")
            index_plus_one = 1
            for biome in arboretum.biomes[biome_type]:
                print(f"{index_plus_one}. {biome}")
                index_dict[f"{biome_type[:1]-{index_plus}}"] = [biome_type, biome]
    choice = input("Enter the letter and number corresponding to your choice.")


def build_facility_report(arboretum):

    print("Would you like a full report, or a single biome report?")
    print("1. Full")
    print("2. Single")

    choice = input(" >>  ")

    if choice == "1":
        build_full_report(arboretum)
    
    elif choice == "2":
        build_single_report(arboretum)

    else:
        build_facility_report(arboretum)