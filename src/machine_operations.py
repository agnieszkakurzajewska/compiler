from re import A

memory_iterator = 0

def read_register(output):

    output = add_to_output(output, "RESET b")
    output = add_to_output(output, "LOAD b")
    return add_to_output(output, "PUT")


# TODO zoptymalizwoac zwiekszanie
def set_register(output, value):
    # Store x oznacza zapisz to co jest w rejestrze a do 
    # komórki pamięci o numerze znajdującym się w rejestrze x
 
    output = add_to_output(output, "RESET a")
    output = add_to_output(output, "RESET b")

    for a in range(value):
        output = add_to_output(output, "INC a")

    for b in range(memory_iterator):
        output = add_to_output(output, "INC b")

    output = add_to_output(output, "STORE b")

    return output

def add_to_output(output, s):
    return output + "\n" + s
