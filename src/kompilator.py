import ply.lex as lex
from grammar import *
from lexer import *
from tokens import *
import sys

input = open(sys.argv[1], "r");
input_text = input.read()

lexer = lex.lex()
parser = yacc.yacc()

parser.parse(input_text, lexer=lexer)
