def init():
    global registries
    global memory
    global variables
    global expressions
    global output
    global next_empty_p_iterator

    registries = {
        'a': {'val_name': None, 'number': 0, 'free': True},
        'b': {'val_name': None, 'number': 0, 'free': True},
        'c': {'val_name': None, 'number': 0, 'free': True},
        'd': {'val_name': None, 'number': 0, 'free': True},
        'e': {'val_name': None, 'number': 0, 'free': True},
        'f': {'val_name': None, 'number': 0, 'free': True},
        'g': {'val_name': None, 'number': 0, 'free': True},
        'h': {'val_name': None, 'number': 0, 'free': True},
        }

    memory = {}
    variables = []
    expressions = []
    output = ""
    next_empty_p_iterator = 0