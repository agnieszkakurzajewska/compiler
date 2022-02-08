def t_num(t):
    r'[-]?[0-9]+'
    t.value = int(t.value)    
    return t

def t_error(t):
    print("----------------------------------error----------------------------------")
    t.lexer.skip(1)

def t_ignore_comment(t):
    r'(\((.|\n)*?\))'

t_ignore  = '[\n | \t | ]'

t_pidentifier = r'[_a-z]+'
