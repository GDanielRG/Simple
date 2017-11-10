class Program():
    def __init__(self, variables = None, blocks = list(), main = None):
        self.variables = variables
        self.blocks = blocks
        self.main = main

    def print(self):
        print('Program:')
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

class Variable():
    def __init__(self, lineNumber, type = None, identifier = None, expression = None, options = None):
        self.lineNumber = lineNumber
        self.type = type
        self.identifier = identifier
        self.expression = expression
        self.options = options
    
    def print(self, indent = 0):
        string = ''
        for i in range(indent):
            string+='\t'
        print(string + self.type + ': ' + self.identifier + ' @' + str(self.lineNumber))
        if(self.options):
            print('\t' + string + 'Options: ' + str(self.options))

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
        print(string + self.type + ': ' + self.value)
        if(self.options):
            print('\t' + string + 'Options: ' + str(self.options))

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

        if(self.statements):
            print('\t'+ string + 'Statements:')
            for statement in self.statements:
                statement.print(indent + 2)

class Parameter():
    def __init__(self, lineNumber, type, identifier):
        self.lineNumber = lineNumber
        self.type = type
        self.identifier = identifier

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



    
