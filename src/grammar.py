import numpy as np

variables = {}
current_identifier = None
output = ""

def p_program(p):
    '''program : VAR declarations BEGIN commands END
            | BEGIN commands END'''
    global output
    output = output + "HALT"
    print(output)


def p_new_int_declaration(p):
    '''declarations : pidentifier'''
    variables[p[1]] = None

def p_new_array_declaration(p):
    '''declarations : pidentifier LEFT_SBRACKET num COLON num RIGHT_SBRACKET'''
    arr_dict =  {"size": p[5]-p[3]+1, "first_index": p[3]}
    variables[p[1]] = arr_dict


def p_declarations(p):
    '''
    declarations : declarations COMMA pidentifier
                 | declarations COMMA pidentifier LEFT_SBRACKET num COLON num RIGHT_SBRACKET
    '''
    print("declarations: ", end = '')
    print(p[1])
    
def p_commands(p):
    '''
    commands     : commands command
                 | command
    '''
    print("commands: ", end = '')
    print(p[0])

def p_assign(p):
    '''
    command      : identifier ASSIGN expression SEMICOLON 
    '''  
    if current_identifier in variables.keys():
        variables[p[1]] = p[3]
        print("przypisano wartość do zmiennej")    
    else:
        print(p[1])

def p_command(p):
    '''
    command      : IF condition THEN commands ELSE commands ENDIF
                 | IF condition THEN commands ENDIF
                 | WHILE condition DO commands ENDWHILE
                 | REPEAT commands UNTIL condition SEMICOLON
                 | FOR pidentifier FROM value TO value DO commands ENDFOR
                 | FOR pidentifier FROM value DOWNTO value DO commands ENDFOR
                 | READ identifier SEMICOLON
                 | WRITE value SEMICOLON
    '''

    print("command: ", end = '')
    print(p[0])
    
def p_expression(p):
    '''
    expression   : value
                 | value PLUS value
                 | value MINUS value
                 | value TIMES value
                 | value DIV value
                 | value MOD value
    '''
    print("expression: ", end = '')
    print(p[0])
    
def p_condition(p):
    '''
    condition    : value EQ value
                 | value NEQ value
                 | value LE value
                 | value GE value
                 | value LEQ value
                 | value GEQ value
    '''
    print("condition: ", end = '')
    print(p[0])
    
def p_value(p):
    '''
    value        : num
                 | identifier
    '''
    print("value: ", end = '')
    print(p[0])
    

def p_identifier(p):
    '''
    identifier   : pidentifier
                 | pidentifier LEFT_SBRACKET pidentifier RIGHT_SBRACKET
                 | pidentifier LEFT_SBRACKET num RIGHT_SBRACKET
    '''
    global current_identifier

    if len(p) == 2:
        current_identifier = p[1]
    

    print("identifier: ", end = '')
    print(p[0])
    
def p_error(p):
    print("eeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeee")
        