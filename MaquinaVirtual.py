import ParseTree
import simpleParser

result = simpleParser.result

#booleano en caso de que un error detenga el programa, empieza false
giveUp = False

# number a = 1;
# number b = 7;
# number c = a + 8;
# number z =  (a + b - b + c) * b / c

#creamos pila de memorias
memories = list()

#listas de cosas que imprimir
myResults = list()
errors = list()

#creamos el quadruplo principal
quadruples = []

#Creación de contador (apuntador) para cuadruplos
counter = 0

#Necesitare una pila de saltos para llamadas de función
callPSaltos = list()

#Tambien pueden haber casos donde el contador no avanza y envez se mueve
counterGo = True

#Creacion de lista que guarda el quadruple apuntado (opcional)
loadedQuadruple = []

#Antes de meter una memoria para el llamado de una funcion, la debemos almacenar
newMems = list()

#Requerimos de un contador para los parametros 
counterParams = list()

#y tambien necesitamos una pila que memorize la llave de los blocks que se llaman
keyParams = list()

#Pila para listas de iteradores
listasIterador = list()

#counterListasIterador
#counterListasIterador = list()

#creamos un diccionario con funciones
funDict = {}

#ahora recorremos todas las funciones 
for key, variable in result.blocks.items():
	funDict[variable.identifier] = ParseTree.Variable(None,variable.type,variable.identifier)

	

#Esta es la memoria de nuestro programa durante ejecución
memGlobal = {
	#Dividimos las variables con las temporales
	 'variables' : {**result.variables, **result.constants, **funDict},

     'temporals' : {

     }
    
 }


#for m in simpleParser.result.constants:
#	print(m)

memories.append(memGlobal)


#++++++++++++++++++++++++++++MOCK START++++++++++++++++++++++++++++

#ejemplo de cuadruplo generado (Fibonacci)

quadruples.append(['goto', None, None, '17']) #voy al main

quadruples.append(['<', 'a', '2.0', '[t1]']) #empieza condicion if
quadruples.append(['gotof', '[t1]',  None, '5']) 
quadruples.append(['return', 'a',  None, None]) #return
quadruples.append(['goto', None,  None, '17']) 
quadruples.append(['era', 'fibonacci', None, None]) #fibonacci(a-1)
quadruples.append(['-', 'a', '1.0','[t2]'])
quadruples.append(['param', '[t2]', None,'param1'])
quadruples.append(['gosub', 'fibonacci', None,'1']) #ir a quadruplo 2
quadruples.append(['=', 'fibonacci', None,'[t3]']) #t3 contiene fibonacci(a-1)
quadruples.append(['era', 'fibonacci', None, None]) #fibonacci(a-2)
quadruples.append(['-', 'a', '2.0','[t4]'])
quadruples.append(['param', '[t4]', None,'param1'])
quadruples.append(['gosub', 'fibonacci', None,'1']) #ir a quadruplo 2
quadruples.append(['=', 'fibonacci', None,'[t5]']) #t5 contiene fibonacci(a-2)
quadruples.append(['+', '[t3]', '[t5]', '[t6]']) #suma de fibonaccis
quadruples.append(['return', '[t6]', None,None]) #return

quadruples.append(['era', '[main]', None, None]) #enter the main
quadruples.append(['=', '7.0',  None, 'a'])
quadruples.append(['era', 'fibonacci', None, None]) #fibonacci(a)
quadruples.append(['param', 'a', None,'param1'])
quadruples.append(['gosub', 'fibonacci', None,'1']) #ir a quadruplo 2
quadruples.append(['=', 'fibonacci', None,'[t1]']) #t1 contiene fibonacci(a)
quadruples.append(['=', '[t1]', None,'a']) #t1 contiene fibonacci(a)
quadruples.append(['-', '5.0', '4.0','[t2]']) #expresion de xd[5-4]
quadruples.append(['ver', '[t2]', None, 'xd']) #verificar que [t2] (5-4) exista en xd
quadruples.append(['=', 'a', None, 'xd']) #xd[5-4] = a
quadruples.append(['end',None,None,None]) #finish


#ejemplo de cuadruplo generado (AreaPerimeter)

# quadruples.append(['era', '[main]', None, None])
# quadruples.append(['=', '3.0', None, 'width'])
# quadruples.append(['=', '4.0', None, 'height'])
# quadruples.append(['era', 'area', None, None])
# quadruples.append(['param', 'width', None, None])
# quadruples.append(['param', 'height', None, None])
# quadruples.append(['gosub', 'area', None,'19'])
# quadruples.append(['=', 'area', None,'[t1]'])
# quadruples.append(['=', '[t1]', None,'myArea'])
# quadruples.append(['era', 'perimeter', None, None])
# quadruples.append(['param', '3.0', None, None])
# quadruples.append(['param', 'height', None, None])
# quadruples.append(['gosub', 'perimeter', None,'16'])
# quadruples.append(['=', 'perimeter', None,'[t2]'])
# quadruples.append(['=', '[t2]', None,'myPerimeter'])
# quadruples.append(['end', None, None, None])
# quadruples.append(['+', 'h', 'w', '[t1]'])
# quadruples.append(['*', '2.0', '[t1]', '[t2]'])
# quadruples.append(['return', '[t2]', None, None])
# quadruples.append(['*', 'h', 'w', '[t1]'])
# quadruples.append(['return', '[t1]', None, None])




#++++++++++++++++++++++++++++MOCK FINISH++++++++++++++++++++++++++++


#Como alternativa al switch, definimos las funciones por separado

def f_end():
	global giveUp
	giveUp = True

def f_display():
	firstPositionMemories = len(memories) - 1

	if(isTemporal(quadruples[counter][1])):
		firstKey ="temporals"
	else:
		firstKey ="variables"
		if(not isLocal(quadruples[counter][1])):
			firstPositionMemories = 0

	myResults.append(memories[firstPositionMemories][firstKey][quadruples[counter][1]].value)


def f_ver():
	#formato cuadruplo 
	#['ver', 'r' (num iterador), None,'t'(key arreglo)]

	global listasIterador
	
	#revisar si el numero 'r' entra en el iterador 

	


def f_era():
	global newMems
	global counterParams
	global keyParams

	counterParam = 0

	#conseguir elemento #1 para buscar el key de la funcion
	#quadruples[counter][1]	

	#buscar objeto del block usando elemento #1

	if(isTemporal(quadruples[counter][1])):
		newMem = {
			'variables' : result.main.variables,

     		'temporals' : {}
		}
		memories.append(newMem)

	else:
		block = result.blocks[quadruples[counter][1]]
		#poner el nombre del block en la pila de llaves
		keyParams.append(quadruples[counter][1])

		varDict = {}
		
		#necesitamos clonar, no simplemente copiar variables, para nuestra nueva memoria local
		#recorremos todas las variables 
		for key, variable in block.variables.items():
			varDict[key] = ParseTree.Variable(variable.lineNumber,variable.type,variable.identifier,variable.expression,variable.options,variable.value)

		#creamos una nueva memoria para la pila
		newMem = {
		#Dividimos las variables locales con las temporales
		 'variables' : varDict,

	     'temporals' : {}
		}		
		#guardar nueva memoria y contador de parametros en sus pilas respectivas
		newMems.append(newMem)
		counterParams.append(counterParam)


def f_param():
	
	global counterParams
	global newMems

	positionMemories = len(memories) - 1

	#necesitamos apuntar al ultimo elemento de la pilas
	newMemsPosition = len(newMems) - 1
	counterParamPosition = len(counterParams) - 1
	keyParamPosition = len(keyParams) - 1

	#necesitamos obtener la key del parametro

	block = result.blocks[keyParams[keyParamPosition]]
	key = block.parameters[counterParams[counterParamPosition]].identifier
	print(key)

	#necesitamos saber si la expresion sale de una temporal o local
	if(isTemporal(quadruples[counter][1])):
		firstKey ="temporals"
	else:
		firstKey ="variables"
		if(not isLocal(quadruples[counter][1])):
			positionMemories = 0	

	print(counterParams)
	print(counterParams[counterParamPosition])
	print("En param, se la asignara el valor " + str(memories[positionMemories][firstKey][quadruples[counter][1]].value) + " de " + memories[positionMemories][firstKey][quadruples[counter][1]].identifier + "(en memoria " + str(positionMemories + 1) + ")" + " a " + newMems[newMemsPosition]['variables'][key].identifier)
	#despues necesitamos asignar la expresion que recibimos a la memoria
	print(memories[positionMemories][firstKey])
	newMems[newMemsPosition]['variables'][key].value = memories[positionMemories][firstKey][quadruples[counter][1]].value
	printMemories()
	#le sumamos uno al ultimo contador de la pila
	counterParams[counterParamPosition] += 1

def f_gosub():
	global counterGo
	global counter
	global callPSaltos
	global newMems

	positionMemories = len(memories) - 1
	newMemsPosition = len(newMems) - 1

	#poner el counter en el que estoy antes de irme a la otra funcion
	callPSaltos.append(counter)

	#metemos la ultima memoria local que creamos a la pila de memorias
	print(newMems)
	memories.append(newMems.pop())
	print(newMems)

	
	counter = int([quadruples[counter][3]][0])
	counterGo = False

	print("Saltamos al cuadruplo " + str(counter))

def f_return():
	global counterGo
	global counter

	keyParamPosition = len(keyParams) - 1
	PositionMemories = len(memories) - 1

	if(isTemporal(quadruples[counter][1])):
		firstKey ="temporals"
	else:
		firstKey ="variables"
		if(not isLocal(quadruples[counter][1])):
			PositionMemories = 0

	#almacenar expresion resultante en la variable global de la funcion
	memories[0]['variables'][keyParams[keyParamPosition]].value = memories[PositionMemories][firstKey][quadruples[counter][1]].value

	#remover la ultima llave de block y contador de parametro
	counterParams.pop()
	keyParams.pop()

	#evitar que el counter se incremente porque...
	counterGo = False
	#regresamos al quadruplo en que nos quedamos mas uno
	counter = callPSaltos.pop() + 1

	#y finalmente popiamos la memoria que ya no vamos a usar
	memories.pop()

def f_gotof():
	global counterGo
	global counter

	positionMemories = len(memories) - 1

	if(isTemporal(quadruples[counter][1])):
		firstKey ="temporals"
	else:
		firstKey ="variables"
		if(not isLocal(quadruples[counter][1])):
			positionMemories = 0			

	if not (memories[positionMemories][firstKey][quadruples[counter][1]].value):
		counter = int([quadruples[counter][3]][0])
		counterGo = False
		print("Fallo la condicion y se saltara al cuadruplo " + str(counter))


def f_gotov():
	global counterGo
	global counter

	positionMemories = len(memories) - 1

	if(isTemporal(quadruples[counter][1])):
		firstKey ="temporals"
	else:
		firstKey ="variables"
		if(not isLocal(quadruples[counter][1])):
			positionMemories = 0			

	if (memories[positionMemories][firstKey][quadruples[counter][1]].value):
		counter = int([quadruples[counter][3]][0])
		counterGo = False
		print("la condicion fue un exito y se saltara al cuadruplo " + str(counter))

def f_goto():
	global counterGo
	global counter

	counter = int([quadruples[counter][3]][0])
	counterGo = False
	print("Se saltara al cuadruplo " + str(counter))

def f_equality():

	firstPositionMemories = len(memories) - 1
	secondPositionMemories = len(memories) - 1
	thirdPositionMemories = len(memories) - 1

	if(isTemporal(quadruples[counter][1])):
		firstKey ="temporals"
	else:
		firstKey ="variables"
		if(not isLocal(quadruples[counter][1])):
			firstPositionMemories = 0

	if(isTemporal(quadruples[counter][2])):
		secondKey ="temporals"
	else:
		secondKey ="variables"
		if(not isLocal(quadruples[counter][2])):
			secondPositionMemories = 0

	if(isTemporal(quadruples[counter][3])):
		thirdKey ="temporals"
	else:
		thirdKey ="variables"
		if(not isLocal(quadruples[counter][3])):
			thirdPositionMemories = 0

	memories[thirdPositionMemories][thirdKey][quadruples[counter][3]] = ParseTree.Variable(0,"flag",quadruples[counter][3],None,None, None)
	memories[thirdPositionMemories][thirdKey][quadruples[counter][3]].value = memories[firstPositionMemories][firstKey][quadruples[counter][1]].value is memories[secondPositionMemories][secondKey][quadruples[counter][2]].value
	printMemories()

def f_and():

	firstPositionMemories = len(memories) - 1
	secondPositionMemories = len(memories) - 1
	thirdPositionMemories = len(memories) - 1

	if(isTemporal(quadruples[counter][1])):
		firstKey ="temporals"
	else:
		firstKey ="variables"
		if(not isLocal(quadruples[counter][1])):
			firstPositionMemories = 0

	if(isTemporal(quadruples[counter][2])):
		secondKey ="temporals"
	else:
		secondKey ="variables"
		if(not isLocal(quadruples[counter][2])):
			secondPositionMemories = 0

	if(isTemporal(quadruples[counter][3])):
		thirdKey ="temporals"
	else:
		thirdKey ="variables"
		if(not isLocal(quadruples[counter][3])):
			thirdPositionMemories = 0

	memories[thirdPositionMemories][thirdKey][quadruples[counter][3]] = ParseTree.Variable(0,"flag",quadruples[counter][3],None,None, None)
	memories[thirdPositionMemories][thirdKey][quadruples[counter][3]].value = memories[firstPositionMemories][firstKey][quadruples[counter][1]].value and memories[secondPositionMemories][secondKey][quadruples[counter][2]].value
	printMemories()

def f_or():

	firstPositionMemories = len(memories) - 1
	secondPositionMemories = len(memories) - 1
	thirdPositionMemories = len(memories) - 1

	if(isTemporal(quadruples[counter][1])):
		firstKey ="temporals"
	else:
		firstKey ="variables"
		if(not isLocal(quadruples[counter][1])):
			firstPositionMemories = 0

	if(isTemporal(quadruples[counter][2])):
		secondKey ="temporals"
	else:
		secondKey ="variables"
		if(not isLocal(quadruples[counter][2])):
			secondPositionMemories = 0

	if(isTemporal(quadruples[counter][3])):
		thirdKey ="temporals"
	else:
		thirdKey ="variables"
		if(not isLocal(quadruples[counter][3])):
			thirdPositionMemories = 0

	memories[thirdPositionMemories][thirdKey][quadruples[counter][3]] = ParseTree.Variable(0,"flag",quadruples[counter][3],None,None, None)
	memories[thirdPositionMemories][thirdKey][quadruples[counter][3]].value = memories[firstPositionMemories][firstKey][quadruples[counter][1]].value or memories[secondPositionMemories][secondKey][quadruples[counter][2]].value
	printMemories()

def f_not():

	thirdPositionMemories = len(memories) - 1

	if(isTemporal(quadruples[counter][3])):
		thirdKey ="temporals"
	else:
		thirdKey ="variables"
		if(not isLocal(quadruples[counter][3])):
			thirdPositionMemories = 0

	memories[thirdPositionMemories][thirdKey][quadruples[counter][3]].value = not memories[thirdPositionMemories][thirdKey][quadruples[counter][3]].value 
	printMemories()

def f_greater():

	firstPositionMemories = len(memories) - 1
	secondPositionMemories = len(memories) - 1
	thirdPositionMemories = len(memories) - 1

	if(isTemporal(quadruples[counter][1])):
		firstKey ="temporals"
	else:
		firstKey ="variables"
		if(not isLocal(quadruples[counter][1])):
			firstPositionMemories = 0

	if(isTemporal(quadruples[counter][2])):
		secondKey ="temporals"
	else:
		secondKey ="variables"
		if(not isLocal(quadruples[counter][2])):
			secondPositionMemories = 0

	if(isTemporal(quadruples[counter][3])):
		thirdKey ="temporals"
	else:
		thirdKey ="variables"
		if(not isLocal(quadruples[counter][3])):
			thirdPositionMemories = 0

	memories[thirdPositionMemories][thirdKey][quadruples[counter][3]] = ParseTree.Variable(0,"flag",quadruples[counter][3],None,None, None)
	memories[thirdPositionMemories][thirdKey][quadruples[counter][3]].value = memories[firstPositionMemories][firstKey][quadruples[counter][1]].value > memories[secondPositionMemories][secondKey][quadruples[counter][2]].value
	printMemories()

def f_lesser():

	firstPositionMemories = len(memories) - 1
	secondPositionMemories = len(memories) - 1
	thirdPositionMemories = len(memories) - 1

	if(isTemporal(quadruples[counter][1])):
		firstKey ="temporals"
	else:
		firstKey ="variables"
		if(not isLocal(quadruples[counter][1])):
			firstPositionMemories = 0

	if(isTemporal(quadruples[counter][2])):
		secondKey ="temporals"
	else:
		secondKey ="variables"
		if(not isLocal(quadruples[counter][2])):
			secondPositionMemories = 0

	if(isTemporal(quadruples[counter][3])):
		thirdKey ="temporals"
	else:
		thirdKey ="variables"
		if(not isLocal(quadruples[counter][3])):
			thirdPositionMemories = 0

	memories[thirdPositionMemories][thirdKey][quadruples[counter][3]] = ParseTree.Variable(0,"flag",quadruples[counter][3],None,None, None)
	memories[thirdPositionMemories][thirdKey][quadruples[counter][3]].value = memories[firstPositionMemories][firstKey][quadruples[counter][1]].value < memories[secondPositionMemories][secondKey][quadruples[counter][2]].value
	printMemories()

def f_plus():

	firstPositionMemories = len(memories) - 1
	secondPositionMemories = len(memories) - 1
	thirdPositionMemories = len(memories) - 1

	if(isTemporal(quadruples[counter][1])):
		firstKey ="temporals"
	else:
		firstKey ="variables"
		if(not isLocal(quadruples[counter][1])):
			firstPositionMemories = 0

	if(isTemporal(quadruples[counter][2])):
		secondKey ="temporals"
	else:
		secondKey ="variables"
		if(not isLocal(quadruples[counter][2])):
			secondPositionMemories = 0


	if(isTemporal(quadruples[counter][3])):
		#si el tercero es temporal (en una suma no deberia serlo)
		thirdKey ="temporals"
	else:
		thirdKey ="variables"
		if(not isLocal(quadruples[counter][3])):
			thirdPositionMemories = 0

	memories[thirdPositionMemories][thirdKey][quadruples[counter][3]] = ParseTree.Variable(0,"number",quadruples[counter][3],None,None, None)
	memories[thirdPositionMemories][thirdKey][quadruples[counter][3]].value = memories[firstPositionMemories][firstKey][quadruples[counter][1]].value + memories[secondPositionMemories][secondKey][quadruples[counter][2]].value
	printMemories()
	
def f_minus():

	firstPositionMemories = len(memories) - 1
	secondPositionMemories = len(memories) - 1
	thirdPositionMemories = len(memories) - 1

	if(isTemporal(quadruples[counter][1])):
		firstKey ="temporals"
	else:
		firstKey ="variables"
		if(not isLocal(quadruples[counter][1])):
			firstPositionMemories = 0

	if(isTemporal(quadruples[counter][2])):
		secondKey ="temporals"
	else:
		secondKey ="variables"
		if(not isLocal(quadruples[counter][2])):
			secondPositionMemories = 0

	if(isTemporal(quadruples[counter][3])):
		thirdKey ="temporals"
	else:
		thirdKey ="variables"
		if(not isLocal(quadruples[counter][3])):
			thirdPositionMemories = 0

	memories[thirdPositionMemories][thirdKey][quadruples[counter][3]] = ParseTree.Variable(0,"number",quadruples[counter][3],None,None, None)
	memories[thirdPositionMemories][thirdKey][quadruples[counter][3]].value = memories[firstPositionMemories][firstKey][quadruples[counter][1]].value - memories[secondPositionMemories][secondKey][quadruples[counter][2]].value
	print("Restamos la " + quadruples[counter][1] + " en memoria " + str(firstPositionMemories + 1) + " con la variable " + quadruples[counter][2] + " en memoria " + str(thirdPositionMemories + 1))
	printMemories()

def f_multiplication():

	firstPositionMemories = len(memories) - 1
	secondPositionMemories = len(memories) - 1
	thirdPositionMemories = len(memories) - 1

	if(isTemporal(quadruples[counter][1])):
		firstKey ="temporals"
	else:
		firstKey ="variables"
		if(not isLocal(quadruples[counter][1])):
			firstPositionMemories = 0

	if(isTemporal(quadruples[counter][2])):
		secondKey ="temporals"
	else:
		secondKey ="variables"
		if(not isLocal(quadruples[counter][2])):
			secondPositionMemories = 0

	if(isTemporal(quadruples[counter][3])):
		thirdKey ="temporals"
	else:
		thirdKey ="variables"
		if(not isLocal(quadruples[counter][3])):
			thirdPositionMemories = 0

	memories[thirdPositionMemories][thirdKey][quadruples[counter][3]] = ParseTree.Variable(0,"number",quadruples[counter][3],None,None, None)
	memories[thirdPositionMemories][thirdKey][quadruples[counter][3]].value = memories[firstPositionMemories][firstKey][quadruples[counter][1]].value * memories[secondPositionMemories][secondKey][quadruples[counter][2]].value
	printMemories()

def f_division():
	
	firstPositionMemories = len(memories) - 1
	secondPositionMemories = len(memories) - 1
	thirdPositionMemories = len(memories) - 1

	if(isTemporal(quadruples[counter][1])):
		firstKey ="temporals"
	else:
		firstKey ="variables"
		if(not isLocal(quadruples[counter][1])):
			firstPositionMemories = 0

	if(isTemporal(quadruples[counter][2])):
		secondKey ="temporals"
	else:
		secondKey ="variables"
		if(not isLocal(quadruples[counter][2])):
			secondPositionMemories = 0

	if(isTemporal(quadruples[counter][3])):
		thirdKey ="temporals"
	else:
		thirdKey ="variables"
		if(not isLocal(quadruples[counter][3])):
			thirdPositionMemories = 0

	memories[thirdPositionMemories][thirdKey][quadruples[counter][3]] = ParseTree.Variable(0,"number",quadruples[counter][3],None,None, None)
	memories[thirdPositionMemories][thirdKey][quadruples[counter][3]].value = memories[firstPositionMemories][firstKey][quadruples[counter][1]].value / memories[secondPositionMemories][secondKey][quadruples[counter][2]].value
	printMemories()

def f_modulus():
	
	firstPositionMemories = len(memories) - 1
	secondPositionMemories = len(memories) - 1
	thirdPositionMemories = len(memories) - 1

	if(isTemporal(quadruples[counter][1])):
		firstKey ="temporals"
	else:
		firstKey ="variables"
		if(not isLocal(quadruples[counter][1])):
			firstPositionMemories = 0

	if(isTemporal(quadruples[counter][2])):
		secondKey ="temporals"
	else:
		secondKey ="variables"
		if(not isLocal(quadruples[counter][2])):
			secondPositionMemories = 0

	if(isTemporal(quadruples[counter][3])):
		thirdKey ="temporals"
	else:
		thirdKey ="variables"
		if(not isLocal(quadruples[counter][3])):
			thirdPositionMemories = 0

	memories[thirdPositionMemories][thirdKey][quadruples[counter][3]] = ParseTree.Variable(0,"number",quadruples[counter][3],None,None, None)
	memories[thirdPositionMemories][thirdKey][quadruples[counter][3]].value = memories[firstPositionMemories][firstKey][quadruples[counter][1]].value % memories[secondPositionMemories][secondKey][quadruples[counter][2]].value
	printMemories()

def f_assign():

	listasIteradorPosition = len(listasIterador) - 1


	firstPositionMemories = len(memories) - 1
	thirdPositionMemories = len(memories) - 1

	#Variables que se guardan, si recibo una matriz o no
	firstVariableObj = None
	secondVariableObj = None
	thirdVariableObj = None

	if(isTemporal(quadruples[counter][1])):
		firstKey ="temporals"
	else:
		firstKey ="variables"
		if(not isLocal(quadruples[counter][1])):
			firstPositionMemories = 0

	#revisar si el valor 1 del quadruplo es arreglo/matriz
	#aqui empieza el infierno de ifs
	if isArray(memories[firstPositionMemories][firstKey][quadruples[counter][1]]) :
		print(memories[firstPositionMemories][firstKey][quadruples[counter][1]].identifier)
		if()
		

	if(isTemporal(quadruples[counter][3])):
		thirdKey ="temporals"
		if not quadruples[counter][3] in memories[thirdPositionMemories][thirdKey]:
			memories[thirdPositionMemories][thirdKey][quadruples[counter][3]] = ParseTree.Variable(None,memories[firstPositionMemories][firstKey][quadruples[counter][1]].type,quadruples[counter][3])

	else:
		thirdKey ="variables"
		if(not isLocal(quadruples[counter][3])):
			thirdPositionMemories = 0
	
	#revisar si el valor 3 del quadruplo es arreglo/matriz
	if isArray(memories[thirdPositionMemories][thirdKey][quadruples[counter][3]]) :
		print(memories[thirdPositionMemories][thirdKey][quadruples[counter][3]].identifier)

	memories[thirdPositionMemories][thirdKey][quadruples[counter][3]].value = memories[firstPositionMemories][firstKey][quadruples[counter][1]].value
	printMemories()


#una vez que declaramos todas las funciones del "switch" 
options = { #expresiones
			'+': f_plus,
		   '-': f_minus,
		   '*': f_multiplication,
		   '/': f_division,
		   '%' : f_modulus,
		   '=': f_assign,
		   '==': f_equality,
		   '>': f_greater,
		   '<': f_lesser,
		   'and': f_and,
		   'or' : f_or,
		   'not' : f_not,
		   #ciclos if y while
		   'gotof' : f_gotof,
		   'gotov' : f_gotov,
		   'goto' : f_goto,
		   #llamado de funciones
		   'gosub' : f_gosub,
		   'era' : f_era,
		   'param' : f_param,
		   'return' : f_return,
		   #verificacion de arreglo/matriz
		   'ver' : f_ver,
		   #si acaba el programa
		   'end' : f_end
}

#funcion para revisar si una variable esta en memoria local o global
def isLocal(expression):
	if(expression in memories[len(memories)-1]['variables']):
		print(str(expression) + " esta en memoria local")
		return True
	if(expression in memories[0]['variables']):
		print(str(expression) + " esta en memoria global")
		return False
	print("expression " +  str(expression) + " not found in memory, help!")
	return False


#adicionalmente necesitamos funciones que se ejecutan si la variable el temporal o no
def isTemporal(expression):
	if(expression[0] == "[" and expression[len(expression)-1] == "]"):
		return True
	return False

#necesitamos un check especial para constantes
def isConstant(expresion):
	if(expresion.find('.') != -1):
		print("expresion no es constante")
		return False
	else:
		return True

def isArray(expresionItem):
	if(expresionItem.type == "manynumbers"):
		print("aaa.. " + expresionItem.identifier + " es un arreglo")
		return True
	else:
		return False

def printMemories():

	count = 1
	stringCollectorvariables = ""
	stringCollectortemporals = ""
	for memory in memories:
		print("Memory # " + str(count))
		print("\t" + "Variables")
		for key, variable in memory['variables'].items():
			if (stringCollectorvariables is ""):
				stringCollectorvariables = variable.identifier + ": " + str(variable.value)
			else:
				stringCollectorvariables += ", " + variable.identifier + ": " + str(variable.value)
		print("\t" + "\t" + stringCollectorvariables)
		print("\t" + "Temporals")
		for key, variable in memory['temporals'].items():
			if (stringCollectortemporals is ""):
				stringCollectortemporals = variable.identifier + ": " + str(variable.value)
			else:
				stringCollectortemporals += ", " + variable.identifier + ": " + str(variable.value)
		print("\t" + "\t" + stringCollectortemporals)
		count += 1
		stringCollectorvariables = ""
		stringCollectortemporals = ""



while counter < len(quadruples):
	if(not giveUp):
		counterGo = True
		print("-------------")
		print(quadruples[counter])
		options[quadruples[counter][0]]()
		if(counterGo):
			counter = counter + 1
	else:
		break
pass

# mem['t2'] = mem['a'] + mem[8]
# .....
# .....
# mem['z'] = mem['t6']