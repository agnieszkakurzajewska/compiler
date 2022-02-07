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
parser = yacc.yacc()

parser.parse(input_text, lexer=lexer)
print(settings.output)

output = open(sys.argv[2], "w")
output.write(settings.output)
output.close()