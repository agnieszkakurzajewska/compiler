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
    name = get_stack_top()
    place_in_memory = None
    
    if is_variable_empty(name):
        place_in_memory = search_place_in_memory_using_name(name)
    else:
        print("error")

    r = get_register_which_contains_value(name)
    if r == False:
        r = find_free_registry()
        set_registry_value(r, place_in_memory)
        
    add_to_output("LOAD "+str(r))
    add_to_output("PUT")
    settings.registries[r] = {'value': name, 'free': True}



def assign(): 
    print("qqqqqq")
    # 3 i n
    var_number = get_stack_top()
    var_name =  get_stack_top()
    # print(search_variable_using_name(var_name)) 
    set_or_match_registry_value(var_name) #zapisuje
    # var_name = get_stack_top()
    # set_registry_value("a", var_name)
    # r = find_free_registry()
    # set_or_match_registry_value(r, var_name)
    # add_to_output("STORE "+str(r))
    # set_registry_free(r)

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

def set_or_match_registry_value(var_name): #jesli zmienna juz jest zapisana w pamieci to ja nadpisz, inaczej znajdz wolna pamiec
    memory_place = search_variable_using_name(var_name)
    if memory_place != -1: 
        set_registry_value(find_free_registry(), memory_place)
    else:
        set_registry_value(find_free_registry(), find_free_memory())


        














