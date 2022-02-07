import settings
from machine_operations import *

#done
def p_program(p):
    '''program : VAR declarations BEGIN commands END
            | BEGIN commands END'''
    add_to_output("HALT")


def p_new_int_declaration(p):
    '''declarations : pidentifier'''
    print("dodaje zmienna")
    add_name(p[1])

def p_new_array_declaration(p):
    '''declarations : pidentifier LEFT_SBRACKET num COLON num RIGHT_SBRACKET'''
    arr_dict =  {"size": p[5]-p[3]+1, "first_index": p[3]}
    print("b")


def p_declarations(p):
    '''
    declarations : declarations COMMA pidentifier
                 | declarations COMMA pidentifier LEFT_SBRACKET num COLON num RIGHT_SBRACKET
    '''
    print("c")

def p_commands(p):
    '''
    commands     : commands command
                 | command
    '''


def p_assign(p):
    '''
    command      : identifier ASSIGN expression SEMICOLON 
    '''  
    print("przypisuje")
    set_memory()

def p_write(p):
    '''command      : WRITE value SEMICOLON'''
    read_memory()

def p_command(p):
    '''
    command      : IF condition THEN commands ELSE commands ENDIF
                 | IF condition THEN commands ENDIF
                 | WHILE condition DO commands ENDWHILE
                 | REPEAT commands UNTIL condition SEMICOLON
                 | FOR pidentifier FROM value TO value DO commands ENDFOR
                 | FOR pidentifier FROM value DOWNTO value DO commands ENDFOR
    '''    
    print("f")

def p_read(p):
    '''    command      : READ identifier SEMICOLON'''

def p_expression(p):
    '''
    expression   : value
                 | value PLUS value
                 | value MINUS value
                 | value TIMES value
                 | value DIV value
                 | value MOD value
    '''
    
    
def p_condition(p):
    '''
    condition    : value EQ value
                 | value NEQ value
                 | value LE value
                 | value GE value
                 | value LEQ value
                 | value GEQ value
    '''
    print("h")   


def p_value(p):
    '''value        : identifier'''

def p_num(p):
    '''value        : num'''
    print("dodaję numer")
    add_value(p[1])

def p_identifier(p):
    '''
    identifier   : pidentifier
                 | pidentifier LEFT_SBRACKET pidentifier RIGHT_SBRACKET
                 | pidentifier LEFT_SBRACKET num RIGHT_SBRACKET
    '''
    if len(p) == 5:
        var = str(p[1])+"]"+str(p[3])+"]"
    else:
        var = p[1]
    print("dodaję nazwe zmiennej")
    print(add_name(var))   

def p_error(p):
    print("eeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeee")
        