from plants import Silversword
from plants import Rainbow_Eucalyptus_Tree
from plants import Blue_Jade_Vine
from plants import Mountain_Apple_Tree

def add_plant():
    plant = None

    print("1. Mountain Apple Tree")
    print("2. Silversword")
    print("3. Rainbow Eucalyptus Tree")
    print("4. Blue Jade Vine")

    choice = input("Choose plant to cultivate > ")

    if choice == "1":
        plant = Mountain_Apple_Tree()
    if choice == "2":
        plant = Silversword()
    if choice == "3":
        plant = Rainbow_Eucalyptus_Tree()
    if choice == "4":
        plant = Blue_Jade_Vine()
    if choice != "5":
        pass
    
    
    # for index, river in enumerate(arboretum.rivers):
    #     print(f'{index + 1}. River {river.id}')

    # print("Release the animal into which biome?")
    # choice = input("> ")

    # arboretum.rivers[int(choice) - 1].animals.append(animal)


