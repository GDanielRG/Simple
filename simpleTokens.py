# ------------------------------------------------------------
# calclex.py
#
# tokenizer for a simple expression evaluator for
# numbers and +,-,*,/
# ------------------------------------------------------------
import ply.lex as lex

#List of reserved words that shouldn't be confused for identifiers
reserved = (
   'NOT','AND','OR','START', 'FINISH', 'WORDS', 'NUMBER','LETTER','PROCEDURE', 
   'TOGGLE','IF','ENDIF','DEFINE','ENDDEFINE','WHILE','ENDWHILE','ELSE',
   'BLOCKS','ENDBLOCKS','VARIABLES','ENDVARIABLES','PROGRAM','ENDPROGRAM','DISPLAY', 'TRUE', 'FALSE','RETURN'
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
   'NUMBERVALUE',
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

# Whitespace
# def t_WHITESPACE(t):
#     r'\s+'
#     t.lexer.lineno += t.value.count("\n")
#     return t

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
    
#def t_ID(t):
#    r'[A-Z][A-Z0-9]*'
#    if t.value in keywords:
#        t.type = t.value
#    return t  

# A string containing ignored characters (spaces and tabs)
t_ignore  = ' \t'

# Error handling rule
def t_error(t):
    print("Illegal character '%s'" % t.value[0])
    t.lexer.skip(1)

# Build the lexer
lexer = lex.lex()

# Test it out
data = '''
program
variables
number x = 3, y = 5.4, danielito = 4.20;
words mundial = "hola mundo";
endvariables
blocks
define procedure imprimeMultiplicacion(number a, number b)

enddefine
define number multiplicarConDanielito(number a)

enddefine
define number juan(number a)
variables
number k = 10;
number x = 0;
endvariables

enddefine
define words agregarMundial(words s)

enddefine
endblocks
start
  variables
    number n = 2;
    words palabra = "";
  endvariables

finish
endprogram

'''


# Give the lexer some input
lexer.input(data)

# Tokenize
while True:
    tok = lexer.token()
    if not tok: 
        break      # No more input
    #print(tok)

    #print(tok.type, tok.value, tok.lineno, tok.lexpos)
