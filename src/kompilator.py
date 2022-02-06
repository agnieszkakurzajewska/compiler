from tokenize import triple_quoted
import ply.lex as lex
import ply.yacc as yacc
from grammar import *
from tokens import *


# Regular expression rules for simple tokens


t_pidentifier = r'[_a-z]+'


def t_num(t):
    r'[-]?[0-9]+'
    t.value = int(t.value)    
    return t

def t_newline(t):
    r'\n+'
    t.lexer.lineno += len(t.value)

# A string containing ignored characters (spaces and tabs)
t_ignore  = ' \t'

# Error handling rule
def t_error(t):
    print("Illegal character '%s'" % t.value[0])
    t.lexer.skip(1)

# Build the lexer
lexer = lex.lex()
 
  # Test it out
data = '''
VAR n BEGIN
n ASSIGN 3;
WRITE n;
END
'''

lexer.input(data)
print("\n\n")
# Tokenize 
while True: 
    tok = lexer.token() 
    if not tok: 
        break # Nigdy więcej input 
    print("Typ: ", end = '')
    print(tok.type.ljust(15), end = '')
    print("     | wartosc: ", end = '')
    print(str(tok.value).ljust(10), end = '')
    print("     | numer linii: : ", end = '')
    print(str(tok.lineno).ljust(10), end = '')
    print("     | lexpos: ", end = '')
    print(tok.lexpos)

# if __name__ == '__main__': 
#       lex.runmain()\

parser = yacc.yacc()
parser.parse(data)
 
