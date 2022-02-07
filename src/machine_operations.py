from sys import path_importer_cache
import settings

#ok
def add_to_output(s):
    settings.output = settings.output + "\n" + s

#ok
def read_memory(): #write
    name = settings.names[-1] ##take last var name from stack
    settings.names.pop()
    memory_place = search_place_in_memory_using_name(name)
    r = find_free_registry()
    set_registry_value(memory_place, r)
    add_to_output("LOAD "+str(r))
    add_to_output("PUT")
    set_registry_free(r)

# def read_from_name(name):
#     memory = search_place_in_memory_using_name(name)
#     free_r = find_free_registry()
#     set_registry_value(memory, free_r)
#     add_to_output("LOAD " + free_r)
#     add_to_output("PUT")
#     settings.registries[free_r]["free"] = True

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

# TODO zoptymalizwoac zwiekszanie
def set_registry_value(value, registry):
    add_to_output("RESET " + registry)
    for _ in range(value):
        add_to_output("INC " + registry)

#ok
def add_name(name):
    if name not in settings.names:
        settings.names.append(name)

#ok
def add_value(value):
    if value not in settings.values:
  
        settings.values.append(value)

#ok
def find_free_memory():
    i = 0
    while True:
        if not i in settings.memory_in_usage:
            return i
        else:
            i = i + 1

def set_memory():

    r = find_free_registry()
    free_m = find_free_memory()
    set_registry_value(settings.values[-1], "a")
    set_registry_value(free_m, r)
    add_to_output("STORE "+str(r))
    add_new_full_variable(settings.names[-1], settings.values[-1], free_m)
    settings.values.pop()
    settings.names.pop()
    set_registry_free(r)
#ok
def add_new_full_variable(name, value, free_m):
    settings.full_variables.append((name, value, free_m))

#ok
def find_free_registry():
    for r in settings.registries:
        if settings.registries[r]["free"] and r != 'a':
            return r

def set_registry_free(r):
    settings.registries[r]["free"] = True

def set_registry_not_free(r):
    settings.registries[r]["free"] = False



