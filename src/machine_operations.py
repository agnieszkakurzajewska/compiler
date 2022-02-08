from numpy import ma, var
import settings
from registries_functions import *

# Store x oznacza zapisz to co jest w rejestrze a do komórki
#  pamięci o numerze znajdującym się w rejestrze x
# znajduje wolny r i wolna pamiec

#dodac walidowanie redeklaracji
def add_variable_to_stack(name):
    settings.variables_stack.append(name)


#READ x
def read_input(): 
    print("xxxxxxxxx")

    r = find_free_registry()
    name = get_stack_top() 

    if is_variable_empty(name):
        place_in_memory = find_free_memory()
    else:
        place_in_memory = search_place_in_memory_using_name(name)

    add_to_output("GET")
    set_registry_value(r, place_in_memory)
    add_to_output("STORE "+str(r))

    settings.variables.append((name, place_in_memory, True))
    settings.registries[r] = {'value': name, 'free': True}


#WRITE
def write_output(): 
    print("wwwwwwwwww")

    name = get_stack_top()
    place_in_memory = None

    if is_variable_empty(name):
        place_in_memory = find_free_memory()
        print("byla pusta")
    else:
        place_in_memory = search_place_in_memory_using_name(name)
        print("nie byla pusta")

    r = get_register_which_contains_value(name)
    if r == False:
        print("zodyn nimo")
        r = find_free_registry()

    set_registry_value(r, place_in_memory)
    add_to_output("LOAD "+str(r))
    add_to_output("PUT")
    settings.registries[r] = {'value': name, 'free': True}

#ASSIGN
def assign(): 
    print("qqqqqq")
    var_number = get_stack_top()
    var_name =  get_stack_top()
    print("Pod " + str(var_name) + " podpisuję liczbę " + str(var_number))
    if is_variable_empty(var_name):
        place_in_memory = find_free_memory()
        print("byla pusta")
    else:
        place_in_memory = search_place_in_memory_using_name(var_name)
        print("nie byla pusta")

    r = get_register_which_contains_value(var_name)
    if r == False:
        r = find_free_registry()

    set_registry_value(r, place_in_memory)
    set_registry_value("a", var_number)

    add_to_output("STORE "+str(r))
    settings.registries[r] = {'value': var_name, 'free': True}
    settings.variables.append((var_name, place_in_memory, True))


def add():
    var1 = get_stack_top()
    # var2 = get_stack_top()
    # var1 = return_number(var1)
    # var2 = return_number(var2)
    # add_to_output("RESET " + "a")
    # set_registry_value("a", var1)
    # free_m = find_free_memory()
    # r1 = find_free_registry()
    # set_registry_value(r, free_m)


    # print(var1)
    # print(var2)

        














