def p_program(p):
    '''
    program : VAR declarations BEGIN commands END
            | BEGIN commands END
    '''
    print("program")

def p_declarations(p):
    '''
    declarations : declarations COMMA pidentifier
                 | declarations COMMA pidentifier LEFT_SBRACKET num COLON num RIGHT_SBRACKET
                 | pidentifier
                 | pidentifier LEFT_SBRACKET num COLON num RIGHT_SBRACKET
    '''
    print("declarations")

def p_commands(p):
    '''
    commands     : commands command
                 | command
    '''
    print("commands")

def p_command(p):
    '''
    command      : identifier ASSIGN expression SEMICOLON
                 | IF condition THEN commands ELSE commands ENDIF
                 | IF condition THEN commands ENDIF
                 | WHILE condition DO commands ENDWHILE
                 | REPEAT commands UNTIL condition SEMICOLON
                 | FOR pidentifier FROM value TO value DO commands ENDFOR
                 | FOR pidentifier FROM value DOWNTO value DO commands ENDFOR
                 | READ identifier SEMICOLON
                 | WRITE value SEMICOLON
    '''
    print("command")

def p_expression(p):
    '''
    expression   : value
                 | value PLUS value
                 | value MINUS value
                 | value TIMES value
                 | value DIV value
                 | value MOD value
    '''
    print("expression")

def p_condition(p):
    '''
    condition    : value EQ value
                 | value NEQ value
                 | value LE value
                 | value GE value
                 | value LEQ value
                 | value GEQ value
    '''
    print("condition")

def p_value(p):
    '''
    value        : num
                 | identifier
    '''
    print("value")

def p_identifier(p):
    '''
    identifier   : pidentifier
                 | pidentifier LEFT_SBRACKET pidentifier RIGHT_SBRACKET
                 | pidentifier LEFT_SBRACKET num RIGHT_SBRACKET
    '''
    print("identifier")

def p_error(p):
    print("eeeeeeeeeeeeeeee")