def init():
    global registries
    global memory_in_usage
    global names
    global values
    global full_variables
    global output
    global next_empty_p_iterator

    registries = {
        'a': {'name': None, 'value': 0, 'free': True},
        'b': {'name': None, 'value': 0, 'free': True},
        'c': {'name': None, 'value': 0, 'free': True},
        'd': {'name': None, 'value': 0, 'free': True},
        'e': {'name': None, 'value': 0, 'free': True},
        'f': {'name': None, 'value': 0, 'free': True},
        'g': {'name': None, 'value': 0, 'free': True},
        'h': {'name': None, 'value': 0, 'free': True},
        }

    memory_in_usage = {}
    names = []
    values = []
    full_variables = []
    output = ""
    next_empty_p_iterator = 0
    