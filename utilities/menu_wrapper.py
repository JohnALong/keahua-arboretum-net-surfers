def menu_wrapper(func):
    def wrapped_menu(*args, **kwargs):
        print()
        print("---===***===---"*4)
        func()
        print("---===***===---"*4)
    
    return wrapped_menu