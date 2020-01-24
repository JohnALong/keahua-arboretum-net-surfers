
def build_facility_report(arboretum):
    for biome_list in arboretum.biomes:
        print(biome_list,":")
        for biome in arboretum.biomes[biome_list]:
            print (biome, "Id: {}")
            print("Animals: ")
            for animal in biome.animals:
                print(animal.name, f"Id: {animal.id}")
            print("Plants: ")
            for plant in biome.plants:
                print(plant.name, f"Id: {plant.id}")
            print("-----------------")
 
    input("\n\nPress any key to continue...")
 