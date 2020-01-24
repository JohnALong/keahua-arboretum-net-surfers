
def build_facility_report(arboretum):
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
                print (biome, "Id: {}")
                #check if there are any animals in a specific biome
                if len(biome.animals) > 0:
                    print("Animals: ")
                    #loop through an individual biome's animals
                    for animal in biome.animals:
                        print(animal.name, f"Id: {animal.id}")
                #check if there are any plants in a specific biome
                if len(biome.plants) > 0:
                    print("Plants: ")
                    for plant in biome.plants:
                        print(plant.name, f"Id: {plant.id}")
            print("-----------------")
 
    input("\n\nPress any key to continue...")
 