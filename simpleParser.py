# Yacc example

import ply.yacc as yacc

# Get the token map from the lexer.  This is required.
import calclex
tokens = calclex.tokens

def p_start(p):
  'start : expression'

def p_simple(p):
    'simple : PROGRAM program ENDPROGRAM'
    p[0] = ('simple')

def p_empty(p):
    'empty :'
    pass

def p_program(p):
    'program : variables blocks main'
    p[0] = ('program')

def p_variables(p):
    '''variables : VARIABLES declaration ENDVARIABLES
                  | empty''' 
    # if p[1] == empty:
    #    p[0] = ('empty variables')  
    # else:
    p[0] = ('variables')   

def p_declaration(p):
    '''declaration : variableType IDENTIFIER ASSIGNATION expression declarationExtra SEMICOLON declaration
                  | empty''' 
    # if p[1] == empty:
    #    p[0] = ('empty declaration')  
    # else:
    #   p[0] = ('declaration', p[2], p[3])  
    p[0] = ('declaration')  

def p_declarationExtra(p):
    '''declarationExtra : COMMA IDENTIFIER ASSIGNATION expression declarationExtra
                  | empty''' 
    # if p[1] == empty:
    #    p[0] = ('empty declarationExtra')  
    # else:    
    #   p[0] = ('declarationExtra', p[2], p[3])             
    p[0] = ('declarationExtra')  

def p_blocks(p):
    '''blocks : BLOCKS block ENDBLOCKS
                  | empty''' 
    # if p[1] == empty:
    #    p[0] = ('empty variables')  
    # else:
    p[0] = ('variables')  

def p_block(p):
    '''block : DEFINE blockType IDENTIFIER parameters variables ENDDEFINE blockExtra
                  | empty''' 
    # if p[1] == empty:
    #    p[0] = ('empty block')  
    # else:
    #   p[0] = ('block', p[3])  
    p[0] = ('block') 

def p_blockExtra(p):
    '''blockExtra : DEFINE blockType IDENTIFIER parameters variables ENDDEFINE blockExtra
                  | empty''' 
    # if p[1] == empty:
    #    p[0] = ('empty block')  
    # else:
    #   p[0] = ('block', p[3])  
    p[0] = ('block')   

def p_blockType(p):
    '''blockType : PROCEDURE
                  | variableType
                  | empty''' 
    # if p[1] == empty:
    #    p[0] = ('empty blockType')  
    # else:
    p[0] = ('blockType')   

def p_variableType(p):
    '''variableType : NUMBER 
                  | WORDS
                  | LETTER''' 
    p[0] = ('variableType', p[1])                     

def p_parameters(p):
    'parameters : OPARENTHESIS parameter CPARENTHESIS '
    # if p[1] == empty:
    #    p[0] = ('empty parameters')  
    # else:
    p[0] = ('parameters')   

def p_parameter(p):
    '''parameter : variableType IDENTIFIER parameterNext
                  | empty''' 
    # if p[1] == empty:
    #    p[0] = ('empty parameter')  
    # else :
    #   p[0] = ('parameter', p[2]) 
    p[0] = ('parameter')    

def p_parameterNext(p):
    '''parameterNext : COMMA variableType IDENTIFIER parameterNext
                      | empty''' 
    # if p[1] == empty:
    #    p[0] = ('empty parameterNext')  
    # else :
    #   p[0] = ('parameterNext', p[3]) 
    p[0] = ('parameterNext') 

def p_statute(p):
    'statute : empty'
    p[0] = ('emptyStatute') 

def p_main(p):
    'main : START variables statute FINISH '
    p[0] = ('main') 

def p_expression_plus(p):
    'expression : expression PLUS term'
    p[0] = ("+", p[1],p[3])

def p_expression_minus(p):
    'expression : expression MINUS term'
    p[0] = ("-", p[1],p[3])

def p_expression_term(p):
    'expression : term'
    p[0] = p[1]

def p_term_times(p):
    'term : term MULTIPLICATION factor'
    p[0] = ("*", p[1],p[3])

def p_term_div(p):
    'term : term DIVISION factor'
    p[0] = ("/", p[1],p[3])

def p_term_factor(p):
    'term : factor'
    p[0] = p[1]

def p_factor_num(p):
    '''factor : NUMBERVALUE
                  | WORDSVALUE
                  | LETTERVALUE''' 
    p[0] = p[1]

def p_factor_expr(p):
    'factor : OPARENTHESIS expression CPARENTHESIS'
    p[0] = p[2]

# Error rule for syntax errors
def p_error(p):
    if p:
        print("Syntax error at '%s'" % p.value)
        print("Syntax error at line '%s'" % p.lineno)
    else:
        print("Syntax error at EOF")

# Build the parser
parser = yacc.yacc()

# Test it out
data = '''program
variables
number x = 3, y = 5.4, danielito = 4.20;
number xd = 3;
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

# yacc.parse(data)

# result = parser.parse(data)
# print(result)



while True:
   try:
       s = input('calc > ')
   except EOFError:
       break
   if not s: continue
   result = yacc.parse(s)