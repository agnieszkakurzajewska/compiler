def init():
    global registries
    global variables
    global memory_in_usage
    global variables_stack
    global output

    registries = {
        'a': {'value': 0, 'free': True},
        'b': {'value': 0, 'free': True},
        'c': {'value': 0, 'free': True},
        'd': {'value': 0, 'free': True},
        'e': {'value': 0, 'free': True},
        'f': {'value': 0, 'free': True},
        'g': {'value': 0, 'free': True},
        'h': {'value': 0, 'free': True},
        }
    
    variables = [] #pairs: (name, memory_place)
    memory_in_usage = {}
    variables_stack = []
    output = ""    