from sys import path_importer_cache
import settings

# Store x oznacza zapisz to co jest w rejestrze a do 
# komórki pamięci o numerze znajdującym się w rejestrze x

# done
def add_to_output(s):
    settings.output = settings.output + "\n" + s

def read_register(value):
    add_to_output("RESET b")
    add_to_output("LOAD b")
    add_to_output("PUT")

def add_variable(variable):
    settings.variables.append(variable)

# TODO zoptymalizwoac zwiekszanie
def set_registry_value(value, registry):
    add_to_output("RESET " + registry)
    for _ in range(value):
        add_to_output("INC " + registry)



#done
def add_expression(exp):
    settings.expressions.append(exp)

#done
def set_memory(value):
    free_r = find_free_registry()
    free_m = find_free_memory()
    set_registry_value(value, "a")
    set_registry_value(free_m, free_r)
    add_to_output("STORE "+str(free_r))

#done
def find_free_memory():
    i = 0
    while True:
        if not i in settings.memory:
            return i
        else:
            i = i + 1

# done
def find_free_registry():
    for r in settings.registries:
        if settings.registries[r]["free"]:
            return r


