import settings
from machine_operations import *

def is_variable_empty(name): #zwraca true jesli do zmiennej nie jest jeszcze przypisana zadna wartosc
    for v in settings.variables:
        if v[0] == name:
            return False
    return True

def return_number(value):
    try:
        return int(value)
    except ValueError:
        return int(get_variables_value_using_name(value))
        

def get_variables_value_using_name(name):
    for v in settings.variables:
        if v[0] == name:
            return v[1]
    return False

def get_register_which_contains_value(name):
    for r in settings.registries:
        if str(settings.registries[r]['value']) == name:
            return r
    return False


def add_to_output(s):
    settings.output = settings.output + "\n" + s

# TODO zoptymalizwoac zwiekszanie
def set_registry_value(registry, value):
    print("aaaaaa")
    print(value)
    value = return_number(value) #zwraca zmienna albo jej wartosc
    print(value)
    add_to_output("RESET " + registry)
    for _ in range(value):
        add_to_output("INC " + registry)


def find_free_registry():
    for r in settings.registries:
        if settings.registries[r]["free"] and r != 'a':
            set_registry_not_free(r)
            return r

def set_registry_free(r):
    settings.registries[r]["free"] = True

def set_registry_not_free(r):
    settings.registries[r]["free"] = False

def get__using_var_name(var_name):
    for r in settings.registries:
        if settings.registries[r]['name'] == var_name:
            return r

def search_place_in_memory_using_name(name):
    for f in settings.variables:
        if name == f[0]:   
            return f[1]

def find_free_memory():
    i = 0
    while True:
        if not i in settings.memory_in_usage:
            return i
        else:
            i = i + 1

def get_stack_top():
    top = settings.variables_stack[-1]
    settings.variables_stack.pop()
    return top

def add_to_output(s):
    settings.output = settings.output + "\n" + s

def get_stack_top():
    top = settings.variables_stack[-1]
    settings.variables_stack.pop()
    return top