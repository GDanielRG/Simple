def isConstant(string):
    if(string == 'numberconstant' or string == 'wordsconstant' or string == 'letterconstant' or string == 'flagconstant'):
        return True
    return False

class Program():
    def __init__(self, variables = {}, blocks = {}, main = None):
        self.variables = variables
        self.blocks = blocks
        self.main = main
        self.constants = {}

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

        # Global variables
        if(self.variables):
            for key, variable in self.variables.items():
                variable.createVariableReferences(globalVariables, {}, constants)

        # Main variables
        if(self.main.variables):
            for key, variable in self.main.variables.items():
                variable.createVariableReferences(globalVariables, {}, constants)

        mainVariables = self.main.variables

        # Main statements
        for statement in self.main.statements:
            statement.createVariableReferences(globalVariables, mainVariables, constants)
        
        
        # Blocks statements
        if(self.blocks):
            for key, block in self.blocks.items():
                blockVariables = block.variables
                for statement in block.statements:
                    statement.createVariableReferences(globalVariables, blockVariables, constants)
                
                for key, variable in block.variables.items():
                    variable.createVariableReferences(globalVariables, blockVariables, constants)
        
    def setValuesForVariables(self):
        for key, variable in self.variables.items():
            if(variable.expression):
                if(len(variable.expression.items) == 1 and isConstant(variable.expression.items[0].type)):
                    variable.value = variable.expression.items[0].value.value
        
        for key, variable in self.main.variables.items():
            if(variable.expression):
                if(len(variable.expression.items) == 1 and isConstant(variable.expression.items[0].type)):
                    variable.value = variable.expression.items[0].value.value
        
        for key, block in self.blocks.items():
            for key, variable in block.variables.items():
                if(variable.expression):
                    if(len(variable.expression.items) == 1 and isConstant(variable.expression.items[0].type)):
                        variable.value = variable.expression.items[0].value.value
            
                        

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
    
    def createVariableReferences(self, globalVariables, blockVariables, constants):
        if(self.options and 'arrayIndexes' in self.options and self.options['arrayIndexes']):
            expressions = self.options['arrayIndexes']
            for expression in expressions:
                expression.createVariableReferences(globalVariables, blockVariables, constants)
        if(self.expression):
            self.expression.createVariableReferences(globalVariables, blockVariables, constants)

        

class Expression():
    def __init__(self, lineNumber, items = list()):
        self.lineNumber = lineNumber
        self.items = items

    def print(self, indent = 0):
        string = ''
        for i in range(indent):
            string+='\t'
        if self.items:
            print(string + 'Expression items:')            
            for item in self.items:
                item.print(indent + 1)

    def printInline(self, indent = 0):
        string = ''
        for i in range(indent):
            string+='\t'
        if self.items:
            for item in self.items:
                string += str(item.value)
        print(string)
    
    def createVariableReferences(self, globalVariables, blockVariables, constants):
        for expressionItem in self.items:
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
            expressionItem.createVariableReferences(globalVariables, blockVariables, constants)

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
    
    def createVariableReferences(self, globalVariables, blockVariables, constants):
        if(self.options and 'arrayIndexes' in self.options and self.options['arrayIndexes']):
            expressions = self.options['arrayIndexes']
            for expression in expressions:
                expression.createVariableReferences(globalVariables, blockVariables, constants)
        
        if(self.options and 'parameters' in self.options and self.options['parameters']):
            for expression in self.options['parameters']:
                expression.createVariableReferences(globalVariables, blockVariables, constants)

class Block():
    def __init__(self, lineNumber, type = None, identifier = None, variables = None, parameters = list(), statements = list()):
        self.lineNumber = lineNumber
        self.type = type
        self.identifier = identifier
        self.variables = variables
        self.parameters = parameters
        self.statements = statements
    
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

# class Parameter():
#     def __init__(self, lineNumber, type, identifier):
#         self.lineNumber = lineNumber
#         self.type = type
#         self.identifier = identifier

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
        
        if(self.options and 'else' in self.options and self.options['else']):
            self.options['else'].print(indent + 1)
        
        if(self.options and 'variable' in self.options and self.options['variable']):
            self.options['variable'].print(indent + 1)


    def createVariableReferences(self, globalVariables, blockVariables, constants):
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
            self.options['else'].createVariableReferences(globalVariables, blockVariables, constants)

        if(self.expression):
            for expressionItem in self.expression.items:
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
                expressionItem.createVariableReferences(globalVariables, blockVariables, constants)
                
        
        if(self.statements):
            for statement in self.statements:
                statement.createVariableReferences(globalVariables, blockVariables, constants)
        
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
                    expression.createVariableReferences(globalVariables, blockVariables, constants)


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