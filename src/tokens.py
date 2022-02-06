tokens = (
'ASSIGN',
'BEGIN',
'COLON',
'COMMA',
'COMMENT',
'DIV',
'DO',
'DOWNTO',
'ELSE',
'END',
'ENDIF',
'ENDFOR',
'ENDWHILE',
'EQ',
'FOR',
'FROM',
'GE',
'GEQ',
'IF',
'LE',
'LEQ',
'LEFT_SBRACKET',
'LPAREN',
'MINUS',
'MOD',
'NEQ',
'PLUS',
'READ',
'REPEAT',
'RIGHT_SBRACKET',
'RPAREN',
'SEMICOLON',
'THEN',
'TIMES',
'TO',
'UNTIL',
'VAR',
'WHILE',
'WRITE',
'pidentifier',
'num',
)

t_ASSIGN            = r'ASSIGN'
t_BEGIN             = r'BEGIN'
t_COLON             = r'\:'
t_COMMA             = r','
t_ignore_COMMENT    = r'[(][^\n)]*[)]'
t_DIV               = r'/'
t_DO                = r'DO'
t_DOWNTO            = r'DOWNTO'
t_ELSE              = r'ELSE'
t_END               = r'END'
t_ENDIF             = r'ENDIF'
t_ENDFOR            = r'ENDFOR'
t_ENDWHILE          = r'ENDWHILE'
t_EQ                = r'EQ'
t_FOR               = r'FOR'
t_FROM              = r'FROM'
t_GE                = r'GE'
t_GEQ               = r'GEQ'
t_IF                = r'IF'
t_LE                = r'LE'
t_LEQ               = r'LEQ'
t_LEFT_SBRACKET     = r'\['
t_LPAREN            = r'\('
t_MINUS             = r'-'
t_MOD               = r'MOD'
t_NEQ               = r'NEQ'
t_PLUS              = r'\+'
t_READ              = r'READ'
t_REPEAT            = r'REPEAT'
t_RIGHT_SBRACKET    = r'\]'
t_RPAREN            = r'\)'
t_SEMICOLON         = r';'
t_THEN              = r'THEN'
t_TIMES             = r'\*'
t_TO                = r'TO'
t_UNTIL             = r'UNTIL'
t_VAR               = r'VAR'
t_WHILE             = r'WHILE'
t_WRITE             = r'WRITE'
