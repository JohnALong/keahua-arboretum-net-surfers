import os
from .header import print_header

def clear_screen():
    os.system('cls' if os.name == 'nt' else 'clear')
    print_header()
    return