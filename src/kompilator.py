import ply.lex as lex
import ply.yacc as yacc
from grammar import *

tokens = (
'ASSIGN',
'BEGIN',
'COLON',
'COMMA',
'COMMENT',
'DIVIDE',
'ELSE',
'END',
'ENDIF',
'IF',
'LEFT_SBRACKET',
'LPAREN',
'MINUS',
'PLUS',
'RIGHT_SBRACKET',
'RPAREN',
'SEMICOLON',
'THEN',
'TIMES',
'VAR',
'WRITE',
'pidentifier',
'num',
)

# Regular expression rules for simple tokens
t_ASSIGN            = r'ASSIGN'
t_BEGIN             = r'BEGIN'
t_COLON             = r'\:'
t_COMMA             = r','
t_ignore_COMMENT    = r'[(][^\n)]*[)]'
t_DIVIDE            = r'/'
t_ELSE              = r'ELSE'
t_END               = r'END'
t_ENDIF             = r'ENDIF'
t_IF                = r'IF'
t_LEFT_SBRACKET     = r'\['
t_LPAREN            = r'\('
t_MINUS             = r'-'
t_PLUS              = r'\+'
t_RIGHT_SBRACKET    = r'\]'
t_RPAREN            = r'\)'
t_SEMICOLON         = r';'
t_THEN              = r'THEN'
t_TIMES             = r'\*'
t_VAR               = r'VAR'
t_WRITE             = r'WRITE'


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
 
