
def build_facility_report(arboretum):
    for biome_list in arboretum.biomes:
        print(biome_list,":")
        for biome in arboretum.biomes[biome_list]:
            print (biome, ":")
            print("")
            for animal in biome.animals:
                print(animal.name, f"Id: {animal.id}")
 
    input("\n\nPress any key to continue...")
 