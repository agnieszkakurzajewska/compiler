class OutputGenerator:

    output = None
    
    def __init__(self):
        global output
        output = ''
    
    def append(string):
        global output
        output = output + "\n" + string
        print("doklejono i teraz output wyglada: " + output)
