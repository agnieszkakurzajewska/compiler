import ply.lex as lex
import ply.yacc as yacc
from grammar import *
from lexer import *
from tokens import *
import sys
import settings

settings.init() 

input = open(sys.argv[1], "r");
input_text = input.read()

lexer = lex.lex()

# data = '''
# '''
# lexer.input(data)
# print("\n\n")
# # Tokenize 
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

parser = yacc.yacc()

parser.parse(input_text, lexer=lexer)
print(settings.output)

output = open(sys.argv[2], "w")
output.write(settings.output)
output.close()