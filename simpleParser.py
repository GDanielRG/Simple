# Yacc example

import ply.yacc as yacc

# Get the token map from the lexer.  This is required.
import simpleTokens
import ParseTree
tokens = simpleTokens.tokens

precedence = (
    ('right', 'ASSIGNATION'),
    ('left', 'OR'),
    ('left', 'AND'),
    ('left', 'EQUALITY'),
    ('left', 'GREATER', 'LESSER'),
    ('left', 'PLUS', 'MINUS'),
    ('left', 'MULTIPLICATION', 'DIVISION', 'MODULUS'),
    ('right','NOT')
)

globalVariableType = ''
globalBlockType = ''
globalDeclarations = list()
globalDeclarationsExtra = list()

globalBlocks = list()

globalExpressionItems = list()
globalStatements = list()

def p_simple(p):
    'simple : PROGRAM program ENDPROGRAM'
    # p[0] = ('simple', p[2])
    p[0] = p[2]

def p_empty(p):
    'empty :'
    # p[0] = None

def p_program(p):
    'program : variables blocks main'
    programNode = ParseTree.Program(p[1], p[2], p[3])
    # p[0] = ('program', p[1], p[2], p[3])
    p[0] = programNode

def p_variables(p):
    'variables : VARIABLES declarationList ENDVARIABLES'
    # p[0] = ('variables', p[2])
    global globalDeclarations
    p[0] = globalDeclarations
    globalDeclarations = list()

def p_emptyVariables(p):
    'variables : empty'
    # p[0] = p[1]
    p[0] = list()

def p_declarationList(p):
    'declarationList : declaration declarationList' 
    # p[0] = ('declarations', p[1], p[2])
    

def p_emptyDeclarationList(p):
    'declarationList : empty'
    # p[0] = p[1] 
    # p[0] = None 


def p_declaration(p):
    'declaration : variableType IDENTIFIER ASSIGNATION expression declarationExtra SEMICOLON' 
    global globalDeclarations
    global globalDeclarationsExtra
    global globalVariableType
    variable = ParseTree.Variable(globalVariableType, p[2], None, None)
    globalDeclarations.append(variable)
    while(globalDeclarationsExtra):
        globalDeclarations.append(globalDeclarationsExtra.pop())
    globalDeclarationsExtra = list()
        
    # p[0] = [x for x in globalDeclarations if x is not None]
    # p[0] = ('declaration', p[1], p[2], p[4], p[5])  

def p_arrayDeclaration(p):
    'declaration : arrayType IDENTIFIER OBRACKETS arrayIndexes CBRACKETS ASSIGNATION expression arrayDeclarationExtra SEMICOLON' 
    global globalDeclarations
    global globalDeclarationsExtra
    global globalVariableType
    variable = ParseTree.Variable(globalVariableType, p[2], None, {'arrayIndexes': p[4]})
    globalDeclarations.append(variable)
    while(globalDeclarationsExtra):
        globalDeclarations.append(globalDeclarationsExtra.pop())
    globalDeclarationsExtra = list()

    # p[0] = ('arrayDeclaration', p[1], p[2], p[4], p[7], p[8])  
    # p[0] = [x for x in globalDeclarations if x is not None]

def p_nullDeclaration(p):
    'declaration : variableType IDENTIFIER declarationExtra SEMICOLON' 
    global globalDeclarations
    global globalDeclarationsExtra
    global globalVariableType
    variable = ParseTree.Variable(globalVariableType, p[2], None, None)
    globalDeclarations.append(variable)
    while(globalDeclarationsExtra):
        globalDeclarations.append(globalDeclarationsExtra.pop())
    globalDeclarationsExtra = list()

def p_arrayNullDeclaration(p):
    'declaration : arrayType IDENTIFIER OBRACKETS arrayIndexes CBRACKETS arrayDeclarationExtra SEMICOLON' 
    global globalDeclarations
    global globalDeclarationsExtra
    global globalVariableType
    variable = ParseTree.Variable(globalVariableType, p[2], None, {'arrayIndexes': p[4]})
    globalDeclarations.append(variable)
    while(globalDeclarationsExtra):
        globalDeclarations.append(globalDeclarationsExtra.pop())
    globalDeclarationsExtra = list()

    # p[0] = ('declaration', p[1], p[2], p[3])  
    # p[0] = [x for x in globalDeclarations if x is not None]    

def p_emptyDeclaration(p):
    'declaration : empty'
    # p[0] = p[1]    
    # p[0] = None    

def p_declarationExtra(p):
    'declarationExtra : COMMA IDENTIFIER ASSIGNATION expression declarationExtra'
    global globalDeclarationsExtra
    global globalVariableType
    variable = ParseTree.Variable(globalVariableType, p[2], None, None)
    globalDeclarationsExtra.append(variable)

    # p[0] = ('declarationExtra', p[2], p[4], p[5])  
    # p[0] = [x for x in globalDeclarations if x is not None]

def p_arrayDeclarationExtra(p):
    'arrayDeclarationExtra : COMMA IDENTIFIER OBRACKETS arrayIndexes CBRACKETS ASSIGNATION expression arrayDeclarationExtra'
    global globalDeclarations
    global globalVariableType
    variable = ParseTree.Variable(globalVariableType, p[2], None, {'arrayIndexes': p[4]})
    globalDeclarationsExtra.append(variable)

    # p[0] = ('arrayDeclarationExtra', p[2], p[4], p[7], p[8])  
    # p[0] = [x for x in globalDeclarations if x is not None]

def p_nullDeclarationExtra(p):
    'declarationExtra : COMMA IDENTIFIER declarationExtra'
    global globalDeclarations
    global globalVariableType
    variable = ParseTree.Variable(globalVariableType, p[2], None, None)
    globalDeclarationsExtra.append(variable)

    # p[0] = ('declarationExtra', p[2], p[3])  
    # p[0] = [x for x in globalDeclarations if x is not None]
    

def p_arrayNullDeclarationExtra(p):
    'arrayDeclarationExtra : COMMA IDENTIFIER OBRACKETS arrayIndexes CBRACKETS arrayDeclarationExtra'
    global globalDeclarations
    global globalVariableType
    variable = ParseTree.Variable(globalVariableType, p[2], None, {'arrayIndexes': p[4]})
    globalDeclarationsExtra.append(variable)

    # p[0] = ('declarationExtra', p[2], p[4], p[6])  
    # p[0] = [x for x in globalDeclarations if x is not None]


def p_emptyDeclarationExtra(p):
    'declarationExtra : empty'
    # p[0] = p[1]
    # p[0] = None

def p_emptyArrayDeclarationExtra(p):
    'arrayDeclarationExtra : empty'
    # p[0] = p[1]
    # p[0] = None

def p_arrayIndexes(p):
    'arrayIndexes : NUMBERVALUE arrayIndexesExtra'
    # p[0] = ('arrayIndexes', p[1], p[2])
    # p[0] = '1,2,3'

def p_arrayIndexesExtra(p):
    'arrayIndexesExtra : COMMA NUMBERVALUE arrayIndexesExtra'
    # p[0] = ('arrayIndexesExtra', p[2], p[3])

def p_emptyArrayIndexesExtra(p):
    'arrayIndexesExtra : empty'
    # p[0] = p[1]
    # p[0] = None

def p_blocks(p):
    'blocks : BLOCKS blockList ENDBLOCKS' 
    global globalBlocks
    p[0] = globalBlocks
    globalBlocks = list()
    # p[0] = ('blocks', p[2])

def p_emptyBlocks(p):
    'blocks : empty' 
    # p[0] = p[1]
    # p[0] = None

def p_blockList(p):
    'blockList : block blockList' 
    # p[0] = ('blocks', p[2])

def p_emptyBlockList(p):
    'blockList : empty' 
    # p[0] = ('blocks', p[2])

def p_block(p):
    'block : DEFINE blockType IDENTIFIER parameters variables statementPoint ENDDEFINE' 
    global globalBlocks
    global globalBlockType
    block = ParseTree.Block(globalBlockType, p[3], p[5], None, p[6])
    globalBlocks.append(block)
    # p[0] = ('block', p[2], p[3], p[4], p[5], p[6], p[8]) 

def p_emptyBlock(p):
    'block : empty' 
    # p[0] = p[1]
    # p[0] = None


def p_blockType(p):
    '''blockType : PROCEDURE
                  | variableType
                  | arrayType''' 
    # p[0] = ('blockType', p[1])   
    global globalBlockType              
    globalBlockType = p[1]

def p_variableType(p):
    '''variableType : NUMBER 
                  | WORDS
                  | LETTER
                  | FLAG''' 
    # p[0] = ('variableType', p[1])    
    global globalVariableType              
    globalVariableType = p[1]
    p[0] = p[1]

def p_arrayType(p):
    'arrayType : MANYNUMBERS' 
    # p[0] = ('variableType', p[1])    
    global globalVariableType              
    globalVariableType = p[1]
    p[0] = p[1]

def p_parameters(p):
    'parameters : OPARENTHESIS parameter CPARENTHESIS'
    # p[0] = ('parameters', p[2])   

def p_parameter(p):
    'parameter : variableType IDENTIFIER parameterExtra' 
    # p[0] = ('parameter', p[1], p[2], p[3])    

def p_emptyParameter(p):
    'parameter : empty' 
    # p[0] = p[1]
    # p[0] = None

def p_parameterExtra(p):
    'parameterExtra : COMMA variableType IDENTIFIER parameterExtra' 
    # p[0] = ('parameterExtra', p[2], p[3], p[4]) 

def p_emptyParameterExtra(p):
    'parameterExtra : empty' 
    # p[0] = p[1]
    # p[0] = None

def p_statementPoint(p):
    'statementPoint : statementList' 
    global globalStatements
    p[0] = globalStatements
    globalStatements = list()

def p_statementList(p):
    'statementList : statement statementList' 

def p_emptyStatementList(p):
    'statementList : empty' 
    # p[0] = ('blocks', p[2])


def p_statement(p):
    '''statement : assign SEMICOLON 
                   | call SEMICOLON 
                   | return  empty 
                   | ifStatement empty 
                   | whileStatement empty''' 
    
    # p[0] = ('statement', p[1], p[3]) 

def p_emptyStatement(p):
    'statement : empty' 
    # p[0] = p[1]
    # p[0] = None

def p_assign(p):
    'assign : location ASSIGNATION expression '
    global globalExpressionItems
    global globalStatements
    globalStatements.append(ParseTree.Statement('assignment', ParseTree.Expression(globalExpressionItems), None, {'variable': p[0]}))
    globalExpressionItems = list() 
    # p[0] = ('assign', p[1], p[3]) 
    

def p_location(p):
    'location : IDENTIFIER'
    p[0] = p[1]
    
def p_locationBracket(p):
    'location : IDENTIFIER OBRACKETS arrayIndexes CBRACKETS'
    # p[0] = ('bracketLocation', p[1], p[3])     

def p_locationCall(p):
    'location : call'
    # p[0] = ('callOnLocation', p[1])     

def p_call(p):
    'call : IDENTIFIER OPARENTHESIS actuals CPARENTHESIS'
    # p[0] = ('call', p[1], p[3])    

def p_actuals(p):
    'actuals : expression commaExpressionList'
    # p[0] = ('actuals', p[1], p[2])   

def p_commaExpressionList(p):
    'commaExpressionList : commaExpression commaExpressionList'
    # p[0] = ('commaExpressionList', p[1], p[2])   

def p_emptyCommaExpressionList(p):
    'commaExpressionList : empty'
    # p[0] = p[1]
    # p[0] = None

def p_commaExpression(p):
    'commaExpression : COMMA expression'
    # p[0] = ('expressionOncommaExpression',p[2])

def p_return(p):
    'return : RETURN returnExpression SEMICOLON'
    # p[0] = ('return', p[2])   

def p_returnExpression(p):
    'returnExpression : expression' 
    # p[0] = ('expressionOnReturn', p[1])    

def p_emptyReturnExpression(p):
    'returnExpression : empty' 
    # p[0] = p[1]  
    # p[0] = None  

def p_ifStatement(p):
    'ifStatement : IF OPARENTHESIS expression CPARENTHESIS statementPoint elseStatement ENDIF'
    global globalExpressionItems
    globalStatements.append(ParseTree.Statement('if', ParseTree.Expression(globalExpressionItems), p[5], {'else': p[6]}))
    globalExpressionItems = list()
    # p[0] = ('ifStatement', p[3], p[5], p[6]) 

def p_elseStatement(p):
    'elseStatement : ELSE statementPoint'
    # global globalStatements
    p[0] = ParseTree.Statement('else', None, p[2])
    # globalStatements = list() 
    # p[0] = statement 
    # print('else')
    

def p_emptyElseStatement(p):
    'elseStatement : empty'
    # global globalStatements
    # statement = ParseTree.Statement('else', None)
    # globalStatements = list() 
    # p[0] = statement 
    # p[0] = p[1]
    # p[0] = None

def p_whileStatement(p):
    'whileStatement : WHILE OPARENTHESIS expression CPARENTHESIS statementPoint ENDWHILE'
    # p[0] = ('whileStatement', p[3], p[5]) 

def p_main(p):
    'main : START variables statementPoint FINISH '
    # p[0] = ('main', p[2], p[3]) 
    p[0] = ParseTree.Main(p[2], p[3])

def p_expressionLocation(p):
    'expression : location'
    p[0] = p[1]
    # p[0] = None

def p_expressionUnary(p):
    'expression : unaryExpression'
    p[0] = p[1]
    # p[0] = None

def p_expressionBinary(p):
    'expression : binaryExpression'
    p[0] = p[1]
    # p[0] = None

def p_expressionTokens(p):
    '''expression : FLAGVALUE
                  | NUMBERVALUE
                  | WORDSVALUE
                  | LETTERVALUE''' 
    p[0] = p[1]
    # p[0] = None

def p_parentesisExpression(p):
    'expression : OPARENTHESIS expression CPARENTHESIS'
    p[0] = p[2]

def p_binaryExpressionOr(p):
    'binaryExpression : expression OR expression'
    p[0] = ("OR", p[1], p[3])

def p_binaryExpressionAnd(p):
    'binaryExpression : expression AND expression'
    p[0] = ("AND", p[1], p[3])

def p_binaryExpressionLessThan(p):
    'binaryExpression : expression LESSER expression'
    p[0] = ("<", p[1], p[3])

def p_binaryExpressionGreaterThan(p):
    'binaryExpression : expression GREATER expression'
    p[0] = (">", p[1], p[3])

def p_binaryExpressionEquality(p):
    'binaryExpression : expression EQUALITY expression'
    p[0] = (">", p[1], p[3])

def p_binaryExpressionPlus(p):
    'binaryExpression : expression PLUS expression'
    # p[0] = ("+", p[1], p[3])
    global globalExpressionItems
    expressionItem = ParseTree.ExpressionItem('+', [p[1], p[3]])
    globalExpressionItems.append(expressionItem)

def p_binaryExpressionMinus(p):
    'binaryExpression : expression MINUS expression'
    p[0] = ("-", p[1], p[3])

def p_binaryExpressionMultiplication(p):
    'binaryExpression : expression MULTIPLICATION expression'
    global globalExpressionItems
    expressionItem = ParseTree.ExpressionItem('*', [p[1], p[3]])
    globalExpressionItems.append(expressionItem)

def p_binaryExpressionDivision(p):
    'binaryExpression : expression DIVISION expression'
    p[0] = ("/", p[1], p[3])

def p_binaryExpressionModulus(p):
    'binaryExpression : expression MODULUS expression'
    p[0] = ("%", p[1], p[3])

def p_unaryExpressionNOT(p):
    'unaryExpression : NOT expression'
    p[0] = ("NOT", p[2])


# Error rule for syntax errors
def p_error(p):
    if p:
        print("Syntax error at '%s'" % p.value)
        print("Syntax error at line '%s'" % p.lineno)
    else:
        print("Syntax error at EOF")

# Build the parser
parser = yacc.yacc()

 #Test it out
# data = '''program

#  variables
#  number x = 3.1, y = 5, danielito = 4;
#  manynumbers xd [12.1 - 1] = 3;
#  words mundial = "hola mundo";
#  endvariables

#  blocks
#  define procedure imprimeMultiplicacion(number a, number b)
#  enddefine
#  define flag danielitoEsPeor(number a)
#     if (not danielito < a)
#         return true;
#     else
#         return false;
#     endif
#  enddefine
#  define number multiplicarConDanielito(number a)
#   variables
#  manynumbers xq[15];
#  endvariables
#     return (a * danielito);
#  enddefine
#  define manynumbers juan(number a)
#  variables
#  number k = 10;
#  number x = 0;
#  endvariables

#  enddefine
#  define words agregarMundial(words s)

#  enddefine
#  endblocks
#  start
#    variables
#      number n = 2;
#      words palabra = "a";
#      flag toggle = true;
#    endvariables

#    if(not toggle) 
#         x = xd[1];
#     else
#         while(x < 20)
#             x = multiplicarConDanielito(y);
#         endwhile
#     endif

#  finish
#  endprogram
                # r = a * ( b + c - d * f / g ) + h > ( d + e ) * f and ( a + b * ( c - d ) / h ) + g < b;

#  '''
 
data ='''
    program
        blocks 
            define number funcionmamalona(number x, flag y)
                x = y;
            enddefine

        endblocks
        start
            variables
                number x=3, y=4, z=3, z=7;
                flag x=true;
                number x=3;
            endvariables
            if(r==x)
                r=x;
                r=x;
            else
                x=r;
                if(x==4)
                    x=r;
                else
                    x=r;
                endif
                x=r;
            endif
            p=r;
            p=r;
        finish
    endprogram'''
result = yacc.parse(data)
result.print()