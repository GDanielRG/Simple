quadruples = list()
gotof = list()
goto = list()
temporals = 0

def isConstant(string):
    if(string == 'numberconstant' or string == 'wordsconstant' or string == 'letterconstant' or string == 'flagconstant'):
        return True
    return False

def isArray(string):
    if(string == 'manynumbers'):
        return True
    return False

class Program():
    def __init__(self, variables = {}, blocks = {}, main = None):
        self.variables = variables
        self.blocks = blocks
        self.main = main
        self.constants = {}
        self.quadruples = []

    def print(self):
        print('Program:')
        if(self.constants):            
            print('\tConstants:')
            for key,value in self.constants.items():
                value.print(2)

        if(self.variables):            
            print('\tVariables:')
            for key,value in self.variables.items():
                value.print(2)

        if(self.blocks):
            print('\tBlocks:')
            for key,value in self.blocks.items():
                value.print(2)

        if(self.main):
            print('\tMain:')
            if(self.main):
                self.main.print(2)
    def createVariableReferences(self):
        globalVariables = self.variables
        constants = self.constants
        blocks = self.blocks

        # Global variables
        if(self.variables):
            for key, variable in self.variables.items():
                variable.createVariableReferences(globalVariables, {}, constants, blocks)

        mainVariables = self.main.variables
        
        # Main variables
        if(self.main.variables):
            for key, variable in self.main.variables.items():
                variable.createVariableReferences(globalVariables, mainVariables, constants, blocks)


        # Main statements
        for statement in self.main.statements:
            statement.createVariableReferences(globalVariables, mainVariables, constants, blocks)
        
        
        # Blocks statements
        if(self.blocks):
            for key, block in self.blocks.items():
                blockVariables = block.variables
                for statement in block.statements:
                    statement.createVariableReferences(globalVariables, blockVariables, constants, blocks)
                
                for key, variable in block.variables.items():
                    variable.createVariableReferences(globalVariables, blockVariables, constants, blocks)
        
    def setValuesForVariables(self):
        if(self.variables):
            for key, variable in self.variables.items():
                if(variable.expression):
                    if(len(variable.expression.items) == 1 and isConstant(variable.expression.items[0].type)):
                        variable.value = variable.expression.items[0].value.value
                if(isArray(variable.type)):
                    size = 1
                    for expression in variable.options['arrayIndexes']:
                        size *= expression.items[0].value.value
                    variable.value = [None] * int(size)

        if(self.main.variables):        
            for key, variable in self.main.variables.items():
                if(variable.expression):
                    if(len(variable.expression.items) == 1 and isConstant(variable.expression.items[0].type)):
                        variable.value = variable.expression.items[0].value.value
                if(isArray(variable.type)):
                    size = 1
                    for expression in variable.options['arrayIndexes']:
                        size *= expression.items[0].value.value
                    variable.value = [None] * int(size)
        
        if(self.blocks):
            for key, block in self.blocks.items():
                for key, variable in block.variables.items():
                    if(variable.expression):
                        if(len(variable.expression.items) == 1 and isConstant(variable.expression.items[0].type)):
                            variable.value = variable.expression.items[0].value.value
                    if(isArray(variable.type)):
                        size = 1
                        for expression in variable.options['arrayIndexes']:
                            size *= expression.items[0].value.value
                        variable.value = [None] * int(size)

    def buildQuadruples(self):
        if(self.variables):
            for key, variable in self.variables.items():
                if(variable.expression):
                    variable.expression.buildQuadruples()
                    t = '[t'+ str(temporals) + ']'
                    quadruples.append(['=', t, None, variable.identifier])
        
        quadruples.append(['era', '[main]', None, None])

        if(self.main.variables):
            for key, variable in self.main.variables.items():
                if(variable.expression):
                    variable.expression.buildQuadruples()
                    t = '[t'+ str(temporals) + ']'
                    quadruples.append(['=', t, None, variable.identifier])

        if(self.main.statements):
            for statement in self.main.statements:
                statement.buildQuadruples()

        quadruples.append(['end', None, None, None, None])

        if(self.blocks):
            for key, block in self.blocks.items():
                block.firstQuadruple = len(quadruples)
                for statement in block.statements:
                    statement.buildQuadruples()

        
        return quadruples

            
                        

class Variable():
    def __init__(self, lineNumber, type = None, identifier = None, expression = None, options = None, value = None):
        self.lineNumber = lineNumber
        self.type = type
        self.identifier = identifier
        self.expression = expression
        self.options = options
        self.value = value
    
    def print(self, indent = 0):
        string = ''
        for i in range(indent):
            string+='\t'
        print(string + str(self.type) + ': ' + str(self.identifier) + '= ' + str(self.value) + ' @' + str(self.lineNumber))
        if(self.options):
            print('\t' + string + 'Options: ' + str(self.options))
    
    def createVariableReferences(self, globalVariables, blockVariables, constants, blocks):
        if(self.options and 'arrayIndexes' in self.options and self.options['arrayIndexes']):
            expressions = self.options['arrayIndexes']
            for expression in expressions:
                expression.createVariableReferences(globalVariables, blockVariables, constants, blocks)
        if(self.expression):
            self.expression.createVariableReferences(globalVariables, blockVariables, constants, blocks)

        

class Expression():
    def __init__(self, lineNumber, items = list()):
        self.lineNumber = lineNumber
        self.items = items

    def print(self, indent = 0):
        # string = ''
        # for i in range(indent):
        #     string+='\t'
        # if self.items:
        #     print(string + 'Expression items:')            
        #     for item in self.items:
        #         item.print(indent + 1)
        self.printInline(indent)

    def printInline(self, indent = 0):
        string = ''
        for i in range(indent):
            string+='\t'
        if self.items:
            for item in self.items:
                string += str(item.value)
        print(string)
    
    def createVariableReferences(self, globalVariables, blockVariables, constants, blocks):
        for expressionItem in self.items:
            if(expressionItem.type == 'call'):
                block = None
                if(expressionItem.value in blocks):
                    block = blocks[expressionItem.value]
                else:
                    print('Block not found: ' + str(self.options['identifier']))                                    
                expressionItem.value = block

            if(expressionItem.type == 'variable'):
                variable = None
                if(expressionItem.value in blockVariables):
                    variable = blockVariables[expressionItem.value]
                else:
                    if(expressionItem.value in globalVariables):
                        variable = globalVariables[expressionItem.value]
                if(variable):
                    expressionItem.value = variable
                else:
                    print('Variable not found: ' + str(expressionItem.value))
            if(expressionItem.type == 'flagconstant' or expressionItem.type == 'wordsconstant' or expressionItem.type == 'numberconstant' or expressionItem.type == 'letterconstant'):
                if(str(expressionItem.value) not in constants):
                    constants[str(expressionItem.value)] = Variable(0, expressionItem.type, str(expressionItem.value),None, None, expressionItem.value)
                expressionItem.value = constants[str(expressionItem.value)]
            expressionItem.createVariableReferences(globalVariables, blockVariables, constants, blocks)

    def buildQuadruples(self):
        global temporals
        generalStack = list()
        if self.items:
            for item in self.items:
                if(isConstant(item.type)):
                    generalStack.append(str(item.value.identifier))
                if(item.type == 'variable'):
                    if(isArray(item.value.type)):
                        # for(arrayIndex in item.value.options['arrayIndex']):
                        #     arrayIndex.buildVerQuadruples()
                        # quadruples.append(['endver', None, None, None])
                        # item.value.print()
                        item.value = item.value
                    else:
                        generalStack.append( str(item.value.identifier))
                    # item.print()
                    # generalStack.append(item.identifier)

                # Item is operand    
                if(item.type == 'operand'):
                    if(item.value == '+'):
                        b = generalStack.pop()
                        a = generalStack.pop()
                        temporals += 1
                        t = '[t' + str(temporals) + ']'
                        quadruples.append(['+', a, b, t])
                        generalStack.append(t)
                    if(item.value == '*'):
                        b = generalStack.pop()
                        a = generalStack.pop()
                        temporals += 1
                        t = '[t' + str(temporals) + ']'
                        quadruples.append(['*', a, b, t])
                        generalStack.append(t)
                    if(item.value == '/'):
                        b = generalStack.pop()
                        a = generalStack.pop()
                        temporals += 1
                        t = '[t' + str(temporals) + ']'
                        quadruples.append(['/', a, b, t])
                        generalStack.append(t)
                    if(item.value == '<'):
                        b = generalStack.pop()
                        a = generalStack.pop()
                        temporals += 1
                        t = '[t' + str(temporals) + ']'
                        quadruples.append(['<', a, b, t])
                        generalStack.append(t)
                    if(item.value == '>'):
                        b = generalStack.pop()
                        a = generalStack.pop()
                        temporals += 1
                        t = '[t' + str(temporals) + ']'
                        quadruples.append(['>', a, b, t])
                        generalStack.append(t)
                    if(item.value == '=='):
                        b = generalStack.pop()
                        a = generalStack.pop()
                        temporals += 1
                        t = '[t' + str(temporals) + ']'
                        quadruples.append(['==', a, b, t])
                        generalStack.append(t)
                    if(item.value == 'and'):
                        b = generalStack.pop()
                        a = generalStack.pop()
                        temporals += 1
                        t = '[t' + str(temporals) + ']'
                        quadruples.append(['and', a, b, t])
                        generalStack.append(t)
                    if(item.value == 'or'):
                        b = generalStack.pop()
                        a = generalStack.pop()
                        temporals += 1
                        t = '[t' + str(temporals) + ']'
                        quadruples.append(['or', a, b, t])
                        generalStack.append(t)
                    if(item.value == 'not'):
                        a = generalStack.pop()
                        temporals += 1
                        t = '[t' + str(temporals) + ']'
                        quadruples.append(['not', a, None, t])
                        generalStack.append(t)
                        
                if(item.type == 'call'):
                    quadruples.append(['era', item.value.identifier, None, None])
                    counter = 1
                    for expression in item.options['parameters']:
                        expression.buildQuadruples()
                        t = '[t'+ str(temporals) + ']'                
                        quadruples.append(['param', t, None, None])
                    quadruples.append(['gosub', item.value.identifier, None, None])
                    if(item.value.type != 'procedure'):
                        temporals += 1
                        t = '[t'+ str(temporals) + ']'                                        
                        quadruples.append(['=', item.value.identifier, None, t])
                    generalStack.append(t)
                        

                        

                    # if(item.value.type):
                    # if(item.value)

            if(len(generalStack) > 0):
                temporals += 1
                t = '[t' + str(temporals) + ']'                
                quadruples.append(['=', generalStack.pop(), None, t])
                
                

    # def buildVerQuadruples(self):
    #     generalStack = list()
                    



class ExpressionItem():
    def __init__(self, lineNumber, type = None, value = None, options= None):
        self.lineNumber = lineNumber
        self.type = type
        self.value = value
        self.options = options

    def print(self, indent = 0):
        string = ''
        for i in range(indent):
            string+='\t'     
        print(string + self.type + ': ' + str(self.value))
        if(self.options):
            print('\t' + string + 'Options: ' + str(self.options))
    
    def createVariableReferences(self, globalVariables, blockVariables, constants, blocks):
        if(self.options and 'arrayIndexes' in self.options and self.options['arrayIndexes']):
            expressions = self.options['arrayIndexes']
            for expression in expressions:
                expression.createVariableReferences(globalVariables, blockVariables, constants, blocks)
        
        if(self.options and 'parameters' in self.options and self.options['parameters']):
            for expression in self.options['parameters']:
                expression.createVariableReferences(globalVariables, blockVariables, constants, blocks)

class Block():
    def __init__(self, lineNumber, type = None, identifier = None, variables = None, parameters = list(), statements = list()):
        self.lineNumber = lineNumber
        self.type = type
        self.identifier = identifier
        self.variables = variables
        self.parameters = parameters
        self.statements = statements
        self.firstQuadruple = None
    
    def print(self, indent = 0):
        string = ''
        for i in range(indent):
            string+='\t'
        print(string + self.type + ': ' + self.identifier + ' @' + str(self.lineNumber))

        if(self.variables):
            print('\t'+ string + 'Variables:')
            for key,value in self.variables.items():
                value.print(indent + 2)
        
        if(self.parameters):
            print('\t'+ string + 'Parameters:')
            for parameter in self.parameters:
                parameter.print(indent + 2)

        if(self.statements):
            print('\t'+ string + 'Statements:')
            for statement in self.statements:
                statement.print(indent + 2)


class Main():
    def __init__(self, lineNumber, variables = None, statements = None):
        self.lineNumber = lineNumber
        self.variables = variables
        self.statements = statements

    def print(self, indent = 0):
        string = ''
        for i in range(indent):
            string+='\t'
        
        if(self.variables):
            print(string + 'Variables:')
            for key,value in self.variables.items():
                value.print(indent + 1)
        
        if(self.statements):
            print(string + 'Statements:')
            if(self.statements):
                for statement in self.statements:
                    statement.print(indent + 1)

class Statement():
    def __init__(self, lineNumber, type = None, expression = None, statements = None, options = None):
        self.lineNumber = lineNumber
        self.type = type
        self.expression = expression
        self.statements = statements
        self.options = options
    
    def print(self, indent = 0):
        string = '' 
        for i in range(indent):
            string+='\t'
        print(string + self.type + ': ')              
        if(self.expression):
            print('\t' + string + 'Expression:')
            self.expression.print(indent + 2)  
        if(self.statements):
            print('\t' + string + 'Statements:')
            for statement in self.statements:
                statement.print(indent + 2)    
        if(self.options and 'identifier' in self.options and self.options['identifier']):
            print('\t' + string + 'Identifier: ' + self.options['identifier'])
            
        if(self.options and 'parameters' in self.options and self.options['parameters']):
            print('\t' + string + 'Parameters:')                
            for expression in self.options['parameters']:
                expression.print(indent + 2)
            
        
        if(self.options and 'else' in self.options and self.options['else']):
            self.options['else'].print(indent + 1)
        
        if(self.options and 'variable' in self.options and self.options['variable']):
            self.options['variable'].print(indent + 1)


    def createVariableReferences(self, globalVariables, blockVariables, constants, blocks):
        if(self.options and 'variable' in self.options and self.options['variable']):
            variable = None
            expressionItem = self.options['variable']
            if(expressionItem.value in blockVariables):
                variable = blockVariables[expressionItem.value]
            else:
                if(expressionItem.value in globalVariables):
                    variable = globalVariables[expressionItem.value]
            if(variable):
                expressionItem.value = variable
            else:
                print('Variable not found: ' + str(expressionItem.value))
        
        if(self.options and 'else' in self.options and self.options['else']):
            self.options['else'].createVariableReferences(globalVariables, blockVariables, constants, blocks)
        
        if(self.type == 'call'):
            block = None
            if(self.options['identifier'] in blocks):
                block = blocks[self.options['identifier']]
            else:
                print('Block not found: ' + str(self.options['identifier']))                
            self.identifier = block
        

        if(self.expression):
            self.expression.createVariableReferences(globalVariables, blockVariables, constants, blocks)
                
        
        if(self.statements):
            for statement in self.statements:
                statement.createVariableReferences(globalVariables, blockVariables, constants, blocks)
        
        if(self.type == 'assignment'):
            if(self.options and 'variable' in self.options and self.options['variable']):
                variable = self.options['variable']
                if(variable.value.type == "manynumbers"):
                    if('arrayIndexes' not in variable.options):
                        print('Array assignment not supported: "' + variable.value.identifier + '". Line number ' + str(variable.lineNumber))
                    else:
                        if(len(variable.options['arrayIndexes']) != len(variable.value.options['arrayIndexes'])):
                            print('Inconsistent dimensions on assignment of variable "' + variable.value.identifier + '". Line number ' + str(variable.lineNumber))
            if('arrayIndexes' in self.options['variable'].options and self.options['variable'].options['arrayIndexes']):
                for expression in self.options['variable'].options['arrayIndexes']:
                    expression.createVariableReferences(globalVariables, blockVariables, constants, blocks)
        
        if(self.options and 'parameters' in self.options and self.options['parameters']):
            for expression in self.options['parameters']:
                expression.createVariableReferences(globalVariables, blockVariables, constants, blocks)

    def buildQuadruples(self):

        global gotof
        global goto

        if(self.type == 'assignment'):
            self.expression.buildQuadruples()
            t = '[t'+ str(temporals) + ']'
            quadruples.append(['=', t, None, self.options['variable'].value.identifier])
        
        if(self.type == 'call'):
            quadruples.append(['era', self.options['identifier'], None, None])
            counter = 1
            for expression in self.options['parameters']:
                expression.buildQuadruples()
                t = '[t'+ str(temporals) + ']'                
                quadruples.append(['param', t, None, None])
                counter += 1
            quadruples.append(['gosub', self.options['identifier'], None, None])
        
        if(self.type == 'return'):
            if(self.expression):
                self.expression.buildQuadruples()
                t = '[t'+ str(temporals) + ']'                                
                quadruples.append(['return', t, None, None])
            else:
                quadruples.append(['return', None, None, None])
       
        if(self.type == 'if'):
            
            if(self.expression):
                self.expression.buildQuadruples()
                t = '[t'+ str(temporals) + ']'       
                gotof.append(len(quadruples))
                quadruples.append(['gotof', t, None, None])
            if(self.statements):
                for statement in self.statements:
                    statement.buildQuadruples()
            if(self.options and 'else' in self.options and self.options['else']):
                goto.append(len(quadruples))                
                quadruples.append(['goto', t, None, None])
                quadruples[gotof.pop()][3] = len(quadruples)
                for statement in self.options['else'].statements:
                    statement.buildQuadruples()
                quadruples[goto.pop()][3] = len(quadruples)
            else:
                quadruples[gotof.pop()][3] = len(quadruples)
        
        if(self.type == 'while'):
            
            if(self.expression):
                goto.append(len(quadruples))
                self.expression.buildQuadruples()
                t = '[t'+ str(temporals) + ']'   
                gotof.append(len(quadruples))                    
                quadruples.append(['gotof', t, None, None])
            if(self.statements):
                for statement in self.statements:
                    statement.buildQuadruples()
            quadruples.append(['goto', t, None, goto.pop()])
            quadruples[gotof.pop()][3] = len(quadruples)
        
        if(self.type == 'display'):
            if(self.options and 'parameters' in self.options and self.options['parameters']):
                for expression in self.options['parameters']:
                    expression.buildQuadruples()
                    t = '[t'+ str(temporals) + ']'
                    quadruples.append(['display', t, None, None])
                quadruples.append(['enddisplay', None, None, None])


        # print(string + self.type + ': ' + self.identifier)
        # print('\t'+ string + 'Expression:')
        # for variable in self.variables:
        #     variable.print(indent + 2)


# variable = Variable('number', 'variableBonita1', 'ab+', None)
# variable1 = Variable('word', 'variableBonita2', 'ab+', None)
# variable2 = Variable('letter', 'variableBonita3', 'ab+', None)
# variable3 = Variable('flag', 'variableBonita4', 'ab+', None)
# variables = [variable, variable1, variable2, variable3]
# program = Program(variables, None, None)

# program.print()

# print(program.variables[0].identifier)

# def createVariableInTable(identifier, type, options, scope):
# 	for variables in variablesTable:
# 		if(variable.identifier == identifier and variable.scope == scope):
# 			return false
# 	variablesTable.push()


# program

# for variable in program.variables:
# 	if(variable.expression is not None):
# 		createVariableInTable(variable.identifier, variable.type, variable.options, 'global')

# for variable in program.main.variables:
# 	if(variable.expression is not None):
# 		createVariableInTable(variable.identifier, variable.type, variable.options, 'main')

# for block in program.blocks:
# 	if(block.variables is not None):
# 		for variable in block.variables:
# 			if(variable.expression is not None):
# 				createVariableInTable(variable.identifier, variable.type, variable.options, block.identifier)