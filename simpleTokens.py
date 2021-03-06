# ------------------------------------------------------------
# calclex.py
#
# tokenizer for a simple expression evaluator for
# numbers and +,-,*,/
# ------------------------------------------------------------
import ply.lex as lex

#List of reserved words that shouldn't be confused for identifiers
reserved = (
   'NOT','AND','OR','START', 'FINISH', 'WORDS', 'NUMBER', 'MANYNUMBERS', 'LETTER','PROCEDURE', 
   'FLAG','IF','ENDIF','DEFINE','ENDDEFINE','WHILE','ENDWHILE','ELSE',
   'BLOCKS','ENDBLOCKS','VARIABLES','ENDVARIABLES','PROGRAM','ENDPROGRAM','DISPLAY','RETURN'
)

# List of token names.   This is always required
tokens = reserved + (
   'GREATER',
   'LESSER',
   'EQUALITY',
   'ASSIGNATION',
   'PLUS',
   'MINUS',
   'MULTIPLICATION',
   'DIVISION',
   'MODULUS',
   'NUMBERVALUE',
   'FLAGVALUE',
   'LETTERVALUE',
   'WORDSVALUE',
   'IDENTIFIER',
   'NEWLINE',
   # 'WHITESPACE',
   'COMMA',
   'SEMICOLON',
   'OPARENTHESIS',
   'CPARENTHESIS',
   'OBRACKETS',
   'CBRACKETS'
)

# Regular expression rules for simple tokens
t_GREATER    = r'\>'
t_LESSER    = r'\<'
t_EQUALITY    = r'=='
t_ASSIGNATION   = r'='
t_PLUS    = r'\+'
t_MINUS   = r'-'
t_MODULUS = r'%'
t_MULTIPLICATION   = r'\*'
t_DIVISION  = r'/'
t_OPARENTHESIS  = r'\('
t_CPARENTHESIS  = r'\)'
t_LETTERVALUE = r'(L)?\'([^\\\n]|(\\.))*?\''
t_WORDSVALUE = r'\".*?\"'
t_COMMA = r'\,'
t_SEMICOLON = r'\;'
t_OBRACKETS  = r'\['
t_CBRACKETS  = r'\]'


# A regular expression rule with some action code

def t_NUMBERVALUE(t):
    r'\d+(\.(\d)+)?'
    t.value = float(t.value)    
    return t

def t_FLAGVALUE(t):
    r'true|false'
    if t.value == 'true':
      t.value = True
    else:
      t.value = False
    return t

# Define a rule so we can track line numbers
def t_NEWLINE(t):
    r'\n+'
    t.lexer.lineno += len(t.value)

# Identifiers and reserved words

reserved_map = {}
for r in reserved:
    reserved_map[r.lower()] = r


def t_IDENTIFIER(t):
    r'[A-Za-z_][\w_]*'
    t.type = reserved_map.get(t.value, "IDENTIFIER")
    return t

# A string containing ignored characters (spaces and tabs)
t_ignore  = ' \t'

# Error handling rule
def t_error(t):
    print("Illegal character '%s'" % t.value[0])
    t.lexer.skip(1)

# Build the lexer
lexer = lex.lex()

