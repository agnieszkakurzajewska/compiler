import settings
from additional_functions import *
from registries_functions import *

#dodac walidowanie redeklaracji
def add_variable_to_stack(name):
    settings.variables_stack.append(name)
    print("dodano: "+name)


def read_input(): #READ x
    var_name = get_stack_top()
    free_m = find_free_memory()
    r = find_free_registry()
    add_to_output("GET")
    set_registry_value(free_m, r)
    settings.variables.append((var_name, free_m))
    add_to_output("STORE "+str(r))
    set_registry_free(r)


#ok
def write_output(): #WRITE
    var_name = get_stack_top()
    memory_place = search_variable_using_name(var_name)
    r = find_free_registry()
    print("aaaa")
    print(memory_place)
    set_registry_value(memory_place, r)
    add_to_output("LOAD "+str(r))
    add_to_output("PUT")
    set_registry_free(r)











