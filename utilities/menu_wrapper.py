def menu_wrapper(func):
    def wrapped_menu(*args, **kwargs):
        print()
        print("---===***===---"*4)
        func(*args, **kwargs)
        print("---===***===---"*4)
    
    return wrapped_menu