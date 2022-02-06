def t_num(t):
    r'[-]?[0-9]+'
    t.value = int(t.value)    
    return t

def t_error(t):
    print("Illegal character '%s'" % t.value[0])
    t.lexer.skip(1)

t_ignore  = ' \t\n'

t_pidentifier = r'[_a-z]+'
