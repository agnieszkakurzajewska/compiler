from tokens import *
import ply.lex as lex

class Lexer:



    def __init__(self):

        data = '''
        VAR n BEGIN
        n ASSIGN 3;
        WRITE n;
        END
        '''

        lex.lex()    
        lex.input(data)


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
