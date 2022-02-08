import settings
from machine_operations import *
from additional_functions import *


def add_to_output(s):
    settings.output = settings.output + "\n" + s

# TODO zoptymalizwoac zwiekszanie
def set_registry_value(value, registry):
    add_to_output("RESET " + registry)
    print(settings.registries[registry]['value'])
    print("ioioioioio")
    print(value)
    # value = value - act_val
    for _ in range(int(value)):
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

#ok
def search_place_in_memory_using_name(name):
    for f in settings.full_variables:
        if name == f[0]:   
            return f[1]

#ok
def search_name_using_place_in_memory(place):
    for f in settings.full_variables:
        if place == f[1]:   
            return f[0]

#ok
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
