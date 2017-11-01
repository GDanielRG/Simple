# Yacc example

import ply.yacc as yacc

# Get the token map from the lexer.  This is required.
import simpleTokens
tokens = simpleTokens.tokens


def p_simple(p):
    'simple : PROGRAM program ENDPROGRAM'
    p[0] = ('simple', p[2])

def p_empty(p):
    'empty :'
    p[0] = None

def p_program(p):
    'program : variables blocks main'
    p[0] = ('program', p[1], p[2], p[3])

def p_variables(p):
    'variables : VARIABLES declaration ENDVARIABLES' 
    p[0] = ('variables', p[2])

def p_emptyVariables(p):
    'variables : empty'
    p[0] = p[1]

def p_declaration(p):
    'declaration : variableType IDENTIFIER ASSIGNATION expression declarationExtra SEMICOLON declaration' 
    p[0] = ('declaration', p[1], p[2], p[4], p[5], p[7])  

def p_arrayDeclaration(p):
    'declaration : variableType IDENTIFIER OBRACKETS arrayIndexes CBRACKETS ASSIGNATION expression declarationExtra SEMICOLON declaration' 
    p[0] = ('arrayDeclaration', p[1], p[2], p[4], p[7], p[8], p[10])  

def p_nullDeclaration(p):
    'declaration : variableType IDENTIFIER declarationExtra SEMICOLON declaration' 
    p[0] = ('declaration', p[1], p[2], p[3], p[5])  

def p_emptyDeclaration(p):
    'declaration : empty'
    p[0] = p[1]    

def p_declarationExtra(p):
    'declarationExtra : COMMA IDENTIFIER ASSIGNATION expression declarationExtra'
    p[0] = ('declarationExtra', p[2], p[4], p[5])  

def p_arrayDeclarationExtra(p):
    'declarationExtra : COMMA IDENTIFIER OBRACKETS arrayIndexes CBRACKETS ASSIGNATION expression declarationExtra'
    p[0] = ('arrayDeclarationExtra', p[2], p[4], p[7], p[8])  

def p_nullDeclarationExtra(p):
    'declarationExtra : COMMA IDENTIFIER declarationExtra'
    p[0] = ('declarationExtra', p[2], p[3])  

def p_array_nullDeclarationExtra(p):
    'declarationExtra : COMMA IDENTIFIER OBRACKETS arrayIndexes CBRACKETS declarationExtra'
    p[0] = ('declarationExtra', p[2], p[4], p[6])  

def p_emptyDeclarationExtra(p):
    'declarationExtra : empty'
    p[0] = p[1]

def p_arrayIndexes(p):
    'arrayIndexes : expression arrayIndexesExtra'
    p[0] = ('arrayIndexes', p[1], p[2])

def p_arrayIndexesExtra(p):
    'arrayIndexesExtra : COMMA expression arrayIndexesExtra'
    p[0] = ('arrayIndexesExtra', p[2], p[3])

def p_emptyArrayIndexesExtra(p):
    'arrayIndexesExtra : empty'
    p[0] = p[1]

def p_blocks(p):
    'blocks : BLOCKS block ENDBLOCKS' 
    p[0] = ('blocks', p[2])

def p_emptyBlocks(p):
    'blocks : empty' 
    p[0] = p[1]

def p_block(p):
    'block : DEFINE blockType IDENTIFIER parameters variables statement ENDDEFINE block' 
    p[0] = ('block', p[2], p[3], p[4], p[5], p[6], p[8]) 

def p_emptyBlock(p):
    'block : empty' 
    p[0] = p[1]


def p_blockType(p):
    '''blockType : PROCEDURE
                  | variableType''' 
    p[0] = ('blockType', p[1])   

def p_variableType(p):
    '''variableType : NUMBER 
                  | WORDS
                  | LETTER''' 
    p[0] = ('variableType', p[1])                  

def p_parameters(p):
    'parameters : OPARENTHESIS parameter CPARENTHESIS '
    p[0] = ('parameters', p[2])   

def p_parameter(p):
    'parameter : variableType IDENTIFIER parameterExtra' 
    p[0] = ('parameter', p[1], p[2], p[3])    

def p_emptyParameter(p):
    'parameter : empty' 
    p[0] = p[1]

def p_parameterExtra(p):
    'parameterExtra : COMMA variableType IDENTIFIER parameterExtra' 
    p[0] = ('parameterExtra', p[2], p[3], p[4]) 

def p_emptyParameterExtra(p):
    'parameterExtra : empty' 
    p[0] = p[1]

def p_statement(p):
    # 'statement : empty' 
    
    '''statement : assign SEMICOLON statement
                  | call SEMICOLON statement''' 
    
    # '''statement : assign SEMICOLON 
    #               | call SEMICOLON
    #               | return  SEMICOLON
    #               | ifStmt
    #               | whileStmt''' 
    p[0] = ('statement', p[1], p[3]) 

def p_emptyStatement(p):
    # 'statement : empty' 
    
    'statement : empty' 
    
    # '''statement : assign SEMICOLON 
    #               | call SEMICOLON
    #               | return  SEMICOLON
    #               | ifStmt
    #               | whileStmt''' 
    p[0] = p[1]

def p_assign(p):
    'assign : location ASSIGNATION expression'
    p[0] = ('assign', p[1], p[3]) 
    

def p_location(p):
    'location : IDENTIFIER'
    p[0] = ('identifier', p[1])
    
def p_locationBracket(p):
    'location : IDENTIFIER OBRACKETS arrayIndexes CBRACKETS'
    p[0] = ('bracketLocation', p[1], p[3])     

def p_locationCall(p):
    'location : call'
    p[0] = ('bracketLocation', p[1], p[3])     

def p_call(p):
    'call : IDENTIFIER OPARENTHESIS actuals CPARENTHESIS'

def p_actuals(p):
    'actuals : expression commaExpressionList'

def p_commaExpressionList(p):
    'commaExpressionList : commaExpression commaExpressionList'  

def p_emptyCommaExpressionList(p):
    'commaExpressionList : empty'

def p_commaExpression(p):
    'commaExpression : COMMA expression'

def p_return(p):
    'return : RETURN returnExpression SEMICOLON'

def p_returnExpression(p):
    'returnExpression : expression'      

def p_main(p):
    'main : START variables statement FINISH '
    p[0] = ('main', p[2], p[3]) 

def p_expressionPlus(p):
    'expression : expression PLUS term'
    p[0] = ("+", p[1], p[3])

def p_expressionMinus(p):
    'expression : expression MINUS term'
    p[0] = ("-", p[1], p[3])

def p_expressionTerm(p):
    'expression : term'
    p[0] = p[1]

def p_termTimes(p):
    'term : term MULTIPLICATION factor'
    p[0] = ("*", p[1], p[3])

def p_termDivision(p):
    'term : term DIVISION factor'
    p[0] = ("/", p[1], p[3])

def p_termFactor(p):
    'term : factor'
    p[0] = p[1]

def p_factorNum(p):
    '''factor : NONZEROINT 
                  | NUMBERVALUE
                  | WORDSVALUE
                  | LETTERVALUE''' 
    p[0] = p[1]

def p_factorExpr(p):
    'factor : OPARENTHESIS expression CPARENTHESIS'
    p[0] = p[2]

def p_factorLocation(p):
    'factor : location'
    p[0] = p[1]

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
# data = '''program
# variables
# number x = 3, y = 5.4, danielito = 4.20;
# number xd [12] = 3;
# words mundial = "hola mundo";
# endvariables
# blocks
# define procedure imprimeMultiplicacion(number a, number b)
# enddefine
# define number multiplicarConDanielito(number a)
# enddefine
# define number juan(number a)
# variables
# number k = 10;
# number x = 0;
# endvariables

# enddefine
# define words agregarMundial(words s)

# enddefine
# endblocks
# start
#   variables
#     number n = 2;
#     words palabra = "";
#   endvariables

# finish
# endprogram
# '''
data = '''program
start
    xd = a-b*c/d+e*f-g;
finish
endprogram
'''
# data = '''program
# variables
# number xd [12,2] = 3, x=3, y;

# endvariables
# start
#     xd = 3;
#     y[2] = 5;
#     r[2,3,4] = xd;
#     f = f[1,2];
# finish
# endprogram
# '''

result = yacc.parse(data)
print(result[0])