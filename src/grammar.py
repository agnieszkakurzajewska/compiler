import settings
from machine_operations import *

#done
def p_program(p):
    '''program : VAR declarations BEGIN commands END
            | BEGIN commands END'''
    add_to_output("HALT")


def p_new_int_declaration(p):
    '''declarations : pidentifier'''
    add_variable(p[1])

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
    print("d")


def p_assign(p):
    '''
    command      : identifier ASSIGN expression SEMICOLON 
    '''  
    

def p_write(p):
    '''command      : WRITE value SEMICOLON'''
    print("uuuu")

def p_command(p):
    '''
    command      : IF condition THEN commands ELSE commands ENDIF
                 | IF condition THEN commands ENDIF
                 | WHILE condition DO commands ENDWHILE
                 | REPEAT commands UNTIL condition SEMICOLON
                 | FOR pidentifier FROM value TO value DO commands ENDFOR
                 | FOR pidentifier FROM value DOWNTO value DO commands ENDFOR
                 | READ identifier SEMICOLON
    '''    
    print("f")

def p_expression(p):
    '''
    expression   : value
                 | value PLUS value
                 | value MINUS value
                 | value TIMES value
                 | value DIV value
                 | value MOD value
    '''
print("g")
    
    
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
    '''
    value        : num
                 | identifier
    ''' 
    add_expression(p[1])
    print("i")   

def p_identifier(p):
    '''
    identifier   : pidentifier
                 | pidentifier LEFT_SBRACKET pidentifier RIGHT_SBRACKET
                 | pidentifier LEFT_SBRACKET num RIGHT_SBRACKET
    '''
    print("j")   

def p_error(p):
    print("eeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeee")
        