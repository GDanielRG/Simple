# Yacc example
import ply.yacc as yacc
import sys


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

errors = list()

globalExpressionItems = list()

def flatten(lis):
    """Given a list, possibly nested to any level, return it flattened."""
    new_lis = []
    for item in lis:
        if type(item) == type([]):
            new_lis.extend(flatten(item))
        else:
            new_lis.append(item)
    return new_lis

def p_simple(p):
    'simple : PROGRAM program ENDPROGRAM'
    p[0] = p[2]

def p_empty(p):
    'empty :'

def p_program(p):
    'program : variables blocks main'
    programNode = ParseTree.Program(p[1], p[2], p[3])
    p[0] = programNode

def p_variables(p):
    'variables : VARIABLES declarationList ENDVARIABLES'
    global errors
    variables = {}
    declarations = p[2]
    order = 1
    for declaration in declarations:
        if not declaration.identifier in variables:
            declaration.options['order'] = order
            variables[declaration.identifier] = declaration
        else:
            errors.append('Variable ' + str(declaration.identifier) + ' already declared. Line number: ' + str(declaration.lineNumber))
        order = order + 1
    p[0] = variables

def p_emptyVariables(p):
    'variables : empty'
    p[0] = {}

def p_declarationList(p):
    'declarationList : declaration declarationList' 
    p[0] = flatten([p[1]] + p[2])

def p_emptyDeclarationList(p):
    'declarationList : empty'
    p[0] = list()

def p_declaration(p):
    'declaration : variableType IDENTIFIER ASSIGNATION expression declarationExtra SEMICOLON' 
    expressionItems = p[4]
    expression = ParseTree.Expression(p.lineno(1), expressionItems)
    variable = ParseTree.Variable(p.lineno(2), p[1], p[2], expression, {})
    extraDeclarations = flatten(p[5])
    for extraDeclaration in extraDeclarations:
        extraDeclaration.type = p[1]
    variables = [variable] + extraDeclarations
    p[0] = variables

def p_arrayDeclaration(p):
    'declaration : arrayType IDENTIFIER OBRACKETS arrayIndexes CBRACKETS ASSIGNATION expression arrayDeclarationExtra SEMICOLON' 
    expressionItems = p[7]
    expression = ParseTree.Expression(p.lineno(1), expressionItems)
    variable = ParseTree.Variable(p.lineno(2), p[1], p[2], expression, {'arrayIndexes': p[4]})
    extraDeclarations = flatten(p[8])
    for extraDeclaration in extraDeclarations:
        extraDeclaration.type = p[1]
    variables = [variable] + extraDeclarations
    p[0] = variables    

def p_nullDeclaration(p):
    'declaration : variableType IDENTIFIER declarationExtra SEMICOLON' 
    variable = ParseTree.Variable(p.lineno(2), p[1], p[2], None, {})
    extraDeclarations = flatten(p[3])
    for extraDeclaration in extraDeclarations:
        extraDeclaration.type = p[1]
    variables = [variable] + extraDeclarations
    p[0] = variables

def p_arrayNullDeclaration(p):
    'declaration : arrayType IDENTIFIER OBRACKETS arrayIndexes CBRACKETS arrayDeclarationExtra SEMICOLON' 
    variable = ParseTree.Variable(p.lineno(2), p[1], p[2], None, {'arrayIndexes': p[4]})
    extraDeclarations = flatten(p[6])
    for extraDeclaration in extraDeclarations:
        extraDeclaration.type = p[1]
    variables = [variable] + extraDeclarations
    p[0] = variables

def p_declarationExtra(p):
    'declarationExtra : COMMA IDENTIFIER ASSIGNATION expression declarationExtra'
    expressionItems = p[4]
    expression = ParseTree.Expression(p.lineno(1), expressionItems)
    variable = ParseTree.Variable(p.lineno(2), None, p[2], expression, {})
    variables = flatten([variable] + p[5])    
    p[0] = variables

def p_arrayDeclarationExtra(p):
    'arrayDeclarationExtra : COMMA IDENTIFIER OBRACKETS arrayIndexes CBRACKETS ASSIGNATION expression arrayDeclarationExtra'
    expressionItems = p[7]
    expression = ParseTree.Expression(p.lineno(1), expressionItems)
    variable = ParseTree.Variable(p.lineno(2), None, p[2], expression, {'arrayIndexes': p[4]})
    variables = flatten([variable] + p[8])    
    p[0] = variables

def p_nullDeclarationExtra(p):
    'declarationExtra : COMMA IDENTIFIER declarationExtra'
    variable = ParseTree.Variable(p.lineno(2), None, p[2], None, {})
    variables = flatten([variable] + p[3])    
    p[0] = variables

def p_arrayNullDeclarationExtra(p):
    'arrayDeclarationExtra : COMMA IDENTIFIER OBRACKETS arrayIndexes CBRACKETS arrayDeclarationExtra'
    variable = ParseTree.Variable(p.lineno(2), None, p[2], None, {'arrayIndexes': p[4]})
    variables = flatten([variable] + p[6])    
    p[0] = variables

def p_emptyDeclarationExtra(p):
    'declarationExtra : empty'
    p[0] = list()

def p_emptyArrayDeclarationExtra(p):
    'arrayDeclarationExtra : empty'
    p[0] = list()

def p_arrayIndexes(p):
    'arrayIndexes : expression arrayIndexesExtra'
    expressionItems = p[1]
    expression = ParseTree.Expression(p.lineno(1), expressionItems)
    p[0] = [expression] + p[2]

def p_arrayIndexesExtra(p):
    'arrayIndexesExtra : COMMA expression arrayIndexesExtra'
    expressionItems = p[2]
    expression = ParseTree.Expression(p.lineno(1), expressionItems)
    p[0] = flatten([expression] + p[3])

def p_emptyArrayIndexesExtra(p):
    'arrayIndexesExtra : empty'
    p[0] = list()

def p_blocks(p):
    'blocks : BLOCKS blockList ENDBLOCKS' 
    global errors
    blocks = {}
    functions = p[2]
    for function in functions:
        if not function.identifier in blocks:
            blocks[function.identifier] = function
        else:
            errors.append('Block ' + str(function.identifier) + ' already declared. Line number: ' + str(function.lineNumber))
    p[0] = blocks

def p_emptyBlocks(p):
    'blocks : empty' 

def p_blockList(p):
    'blockList : block blockList'
    p[0] = flatten([p[1]] + p[2])     

def p_emptyBlockList(p):
    'blockList : empty' 
    p[0] = list()

def p_block(p):
    'block : DEFINE blockType IDENTIFIER parameters variables statementPoint ENDDEFINE' 
    parameters = {}
    for parameter in p[4]:
        if parameter.identifier in p[5] or parameter.identifier in parameters:
            errors.append('Variable ' + str(parameter.identifier) + ' already declared in function "' + p[3] + '". Line number: ' + str(p.lineno(1)))
        parameters[parameter.identifier] = parameter
    
    p[0] = ParseTree.Block(p.lineno(1), p[2], p[3], {**parameters, **p[5]}, p[4], p[6])

def p_emptyBlock(p):
    'block : empty' 
    p[0] = None


def p_blockType(p):
    '''blockType : PROCEDURE
                  | variableType
                  | arrayType''' 
    p[0] = p[1]

def p_variableType(p):
    '''variableType : NUMBER 
                    | WORDS
                    | LETTER
                    | FLAG''' 
    p[0] = p[1]

def p_arrayType(p):
    'arrayType : MANYNUMBERS' 
    p[0] = p[1]

def p_parameters(p):
    'parameters : OPARENTHESIS parameter CPARENTHESIS'
    p[0] = flatten(p[2])

def p_parameter(p):
    'parameter : variableType IDENTIFIER parameterExtra' 
    p[0] = [ParseTree.Variable(p.lineno(1), p[1], p[2], None, {'order': 0})] + p[3]

def p_arrayParameter(p):
    'parameter : arrayType IDENTIFIER parameterExtra' 
    p[0] = [ParseTree.Variable(p.lineno(1), p[1], p[2], None, {'order': 0})] + p[3]

def p_emptyParameter(p):
    'parameter : empty' 
    p[0] = list()

def p_parameterExtra(p):
    'parameterExtra : COMMA variableType IDENTIFIER parameterExtra' 
    p[0] = [ParseTree.Variable(p.lineno(1), p[2], p[3], None, {'order': 0})] + p[4]

def p_arrayParameterExtra(p):
    'parameterExtra : COMMA arrayType IDENTIFIER parameterExtra' 
    p[0] = [ParseTree.Variable(p.lineno(1), p[2], p[3], None, {'order': 0})] + p[4]

def p_emptyParameterExtra(p):
    'parameterExtra : empty' 
    p[0] = list()

def p_statementPoint(p):
    'statementPoint : statementList' 
    p[0] = p[1]

def p_statementList(p):
    'statementList : statement statementList' 
    p[0] = flatten([p[1]] + p[2])

def p_emptyStatementList(p):
    'statementList : empty' 
    p[0] = list()

def p_statement(p):
    '''statement : assign SEMICOLON 
                   | display SEMICOLON                 
                   | statementCall SEMICOLON 
                   | return  empty 
                   | ifStatement empty 
                   | whileStatement empty''' 
    p[0] = p[1]

def p_statementCall(p):
    'statementCall : IDENTIFIER OPARENTHESIS actuals CPARENTHESIS'
    p[0] = ParseTree.Statement(p.lineno(1), 'call', None, None, {'parameters': p[3], 'identifier': p[1]})    

def p_emptyStatementCall(p):
    'statementCall : IDENTIFIER OPARENTHESIS  CPARENTHESIS'
    p[0] = [ParseTree.ExpressionItem(p.lineno(1), 'call', p[1], {'parameters': list()})]

def p_display(p):
    'display : DISPLAY OPARENTHESIS actuals CPARENTHESIS'
    p[0] = ParseTree.Statement(p.lineno(1), 'display', None, None, {'parameters': p[3]})    

def p_emptyStatement(p):
    'statement : empty' 
    p[0] = None

def p_assign(p):
    'assign : location ASSIGNATION expression '
    expressionItems = p[3]
    expression = ParseTree.Expression(p.lineno(1), expressionItems)
    if(len(p[1])):
        variable = p[1][0]
    else:
        variable = p[1]
    p[0] = ParseTree.Statement(p.lineno(1), 'assignment', expression, None, {'variable': variable})

def p_location(p):
    'location : IDENTIFIER'
    p[0] = [ParseTree.ExpressionItem(p.lineno(1), 'variable', p[1], {})]
    
def p_locationBracket(p):
    'location : IDENTIFIER OBRACKETS arrayIndexes CBRACKETS'
    p[0] = [ParseTree.ExpressionItem(p.lineno(1), 'variable', p[1], {'arrayIndexes':p[3]})]

def p_call(p):
    'call : IDENTIFIER OPARENTHESIS actuals CPARENTHESIS'
    p[0] = [ParseTree.ExpressionItem(p.lineno(1), 'call', p[1], {'parameters': p[3]})]

def p_emptyCall(p):
    'call : IDENTIFIER OPARENTHESIS  CPARENTHESIS'
    p[0] = [ParseTree.ExpressionItem(p.lineno(1), 'call', p[1], {'parameters': list()})]

def p_singleActual(p):
    'singleActual : expression'
    expressionItems = p[1]
    expression = ParseTree.Expression(p.lineno(1), expressionItems)
    p[0] = expression

def p_singleActualEmpty(p):
    'singleActual : empty'
    p[0] = list()

def p_actuals(p):
    'actuals : expression commaExpressionList'
    expressionItems = p[1]
    expression = ParseTree.Expression(p.lineno(1), expressionItems)
    p[0] = flatten([expression] + p[2])

def p_commaExpressionList(p):
    'commaExpressionList : COMMA expression commaExpressionList'
    expressionItems = p[2]
    expression = ParseTree.Expression(p.lineno(1), expressionItems)
    p[0] = flatten([expression] + p[3])    

def p_emptyCommaExpressionList(p):
    'commaExpressionList : empty'
    p[0] = list()

def p_return(p):
    'return : RETURN expression SEMICOLON'
    expressionItems = p[2]    
    expression = ParseTree.Expression(p.lineno(1), expressionItems)
    p[0] = ParseTree.Statement(p.lineno(1), 'return', expression, None, {})

def p_emptyReturn(p):
    'return : RETURN SEMICOLON'
    p[0] = ParseTree.Statement(p.lineno(1), 'return', None, None, {})

def p_ifStatement(p):
    'ifStatement : IF OPARENTHESIS expression CPARENTHESIS statementPoint elseStatement ENDIF'
    expressionItems = p[3]    
    expression = ParseTree.Expression(p.lineno(1), expressionItems)
    p[0] = ParseTree.Statement(p.lineno(1), 'if', expression, p[5], {'else': p[6]})

def p_elseStatement(p):
    'elseStatement : ELSE statementPoint'
    p[0] = ParseTree.Statement(p.lineno(1), 'else', None, p[2], {})

def p_emptyElseStatement(p):
    'elseStatement : empty'

def p_whileStatement(p):
    'whileStatement : WHILE OPARENTHESIS expression CPARENTHESIS statementPoint ENDWHILE'
    expressionItems = p[3]    
    expression = ParseTree.Expression(p.lineno(1), expressionItems)
    p[0] = ParseTree.Statement(p.lineno(1), 'while', expression, p[5], {})

def p_main(p):
    'main : START variables statementPoint FINISH '
    p[0] = ParseTree.Main(p.lineno(1), p[2], p[3])

def p_expressionLocation(p):
    'expression : location'
    p[0] = p[1]

def p_expressionCall(p):
    'expression : call'
    p[0] = p[1]

def p_expressionUnary(p):
    'expression : unaryExpression'
    p[0] = p[1]

def p_expressionBinary(p):
    'expression : binaryExpression'
    p[0] = p[1]

def p_flagExpressionTokens(p):
    'expression : FLAGVALUE' 
    p[0] = [ParseTree.ExpressionItem(p.lineno(1), 'flagconstant', p[1], {})]

def p_numberExpressionTokens(p):
    'expression : NUMBERVALUE' 
    p[0] = [ParseTree.ExpressionItem(p.lineno(1), 'numberconstant', p[1], {})]

def p_wordsExpressionTokens(p):
    'expression : WORDSVALUE'
    p[0] = [ParseTree.ExpressionItem(p.lineno(1), 'wordsconstant', p[1], {})]

def p_expressionTokens(p):
    'expression : LETTERVALUE'
    p[0] = [ParseTree.ExpressionItem(p.lineno(1), 'letterconstant', p[1], {})]

def p_parentesisExpression(p):
    'expression : OPARENTHESIS expression CPARENTHESIS'
    p[0] = p[2]

def p_binaryExpressionOr(p):
    'binaryExpression : expression OR expression'
    p[0] = flatten([p[1], p[3], ParseTree.ExpressionItem(p.lineno(1), 'operand', 'or')])

def p_binaryExpressionAnd(p):
    'binaryExpression : expression AND expression'
    p[0] = flatten([p[1], p[3], ParseTree.ExpressionItem(p.lineno(1), 'operand', 'and')])

def p_binaryExpressionLessThan(p):
    'binaryExpression : expression LESSER expression'
    p[0] = flatten([p[1], p[3], ParseTree.ExpressionItem(p.lineno(1), 'operand', '<')])

def p_binaryExpressionGreaterThan(p):
    'binaryExpression : expression GREATER expression'
    p[0] = flatten([p[1], p[3], ParseTree.ExpressionItem(p.lineno(1), 'operand', '>')])

def p_binaryExpressionEquality(p):
    'binaryExpression : expression EQUALITY expression'
    p[0] = flatten([p[1], p[3], ParseTree.ExpressionItem(p.lineno(1), 'operand', '==')])

def p_binaryExpressionPlus(p):
    'binaryExpression : expression PLUS expression'
    p[0] = flatten([p[1], p[3], ParseTree.ExpressionItem(p.lineno(2), 'operand', '+')])

def p_binaryExpressionMinus(p):
    'binaryExpression : expression MINUS expression'
    p[0] = flatten([p[1], p[3], ParseTree.ExpressionItem(p.lineno(2), 'operand', '-')])

def p_binaryExpressionMultiplication(p):
    'binaryExpression : expression MULTIPLICATION expression'
    p[0] = flatten([p[1], p[3], ParseTree.ExpressionItem(p.lineno(2), 'operand', '*')])

def p_binaryExpressionDivision(p):
    'binaryExpression : expression DIVISION expression'
    p[0] = flatten([p[1], p[3], ParseTree.ExpressionItem(p.lineno(2), 'operand', '/')])

def p_unaryExpressionNOT(p):
    'unaryExpression : NOT expression'
    p[0] = flatten([p[2], ParseTree.ExpressionItem(p.lineno(2), 'operand', 'not')])

# Error rule for syntax errors
def p_error(p):
    if p:
        print("Syntax error at '%s'" % p.value)
        print("Syntax error at line '%s'" % p.lineno)
    else:
        print("Syntax error at EOF")

# Build the parser
parser = yacc.yacc()

def checkSemantics(programNode):
    # check for variables with same name as a function
    variables = set()
    errors = list()
    if(programNode.variables):
        for key, variable in programNode.variables.items():
            variables.add(variable.identifier)
    
    if(programNode.main.variables):
        for key, variable in programNode.main.variables.items():
            variables.add(variable.identifier)

    if(programNode.blocks):
        for key, block in programNode.blocks.items():
            for key, variable in block.variables.items():
                variables.add(variable.identifier)
    
    if(programNode.blocks):
        for key, block in programNode.blocks.items():
            for variable in variables:
                if(variable == block.identifier):
                    errors.append('Variable contains same name as block "' + variable +'". Line number: ' + str(block.lineNumber))
    return errors

f = open("/Users/Daniel/Documents/OneDrive/ITESM/Compiladores/Simple/IDE/public/danyrod94@gmail.com2","r")
# f = open("C:\\Users\\Daniel\\Documents\\Projects\\Simple\\IDE\\public\\danyrod94@gmail.com2","r")

data = f.read()

result = yacc.parse(data)
result.createVariableReferences()
result.setValuesForVariables()         

result.print()
quadruples = result.buildQuadruples()
errors = errors + checkSemantics(result)

