import settings
from machine_operations import *
from registries_functions import *


def add_to_output(s):
    settings.output = settings.output + "\n" + s

def get_stack_top():
    top = settings.variables_stack[-1]
    settings.variables_stack.pop()
    return top

def search_variable_using_name(name):
    for v in settings.variables:
        if v[0] == name:
            return v[1]
    return -1
