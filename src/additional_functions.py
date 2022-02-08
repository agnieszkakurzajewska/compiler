import settings
from machine_operations import *
from registries_functions import *


def add_to_output(s):
    settings.output = settings.output + "\n" + s

def get_stack_top():
    top = settings.variables_stack[-1]
    settings.variables_stack.pop()
    return top

