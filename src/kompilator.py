import ply.lex as lex
import ply.yacc as yacc
from grammar import *
from tokens import *
from lexer import *

# print("\n\n")
# while True: 
#     tok = lexer.token() 
#     if not tok: 
#         break # Nigdy więcej input 
#     print("Typ: ", end = '')
#     print(tok.type.ljust(15), end = '')
#     print("     | wartosc: ", end = '')
#     print(str(tok.value).ljust(10), end = '')
#     print("     | numer linii: : ", end = '')
#     print(str(tok.lineno).ljust(10), end = '')
#     print("     | lexpos: ", end = '')
#     print(tok.lexpos)


data = '''
VAR n BEGIN
n ASSIGN 3;
WRITE n;
END
'''
lexer = lex.lex()
lexer.input(data)
parser = yacc.yacc()
parser.parse(data)
 
