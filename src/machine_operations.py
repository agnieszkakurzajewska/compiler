from sys import path_importer_cache
import settings

# Store x oznacza zapisz to co jest w rejestrze a do 
# komórki pamięci o numerze znajdującym się w rejestrze x

def add_to_output(s):
    settings.output = settings.output + "\n" + s

def read_register():
    val = settings.values[-1]
    
    add_to_output("RESET b")
    add_to_output("LOAD b")
    add_to_output("PUT")

def read_from_name(name):
    memory = search_var_name_in_memory(name)
    free_r = find_free_registry()
    set_registry_value(memory, free_r)
    add_to_output("LOAD " + free_r)
    add_to_output("PUT")

def search_var_name_in_memory(name):
    for f in settings.full_variables:
        if name == settings.full_variables[f][0]:   
            return settings.full_variables[f][1]

def search_var_value_in_memory(value):
    for f in settings.full_variables:
        if value == settings.full_variables[f][1]:   
            return settings.full_variables[f][0]

# TODO zoptymalizwoac zwiekszanie
def set_registry_value(value, registry):
    add_to_output("RESET " + registry)
    for _ in range(value):
        add_to_output("INC " + registry)

def add_name(name):
    if name not in settings.names:
        settings.names.append(name)

def add_value(value):
    settings.values.append(value)

def find_free_memory():
    i = 0
    while True:
        if not i in settings.memory:
            return i
        else:
            i = i + 1

def set_memory():
    free_r = find_free_registry()
    free_m = find_free_memory()
    set_registry_value(settings.values[-1], "a")
    set_registry_value(free_m, free_r)
    add_to_output("STORE "+str(free_r))
    settings.full_variables.append((settings.names[-1], free_m))
    settings.values.pop()
    settings.names.pop()

def find_free_registry():
    for r in settings.registries:
        if settings.registries[r]["free"] and r != 'a':
            return r


