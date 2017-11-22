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
temporalResultContainer = ""
errorS = ""

#creamos el quadruplo principal
quadruples = simpleParser.quadruples
for quadruple in quadruples:
	print(quadruple)
for key, block in result.blocks.items():
	print('Nuevo meme: ' + str(block.firstQuadruple))
	

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

#Fila para listas de iteradores
FilaListasIterador = list()

#lista temporal en lo que danielito implementa bien arrayIndexes
arrayIndexTemporal = list()

#Guardar Lista de iterador temporal
ListaIterador = list()

#booleano que solo permite la creacion de una lista de iteradores si esta activa
crearListaIterador = True

#counterVerifyIterador
counterVerifyIterador = 0

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

# quadruples.append(['goto', None, None, '17']) #voy al main

# quadruples.append(['<', 'a', '2.0', '[t1]']) #empieza condicion if
# quadruples.append(['gotof', '[t1]',  None, '5']) 
# quadruples.append(['return', 'a',  None, None]) #return
# quadruples.append(['goto', None,  None, '17']) 
# quadruples.append(['era', 'fibonacci', None, None]) #fibonacci(a-1)
# quadruples.append(['-', 'a', '1.0','[t2]'])
# quadruples.append(['param', '[t2]', None,'param1'])
# quadruples.append(['gosub', 'fibonacci', None,'1']) #ir a quadruplo 2
# quadruples.append(['=', 'fibonacci', None,'[t3]']) #t3 contiene fibonacci(a-1)
# quadruples.append(['era', 'fibonacci', None, None]) #fibonacci(a-2)
# quadruples.append(['-', 'a', '2.0','[t4]'])
# quadruples.append(['param', '[t4]', None,'param1'])
# quadruples.append(['gosub', 'fibonacci', None,'1']) #ir a quadruplo 2
# quadruples.append(['=', 'fibonacci', None,'[t5]']) #t5 contiene fibonacci(a-2)
# quadruples.append(['+', '[t3]', '[t5]', '[t6]']) #suma de fibonaccis
# quadruples.append(['return', '[t6]', None,None]) #return

# quadruples.append(['era', '[main]', None, None]) #enter the main
# quadruples.append(['=', '7.0',  None, 'a'])
# quadruples.append(['era', 'fibonacci', None, None]) #fibonacci(a)
# quadruples.append(['param', 'a', None,'param1'])
# quadruples.append(['gosub', 'fibonacci', None,'1']) #ir a quadruplo 2
# quadruples.append(['=', 'fibonacci', None,'[t1]']) #t1 contiene fibonacci(a)
# quadruples.append(['=', '[t1]', None,'a']) #t1 contiene fibonacci(a)
# quadruples.append(['-', '5.0', '4.0','[t2]']) #expresion de xd[5-4]
# quadruples.append(['ver', '[t2]', None, 'xd']) #verificar que [t2] (5-4) exista en xd en dimension 1
# quadruples.append(['endver', None, None, None]) #verificacion acaba, guardar 
# quadruples.append(['=', 'a', None, 'xd']) #xd[5-4] = a

# quadruples.append(['ver', '2.0', None, 'xd']) #verificar que 2 exista en xd
# quadruples.append(['endver', None, None, None]) #verificacion acaba
# quadruples.append(['=', '2.0', None, 'xd']) #xd[2] = 2

# quadruples.append(['-', '5.0', '4.0','[t3]']) #expresion de xd[5-4]
# quadruples.append(['ver', '[t3]', None, 'xd']) #verificar que 2 exista en xd
# quadruples.append(['endver', None, None, None]) #verificacion acaba


# quadruples.append(['ver', '2.0', None, 'xd']) #verificar que 2 exista en xd
# quadruples.append(['endver', None, None, None]) #verificacion acaba

# quadruples.append(['-', 'xd', 'xd', '[t4]']) #suma de xd[5-4] + xd[2]
# quadruples.append(['=', '[t4]', None, 'a']) #suma igual a a
# #37

# quadruples.append(['-', '5.0', '4.0','[t5]']) #expresion de xd[5-4] #38
# quadruples.append(['ver', '[t5]', None, 'xd']) #verificar que 2 exista en xd
# quadruples.append(['endver', None, None, None]) #verificacion acaba

# quadruples.append(['ver', '2.0', None, 'xd']) #verificar que 2 exista en xd
# quadruples.append(['endver', None, None, None]) #verificacion acaba

# quadruples.append(['<', 'xd', 'xd', '[t6]']) #comparacion de xd[5-4] > xd[2]
# quadruples.append(['gotof', '[t6]', None,'48']) #ir a quadruplo 48

# quadruples.append(['ver', '3.0', None, 'xd']) #verificar que 2 exista en xd
# quadruples.append(['endver', None, None, None]) #verificacion acaba

# quadruples.append(['=', '420.0', None, 'xd']) #xd[3] = 420


# quadruples.append(['end',None,None,None]) #finish


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
	global arrayIndexTemporal
	global temporalResultContainer

	#NECESITAMOS una referencia al objeto final
	thirdVariable = None
	#valor final a usar en ecuacion
	firstValue = None

	#variables reservadas para offsets en caso de arreglos
	firstOffset = None
	thirdOffset = None

	firstPositionMemories = len(memories) - 1
	thirdPositionMemories = len(memories) - 1

	if(isTemporal(quadruples[counter][1])):
		firstKey ="temporals"
		firstValue = memories[firstPositionMemories][firstKey][quadruples[counter][1]].value
	else:
		firstKey ="variables"
		if(not isLocal(quadruples[counter][1])):
			firstPositionMemories = 0
		#Hay que ver si estamos lidiando con un arreglo o no
		if(isArray(memories[firstPositionMemories][firstKey][quadruples[counter][1]])):
			#empieza lo bueno
			#hay que obtener la direccion resultante para sacar el value que necesitamos del arreglo aplanado
			
			#TEMPORAL EN LO QUE DANIELITO PONE BIEN LOS ARRAYINDEXES
			contadorTemporal = 0
			for key in memories[firstPositionMemories][firstKey][quadruples[counter][1]].options['arrayIndexes']:
				#.options['arrayIndexes'][counterVerifyIterador].items[0].value.value
				arrayIndexTemporal.append(memories[firstPositionMemories][firstKey][quadruples[counter][1]].options['arrayIndexes'][contadorTemporal].items[0].value.value)
				contadorTemporal += 1
			
			#FIN TEMPORALES

			#vamos a necesitar el offsetValue para firstValue
			firstOffset = offsetCalculator(arrayIndexTemporal)

			#vaciar arrayIndexTemporal
			arrayIndexTemporal = list()

			#finalmente le asignamos el elemento del arreglo a firstValue
			firstValue = memories[firstPositionMemories][firstKey][quadruples[counter][1]].value[firstOffset]

		else:
			#si no es array, sacamos el valor directamente
			firstValue = memories[firstPositionMemories][firstKey][quadruples[counter][1]].value

	print("firstValue es " + str(firstValue))
	stringTemp = ""
	#si es un string
	stringTemp = str(firstValue)

	if(isinstance(firstValue,str)):
		if(str(firstValue[0]) is '"'):
			print("mememe")
			stringTemp = str(firstValue.replace('"',""))

	temporalResultContainer += stringTemp
	print(temporalResultContainer)
	
def f_enddisplay():
	
	global myResults
	global temporalResultContainer

	myResults.append(temporalResultContainer)
	temporalResultContainer = ""
	print(myResults)

def f_ver():
	#formato cuadruplo 
	#['ver', 'r' (num iterador), None,'t'(key arreglo)]
	
	global giveUp
	global errorS
	global ListaIterador

#primero creamos parametros para detectar donde esta la key del arreglo
	firstPositionMemories = len(memories) - 1
	thirdPositionMemories = len(memories) - 1

	if(isTemporal(quadruples[counter][1])):
		firstKey ="temporals"
	else:
		firstKey ="variables"
		if(not isLocal(quadruples[counter][1])):
			firstPositionMemories = 0


	if(isTemporal(quadruples[counter][3])):
		thirdKey ="temporals"
	else:
		thirdKey ="variables"
		if(not isLocal(quadruples[counter][3])):
			thirdPositionMemories = 0

	#Aqui se encuentran los arrayIndexes de nuestra memoria 
	#memories[PositionMemories][thirdKey][quadruples[counter][1]].options['arrayIndexes']

	#necesitaremos un contador global , el cual se hara 0 en endver
	global counterVerifyIterador
	#print(memories[thirdPositionMemories][thirdKey][quadruples[counter][3]].options['arrayIndexes'][counterVerifyIterador])
	print(memories[thirdPositionMemories][thirdKey][quadruples[counter][3]].options['arrayIndexes'][counterVerifyIterador].items[0].value.value)

 	#insertamos el iterador a la lista de iteradores actual
	ListaIterador.append(int(memories[firstPositionMemories][firstKey][quadruples[counter][1]].value)-1)


	#comparar numero de arrayIndex[counter] con r(num iterador)
	if (int(memories[firstPositionMemories][firstKey][quadruples[counter][1]].value) > 0 and int(memories[firstPositionMemories][firstKey][quadruples[counter][1]].value) <= memories[thirdPositionMemories][thirdKey][quadruples[counter][3]].options['arrayIndexes'][counterVerifyIterador].items[0].value.value):
		print ("good")
	else:
		print("IIIIN THE AAAAAARMS")
		#ver si no es una constante
		ts = ""
		if(memories[firstPositionMemories][firstKey][quadruples[counter][1]].value is not quadruples[counter][1]):
			ts = "(" + str(memories[firstPositionMemories][firstKey][quadruples[counter][1]].value) + ")"

		#crear error
		errorS = str(memories[firstPositionMemories][firstKey][quadruples[counter][1]].identifier) + ts + " is out of bounds in array " + str(memories[thirdPositionMemories][thirdKey][quadruples[counter][3]].identifier);
		giveUp = True
	
	#SUMAR contador de verify
	counterVerifyIterador += 1



def f_endver():
	#formato cuadruplo 
	#['ver', None, None,None]

	global ListaIterador
	global FilaListasIterador

	#hay que vaciar ListaIterador despues de guardarla en FilaListasIterador
	FilaListasIterador.append(ListaIterador)
	print(ListaIterador)
	ListaIterador = list()

	#el contador global se hara 0 aqui 
	global counterVerifyIterador
	counterVerifyIterador = 0
	

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

	global arrayIndexTemporal
	global giveUp
	global errorS

	#NECESITAMOS una referencia al objeto final
	thirdVariable = None
	#valor final a usar en ecuacion
	firstValue = None
	secondValue = None

	#variables reservadas para offsets en caso de arreglos
	firstOffset = None
	secondOffset = None
	thirdOffset = None

	firstPositionMemories = len(memories) - 1
	secondPositionMemories = len(memories) - 1
	thirdPositionMemories = len(memories) - 1

	if(isTemporal(quadruples[counter][1])):
		firstKey ="temporals"
		firstValue = memories[firstPositionMemories][firstKey][quadruples[counter][1]].value
	else:
		firstKey ="variables"
		if(not isLocal(quadruples[counter][1])):
			firstPositionMemories = 0
		#Hay que ver si estamos lidiando con un arreglo o no
		if(isArray(memories[firstPositionMemories][firstKey][quadruples[counter][1]])):
			#empieza lo bueno
			#hay que obtener la direccion resultante para sacar el value que necesitamos del arreglo aplanado
			
			#
			contadorTemporal = 0
			for key in memories[firstPositionMemories][firstKey][quadruples[counter][1]].options['arrayIndexes']:
				#.options['arrayIndexes'][counterVerifyIterador].items[0].value.value
				arrayIndexTemporal.append(memories[firstPositionMemories][firstKey][quadruples[counter][1]].options['arrayIndexes'][contadorTemporal].items[0].value.value)
				contadorTemporal += 1
			
			#FIN 

			#vamos a necesitar el offsetValue para firstValue
			firstOffset = offsetCalculator(arrayIndexTemporal)

			#vaciar arrayIndexTemporal
			arrayIndexTemporal = list()

			#finalmente le asignamos el elemento del arreglo a firstValue
			firstValue = memories[firstPositionMemories][firstKey][quadruples[counter][1]].value[firstOffset]

		else:
			#si no es array, sacamos el valor directamente
			firstValue = memories[firstPositionMemories][firstKey][quadruples[counter][1]].value

	if(isTemporal(quadruples[counter][2])):
		secondKey ="temporals"
		secondValue = memories[secondPositionMemories][secondKey][quadruples[counter][2]].value
	else:
		secondKey ="variables"
		if(not isLocal(quadruples[counter][2])):
			secondPositionMemories = 0
		#Hay que ver si estamos lidiando con un arreglo o no
		if(isArray(memories[secondPositionMemories][secondKey][quadruples[counter][2]])):
			#empieza lo bueno
			#hay que obtener la direccion resultante para sacar el value que necesitamos del arreglo aplanado
			
			#
			contadorTemporal = 0
			for key in memories[secondPositionMemories][secondKey][quadruples[counter][2]].options['arrayIndexes']:
				#.options['arrayIndexes'][counterVerifyIterador].items[0].value.value
				arrayIndexTemporal.append(memories[secondPositionMemories][secondKey][quadruples[counter][2]].options['arrayIndexes'][contadorTemporal].items[0].value.value)
				contadorTemporal += 1
			
			#FIN 

			#vamos a necesitar el offsetValue para firstValue
			secondOffset = offsetCalculator(arrayIndexTemporal)

			#vaciar arrayIndexTemporal
			arrayIndexTemporal = list()

			#finalmente le asignamos el elemento del arreglo a firstValue
			secondValue = memories[secondPositionMemories][secondKey][quadruples[counter][2]].value[secondOffset]

		else:
			#si no es array, sacamos el valor directamente
			secondValue = memories[secondPositionMemories][secondKey][quadruples[counter][2]].value


	if(isTemporal(quadruples[counter][3])):
		#si el tercero es temporal (en una suma no deberia serlo)
		thirdKey ="temporals"
		memories[thirdPositionMemories][thirdKey][quadruples[counter][3]] = ParseTree.Variable(0,"flag",quadruples[counter][3],None,None, None)
		thirdVariable = memories[thirdPositionMemories][thirdKey][quadruples[counter][3]]
	else:
		thirdKey ="variables"
		if(not isLocal(quadruples[counter][3])):
			thirdPositionMemories = 0
		#sin importar lo que pase igual vamos a recibir el objeto expression
		thirdVariable = memories[thirdPositionMemories][thirdKey][quadruples[counter][3]]

	#thirdVariable = ParseTree.Variable(0,"number",quadruples[counter][3],None,None, None)

	#checar si un elemento esta vacio
	if (firstValue is None):
		#crear error
		
		errorS = str(memories[firstPositionMemories][firstKey][quadruples[counter][1]].identifier) +  " is trying to be used when it's empty."
		giveUp = True
		return

	if (secondValue is None):
		#crear error
		errorS = str(memories[secondPositionMemories][secondKey][quadruples[counter][2]].identifier) +  " is trying to be used when it's empty."
		giveUp = True
		return

	#ecuación final
	#memories[thirdPositionMemories][thirdKey][quadruples[counter][3]].value = memories[firstPositionMemories][firstKey][quadruples[counter][1]].value + memories[secondPositionMemories][secondKey][quadruples[counter][2]].value
	thirdVariable.value = firstValue is secondValue

	printMemories()

def f_and():

	global arrayIndexTemporal
	global giveUp
	global errorS

	#NECESITAMOS una referencia al objeto final
	thirdVariable = None
	#valor final a usar en ecuacion
	firstValue = None
	secondValue = None

	#variables reservadas para offsets en caso de arreglos
	firstOffset = None
	secondOffset = None
	thirdOffset = None

	firstPositionMemories = len(memories) - 1
	secondPositionMemories = len(memories) - 1
	thirdPositionMemories = len(memories) - 1

	if(isTemporal(quadruples[counter][1])):
		firstKey ="temporals"
		firstValue = memories[firstPositionMemories][firstKey][quadruples[counter][1]].value
	else:
		firstKey ="variables"
		if(not isLocal(quadruples[counter][1])):
			firstPositionMemories = 0
		#Hay que ver si estamos lidiando con un arreglo o no
		if(isArray(memories[firstPositionMemories][firstKey][quadruples[counter][1]])):
			#empieza lo bueno
			#hay que obtener la direccion resultante para sacar el value que necesitamos del arreglo aplanado
			
			#
			contadorTemporal = 0
			for key in memories[firstPositionMemories][firstKey][quadruples[counter][1]].options['arrayIndexes']:
				#.options['arrayIndexes'][counterVerifyIterador].items[0].value.value
				arrayIndexTemporal.append(memories[firstPositionMemories][firstKey][quadruples[counter][1]].options['arrayIndexes'][contadorTemporal].items[0].value.value)
				contadorTemporal += 1
			
			#FIN 

			#vamos a necesitar el offsetValue para firstValue
			firstOffset = offsetCalculator(arrayIndexTemporal)

			#vaciar arrayIndexTemporal
			arrayIndexTemporal = list()

			#finalmente le asignamos el elemento del arreglo a firstValue
			firstValue = memories[firstPositionMemories][firstKey][quadruples[counter][1]].value[firstOffset]

		else:
			#si no es array, sacamos el valor directamente
			firstValue = memories[firstPositionMemories][firstKey][quadruples[counter][1]].value

	if(isTemporal(quadruples[counter][2])):
		secondKey ="temporals"
		secondValue = memories[secondPositionMemories][secondKey][quadruples[counter][2]].value
	else:
		secondKey ="variables"
		if(not isLocal(quadruples[counter][2])):
			secondPositionMemories = 0
		#Hay que ver si estamos lidiando con un arreglo o no
		if(isArray(memories[secondPositionMemories][secondKey][quadruples[counter][2]])):
			#empieza lo bueno
			#hay que obtener la direccion resultante para sacar el value que necesitamos del arreglo aplanado
			
			#
			contadorTemporal = 0
			for key in memories[secondPositionMemories][secondKey][quadruples[counter][2]].options['arrayIndexes']:
				#.options['arrayIndexes'][counterVerifyIterador].items[0].value.value
				arrayIndexTemporal.append(memories[secondPositionMemories][secondKey][quadruples[counter][2]].options['arrayIndexes'][contadorTemporal].items[0].value.value)
				contadorTemporal += 1
			
			#FIN 

			#vamos a necesitar el offsetValue para firstValue
			secondOffset = offsetCalculator(arrayIndexTemporal)

			#vaciar arrayIndexTemporal
			arrayIndexTemporal = list()

			#finalmente le asignamos el elemento del arreglo a firstValue
			secondValue = memories[secondPositionMemories][secondKey][quadruples[counter][2]].value[secondOffset]

		else:
			#si no es array, sacamos el valor directamente
			secondValue = memories[secondPositionMemories][secondKey][quadruples[counter][2]].value


	if(isTemporal(quadruples[counter][3])):
		#si el tercero es temporal (en una suma no deberia serlo)
		thirdKey ="temporals"
		memories[thirdPositionMemories][thirdKey][quadruples[counter][3]] = ParseTree.Variable(0,"flag",quadruples[counter][3],None,None, None)
		thirdVariable = memories[thirdPositionMemories][thirdKey][quadruples[counter][3]]
	else:
		thirdKey ="variables"
		if(not isLocal(quadruples[counter][3])):
			thirdPositionMemories = 0
		#sin importar lo que pase igual vamos a recibir el objeto expression
		thirdVariable = memories[thirdPositionMemories][thirdKey][quadruples[counter][3]]

	#thirdVariable = ParseTree.Variable(0,"number",quadruples[counter][3],None,None, None)

	#checar si un elemento esta vacio
	if (firstValue is None):
		#crear error
		
		errorS = str(memories[firstPositionMemories][firstKey][quadruples[counter][1]].identifier) +  " is trying to be used when it's empty."
		giveUp = True
		return

	if (secondValue is None):
		#crear error
		errorS = str(memories[secondPositionMemories][secondKey][quadruples[counter][2]].identifier) +  " is trying to be used when it's empty."
		giveUp = True
		return	

	#ecuación final
	#memories[thirdPositionMemories][thirdKey][quadruples[counter][3]].value = memories[firstPositionMemories][firstKey][quadruples[counter][1]].value + memories[secondPositionMemories][secondKey][quadruples[counter][2]].value
	thirdVariable.value = firstValue and secondValue

	printMemories()

def f_or():

	global arrayIndexTemporal
	global giveUp
	global errorS

	#NECESITAMOS una referencia al objeto final
	thirdVariable = None
	#valor final a usar en ecuacion
	firstValue = None
	secondValue = None

	#variables reservadas para offsets en caso de arreglos
	firstOffset = None
	secondOffset = None
	thirdOffset = None

	firstPositionMemories = len(memories) - 1
	secondPositionMemories = len(memories) - 1
	thirdPositionMemories = len(memories) - 1

	if(isTemporal(quadruples[counter][1])):
		firstKey ="temporals"
		firstValue = memories[firstPositionMemories][firstKey][quadruples[counter][1]].value
	else:
		firstKey ="variables"
		if(not isLocal(quadruples[counter][1])):
			firstPositionMemories = 0
		#Hay que ver si estamos lidiando con un arreglo o no
		if(isArray(memories[firstPositionMemories][firstKey][quadruples[counter][1]])):
			#empieza lo bueno
			#hay que obtener la direccion resultante para sacar el value que necesitamos del arreglo aplanado
			
			#
			contadorTemporal = 0
			for key in memories[firstPositionMemories][firstKey][quadruples[counter][1]].options['arrayIndexes']:
				#.options['arrayIndexes'][counterVerifyIterador].items[0].value.value
				arrayIndexTemporal.append(memories[firstPositionMemories][firstKey][quadruples[counter][1]].options['arrayIndexes'][contadorTemporal].items[0].value.value)
				contadorTemporal += 1
			
			#FIN 

			#vamos a necesitar el offsetValue para firstValue
			firstOffset = offsetCalculator(arrayIndexTemporal)

			#vaciar arrayIndexTemporal
			arrayIndexTemporal = list()

			#finalmente le asignamos el elemento del arreglo a firstValue
			firstValue = memories[firstPositionMemories][firstKey][quadruples[counter][1]].value[firstOffset]

		else:
			#si no es array, sacamos el valor directamente
			firstValue = memories[firstPositionMemories][firstKey][quadruples[counter][1]].value

	if(isTemporal(quadruples[counter][2])):
		secondKey ="temporals"
		secondValue = memories[secondPositionMemories][secondKey][quadruples[counter][2]].value
	else:
		secondKey ="variables"
		if(not isLocal(quadruples[counter][2])):
			secondPositionMemories = 0
		#Hay que ver si estamos lidiando con un arreglo o no
		if(isArray(memories[secondPositionMemories][secondKey][quadruples[counter][2]])):
			#empieza lo bueno
			#hay que obtener la direccion resultante para sacar el value que necesitamos del arreglo aplanado
			
			#
			contadorTemporal = 0
			for key in memories[secondPositionMemories][secondKey][quadruples[counter][2]].options['arrayIndexes']:
				#.options['arrayIndexes'][counterVerifyIterador].items[0].value.value
				arrayIndexTemporal.append(memories[secondPositionMemories][secondKey][quadruples[counter][2]].options['arrayIndexes'][contadorTemporal].items[0].value.value)
				contadorTemporal += 1
			
			#FIN 

			#vamos a necesitar el offsetValue para firstValue
			secondOffset = offsetCalculator(arrayIndexTemporal)

			#vaciar arrayIndexTemporal
			arrayIndexTemporal = list()

			#finalmente le asignamos el elemento del arreglo a firstValue
			secondValue = memories[secondPositionMemories][secondKey][quadruples[counter][2]].value[secondOffset]

		else:
			#si no es array, sacamos el valor directamente
			secondValue = memories[secondPositionMemories][secondKey][quadruples[counter][2]].value


	if(isTemporal(quadruples[counter][3])):
		#si el tercero es temporal (en una suma no deberia serlo)
		thirdKey ="temporals"
		memories[thirdPositionMemories][thirdKey][quadruples[counter][3]] = ParseTree.Variable(0,"flag",quadruples[counter][3],None,None, None)
		thirdVariable = memories[thirdPositionMemories][thirdKey][quadruples[counter][3]]
	else:
		thirdKey ="variables"
		if(not isLocal(quadruples[counter][3])):
			thirdPositionMemories = 0
		#sin importar lo que pase igual vamos a recibir el objeto expression
		thirdVariable = memories[thirdPositionMemories][thirdKey][quadruples[counter][3]]

	#thirdVariable = ParseTree.Variable(0,"number",quadruples[counter][3],None,None, None)

		#checar si un elemento esta vacio
	if (firstValue is None):
		#crear error
		
		errorS = str(memories[firstPositionMemories][firstKey][quadruples[counter][1]].identifier) +  " is trying to be used when it's empty."
		giveUp = True
		return

	if (secondValue is None):
		#crear error
		errorS = str(memories[secondPositionMemories][secondKey][quadruples[counter][2]].identifier) +  " is trying to be used when it's empty."
		giveUp = True
		return

	#ecuación final
	#memories[thirdPositionMemories][thirdKey][quadruples[counter][3]].value = memories[firstPositionMemories][firstKey][quadruples[counter][1]].value + memories[secondPositionMemories][secondKey][quadruples[counter][2]].value
	thirdVariable.value = firstValue or secondValue

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

	global arrayIndexTemporal
	global giveUp
	global errorS

	#NECESITAMOS una referencia al objeto final
	thirdVariable = None
	#valor final a usar en ecuacion
	firstValue = None
	secondValue = None

	#variables reservadas para offsets en caso de arreglos
	firstOffset = None
	secondOffset = None
	thirdOffset = None

	firstPositionMemories = len(memories) - 1
	secondPositionMemories = len(memories) - 1
	thirdPositionMemories = len(memories) - 1

	if(isTemporal(quadruples[counter][1])):
		firstKey ="temporals"
		firstValue = memories[firstPositionMemories][firstKey][quadruples[counter][1]].value
	else:
		firstKey ="variables"
		if(not isLocal(quadruples[counter][1])):
			firstPositionMemories = 0
		#Hay que ver si estamos lidiando con un arreglo o no
		if(isArray(memories[firstPositionMemories][firstKey][quadruples[counter][1]])):
			#empieza lo bueno
			#hay que obtener la direccion resultante para sacar el value que necesitamos del arreglo aplanado
			
			#
			contadorTemporal = 0
			for key in memories[firstPositionMemories][firstKey][quadruples[counter][1]].options['arrayIndexes']:
				#.options['arrayIndexes'][counterVerifyIterador].items[0].value.value
				arrayIndexTemporal.append(memories[firstPositionMemories][firstKey][quadruples[counter][1]].options['arrayIndexes'][contadorTemporal].items[0].value.value)
				contadorTemporal += 1
			
			#FIN 

			#vamos a necesitar el offsetValue para firstValue
			firstOffset = offsetCalculator(arrayIndexTemporal)

			#vaciar arrayIndexTemporal
			arrayIndexTemporal = list()

			#finalmente le asignamos el elemento del arreglo a firstValue
			firstValue = memories[firstPositionMemories][firstKey][quadruples[counter][1]].value[firstOffset]

		else:
			#si no es array, sacamos el valor directamente
			firstValue = memories[firstPositionMemories][firstKey][quadruples[counter][1]].value

	if(isTemporal(quadruples[counter][2])):
		secondKey ="temporals"
		secondValue = memories[secondPositionMemories][secondKey][quadruples[counter][2]].value
	else:
		secondKey ="variables"
		if(not isLocal(quadruples[counter][2])):
			secondPositionMemories = 0
		#Hay que ver si estamos lidiando con un arreglo o no
		if(isArray(memories[secondPositionMemories][secondKey][quadruples[counter][2]])):
			#empieza lo bueno
			#hay que obtener la direccion resultante para sacar el value que necesitamos del arreglo aplanado
			
			#
			contadorTemporal = 0
			for key in memories[secondPositionMemories][secondKey][quadruples[counter][2]].options['arrayIndexes']:
				#.options['arrayIndexes'][counterVerifyIterador].items[0].value.value
				arrayIndexTemporal.append(memories[secondPositionMemories][secondKey][quadruples[counter][2]].options['arrayIndexes'][contadorTemporal].items[0].value.value)
				contadorTemporal += 1
			
			#FIN 

			#vamos a necesitar el offsetValue para firstValue
			secondOffset = offsetCalculator(arrayIndexTemporal)

			#vaciar arrayIndexTemporal
			arrayIndexTemporal = list()

			#finalmente le asignamos el elemento del arreglo a firstValue
			secondValue = memories[secondPositionMemories][secondKey][quadruples[counter][2]].value[secondOffset]

		else:
			#si no es array, sacamos el valor directamente
			secondValue = memories[secondPositionMemories][secondKey][quadruples[counter][2]].value


	if(isTemporal(quadruples[counter][3])):
		#si el tercero es temporal (en una suma no deberia serlo)
		thirdKey ="temporals"
		memories[thirdPositionMemories][thirdKey][quadruples[counter][3]] = ParseTree.Variable(0,"flag",quadruples[counter][3],None,None, None)
		thirdVariable = memories[thirdPositionMemories][thirdKey][quadruples[counter][3]]
	else:
		thirdKey ="variables"
		if(not isLocal(quadruples[counter][3])):
			thirdPositionMemories = 0
		#sin importar lo que pase igual vamos a recibir el objeto expression
		thirdVariable = memories[thirdPositionMemories][thirdKey][quadruples[counter][3]]

	#thirdVariable = ParseTree.Variable(0,"number",quadruples[counter][3],None,None, None)

	#checar si un elemento esta vacio
	if (firstValue is None):
		#crear error
		
		errorS = str(memories[firstPositionMemories][firstKey][quadruples[counter][1]].identifier) +  " is trying to be used when it's empty."
		giveUp = True
		return

	if (secondValue is None):
		#crear error
		errorS = str(memories[secondPositionMemories][secondKey][quadruples[counter][2]].identifier) +  " is trying to be used when it's empty."
		giveUp = True
		return


	#ecuación final
	#memories[thirdPositionMemories][thirdKey][quadruples[counter][3]].value = memories[firstPositionMemories][firstKey][quadruples[counter][1]].value + memories[secondPositionMemories][secondKey][quadruples[counter][2]].value
	thirdVariable.value = firstValue > secondValue

	printMemories()

def f_lesser():

	global arrayIndexTemporal
	global giveUp
	global errorS

	#NECESITAMOS una referencia al objeto final
	thirdVariable = None
	#valor final a usar en ecuacion
	firstValue = None
	secondValue = None

	#variables reservadas para offsets en caso de arreglos
	firstOffset = None
	secondOffset = None
	thirdOffset = None

	firstPositionMemories = len(memories) - 1
	secondPositionMemories = len(memories) - 1
	thirdPositionMemories = len(memories) - 1

	if(isTemporal(quadruples[counter][1])):
		firstKey ="temporals"
		firstValue = memories[firstPositionMemories][firstKey][quadruples[counter][1]].value
	else:
		firstKey ="variables"
		if(not isLocal(quadruples[counter][1])):
			firstPositionMemories = 0
		#Hay que ver si estamos lidiando con un arreglo o no
		if(isArray(memories[firstPositionMemories][firstKey][quadruples[counter][1]])):
			#empieza lo bueno
			#hay que obtener la direccion resultante para sacar el value que necesitamos del arreglo aplanado
			
			#
			contadorTemporal = 0
			for key in memories[firstPositionMemories][firstKey][quadruples[counter][1]].options['arrayIndexes']:
				#.options['arrayIndexes'][counterVerifyIterador].items[0].value.value
				arrayIndexTemporal.append(memories[firstPositionMemories][firstKey][quadruples[counter][1]].options['arrayIndexes'][contadorTemporal].items[0].value.value)
				contadorTemporal += 1
			
			#FIN 

			#vamos a necesitar el offsetValue para firstValue
			firstOffset = offsetCalculator(arrayIndexTemporal)

			#vaciar arrayIndexTemporal
			arrayIndexTemporal = list()

			#finalmente le asignamos el elemento del arreglo a firstValue
			firstValue = memories[firstPositionMemories][firstKey][quadruples[counter][1]].value[firstOffset]

		else:
			#si no es array, sacamos el valor directamente
			firstValue = memories[firstPositionMemories][firstKey][quadruples[counter][1]].value

	if(isTemporal(quadruples[counter][2])):
		secondKey ="temporals"
		secondValue = memories[secondPositionMemories][secondKey][quadruples[counter][2]].value
	else:
		secondKey ="variables"
		if(not isLocal(quadruples[counter][2])):
			secondPositionMemories = 0
		#Hay que ver si estamos lidiando con un arreglo o no
		if(isArray(memories[secondPositionMemories][secondKey][quadruples[counter][2]])):
			#empieza lo bueno
			#hay que obtener la direccion resultante para sacar el value que necesitamos del arreglo aplanado
			
			#
			contadorTemporal = 0
			for key in memories[secondPositionMemories][secondKey][quadruples[counter][2]].options['arrayIndexes']:
				#.options['arrayIndexes'][counterVerifyIterador].items[0].value.value
				arrayIndexTemporal.append(memories[secondPositionMemories][secondKey][quadruples[counter][2]].options['arrayIndexes'][contadorTemporal].items[0].value.value)
				contadorTemporal += 1
			
			#FIN 

			#vamos a necesitar el offsetValue para firstValue
			secondOffset = offsetCalculator(arrayIndexTemporal)

			#vaciar arrayIndexTemporal
			arrayIndexTemporal = list()

			#finalmente le asignamos el elemento del arreglo a firstValue
			secondValue = memories[secondPositionMemories][secondKey][quadruples[counter][2]].value[secondOffset]

		else:
			#si no es array, sacamos el valor directamente
			secondValue = memories[secondPositionMemories][secondKey][quadruples[counter][2]].value


	if(isTemporal(quadruples[counter][3])):
		#si el tercero es temporal (en una suma no deberia serlo)
		thirdKey ="temporals"
		memories[thirdPositionMemories][thirdKey][quadruples[counter][3]] = ParseTree.Variable(0,"flag",quadruples[counter][3],None,None, None)
		thirdVariable = memories[thirdPositionMemories][thirdKey][quadruples[counter][3]]
	else:
		thirdKey ="variables"
		if(not isLocal(quadruples[counter][3])):
			thirdPositionMemories = 0
		#sin importar lo que pase igual vamos a recibir el objeto expression
		thirdVariable = memories[thirdPositionMemories][thirdKey][quadruples[counter][3]]

	#thirdVariable = ParseTree.Variable(0,"number",quadruples[counter][3],None,None, None)

	#checar si un elemento esta vacio
	if (firstValue is None):
		#crear error
		
		errorS = str(memories[firstPositionMemories][firstKey][quadruples[counter][1]].identifier) +  " is trying to be used when it's empty."
		giveUp = True
		return

	if (secondValue is None):
		#crear error
		errorS = str(memories[secondPositionMemories][secondKey][quadruples[counter][2]].identifier) +  " is trying to be used when it's empty."
		giveUp = True
		return

	#ecuación final
	#memories[thirdPositionMemories][thirdKey][quadruples[counter][3]].value = memories[firstPositionMemories][firstKey][quadruples[counter][1]].value + memories[secondPositionMemories][secondKey][quadruples[counter][2]].value
	thirdVariable.value = firstValue < secondValue

	printMemories()


def f_plus():

	global arrayIndexTemporal
	global giveUp
	global errorS

	#NECESITAMOS una referencia al objeto final
	thirdVariable = None
	#valor final a usar en ecuacion
	firstValue = None
	secondValue = None

	#variables reservadas para offsets en caso de arreglos
	firstOffset = None
	secondOffset = None
	thirdOffset = None

	firstPositionMemories = len(memories) - 1
	secondPositionMemories = len(memories) - 1
	thirdPositionMemories = len(memories) - 1

	if(isTemporal(quadruples[counter][1])):
		firstKey ="temporals"
		firstValue = memories[firstPositionMemories][firstKey][quadruples[counter][1]].value
	else:
		firstKey ="variables"
		if(not isLocal(quadruples[counter][1])):
			firstPositionMemories = 0
		#Hay que ver si estamos lidiando con un arreglo o no
		if(isArray(memories[firstPositionMemories][firstKey][quadruples[counter][1]])):
			#empieza lo bueno
			#hay que obtener la direccion resultante para sacar el value que necesitamos del arreglo aplanado
			
			#
			contadorTemporal = 0
			for key in memories[firstPositionMemories][firstKey][quadruples[counter][1]].options['arrayIndexes']:
				#.options['arrayIndexes'][counterVerifyIterador].items[0].value.value
				arrayIndexTemporal.append(memories[firstPositionMemories][firstKey][quadruples[counter][1]].options['arrayIndexes'][contadorTemporal].items[0].value.value)
				contadorTemporal += 1
			
			#FIN 

			#vamos a necesitar el offsetValue para firstValue
			firstOffset = offsetCalculator(arrayIndexTemporal)

			#vaciar arrayIndexTemporal
			arrayIndexTemporal = list()

			#finalmente le asignamos el elemento del arreglo a firstValue
			firstValue = memories[firstPositionMemories][firstKey][quadruples[counter][1]].value[firstOffset]

		else:
			#si no es array, sacamos el valor directamente
			firstValue = memories[firstPositionMemories][firstKey][quadruples[counter][1]].value

	if(isTemporal(quadruples[counter][2])):
		secondKey ="temporals"
		secondValue = memories[secondPositionMemories][secondKey][quadruples[counter][2]].value
	else:
		secondKey ="variables"
		if(not isLocal(quadruples[counter][2])):
			secondPositionMemories = 0
		#Hay que ver si estamos lidiando con un arreglo o no
		if(isArray(memories[secondPositionMemories][secondKey][quadruples[counter][2]])):
			#empieza lo bueno
			#hay que obtener la direccion resultante para sacar el value que necesitamos del arreglo aplanado
			
			#
			contadorTemporal = 0
			for key in memories[secondPositionMemories][secondKey][quadruples[counter][2]].options['arrayIndexes']:
				#.options['arrayIndexes'][counterVerifyIterador].items[0].value.value
				arrayIndexTemporal.append(memories[secondPositionMemories][secondKey][quadruples[counter][2]].options['arrayIndexes'][contadorTemporal].items[0].value.value)
				contadorTemporal += 1
			
			#FIN 

			#vamos a necesitar el offsetValue para firstValue
			secondOffset = offsetCalculator(arrayIndexTemporal)

			#vaciar arrayIndexTemporal
			arrayIndexTemporal = list()

			#finalmente le asignamos el elemento del arreglo a firstValue
			secondValue = memories[secondPositionMemories][secondKey][quadruples[counter][2]].value[secondOffset]

		else:
			#si no es array, sacamos el valor directamente
			secondValue = memories[secondPositionMemories][secondKey][quadruples[counter][2]].value


	if(isTemporal(quadruples[counter][3])):
		#si el tercero es temporal (en una suma no deberia serlo)
		thirdKey ="temporals"
		memories[thirdPositionMemories][thirdKey][quadruples[counter][3]] = ParseTree.Variable(0,"number",quadruples[counter][3],None,None, None)
		thirdVariable = memories[thirdPositionMemories][thirdKey][quadruples[counter][3]]
	else:
		thirdKey ="variables"
		if(not isLocal(quadruples[counter][3])):
			thirdPositionMemories = 0
		#sin importar lo que pase igual vamos a recibir el objeto expression
		thirdVariable = memories[thirdPositionMemories][thirdKey][quadruples[counter][3]]

	#thirdVariable = ParseTree.Variable(0,"number",quadruples[counter][3],None,None, None)

	#checar si un elemento esta vacio
	if (firstValue is None):
		#crear error
		
		errorS = str(memories[firstPositionMemories][firstKey][quadruples[counter][1]].identifier) +  " is trying to be used when it's empty."
		giveUp = True
		return

	if (secondValue is None):
		#crear error
		errorS = str(memories[secondPositionMemories][secondKey][quadruples[counter][2]].identifier) +  " is trying to be used when it's empty."
		giveUp = True
		return

	#ecuación final
	#memories[thirdPositionMemories][thirdKey][quadruples[counter][3]].value = memories[firstPositionMemories][firstKey][quadruples[counter][1]].value + memories[secondPositionMemories][secondKey][quadruples[counter][2]].value
	thirdVariable.value = firstValue + secondValue

	printMemories()
	
def f_minus():

	global arrayIndexTemporal
	global giveUp
	global errorS

	#NECESITAMOS una referencia al objeto final
	thirdVariable = None
	#valor final a usar en ecuacion
	firstValue = None
	secondValue = None

	#variables reservadas para offsets en caso de arreglos
	firstOffset = None
	secondOffset = None
	thirdOffset = None

	firstPositionMemories = len(memories) - 1
	secondPositionMemories = len(memories) - 1
	thirdPositionMemories = len(memories) - 1

	if(isTemporal(quadruples[counter][1])):
		firstKey ="temporals"
		firstValue = memories[firstPositionMemories][firstKey][quadruples[counter][1]].value
	else:
		firstKey ="variables"
		if(not isLocal(quadruples[counter][1])):
			firstPositionMemories = 0
		#Hay que ver si estamos lidiando con un arreglo o no
		if(isArray(memories[firstPositionMemories][firstKey][quadruples[counter][1]])):
			#empieza lo bueno
			#hay que obtener la direccion resultante para sacar el value que necesitamos del arreglo aplanado
			
			#
			contadorTemporal = 0
			for key in memories[firstPositionMemories][firstKey][quadruples[counter][1]].options['arrayIndexes']:
				#.options['arrayIndexes'][counterVerifyIterador].items[0].value.value
				arrayIndexTemporal.append(memories[firstPositionMemories][firstKey][quadruples[counter][1]].options['arrayIndexes'][contadorTemporal].items[0].value.value)
				contadorTemporal += 1
			
			#FIN 

			#vamos a necesitar el offsetValue para firstValue
			firstOffset = offsetCalculator(arrayIndexTemporal)

			#vaciar arrayIndexTemporal
			arrayIndexTemporal = list()

			#finalmente le asignamos el elemento del arreglo a firstValue
			firstValue = memories[firstPositionMemories][firstKey][quadruples[counter][1]].value[firstOffset]

		else:
			#si no es array, sacamos el valor directamente
			firstValue = memories[firstPositionMemories][firstKey][quadruples[counter][1]].value

	if(isTemporal(quadruples[counter][2])):
		secondKey ="temporals"
		secondValue = memories[secondPositionMemories][secondKey][quadruples[counter][2]].value
	else:
		secondKey ="variables"
		if(not isLocal(quadruples[counter][2])):
			secondPositionMemories = 0
		#Hay que ver si estamos lidiando con un arreglo o no
		if(isArray(memories[secondPositionMemories][secondKey][quadruples[counter][2]])):
			#empieza lo bueno
			#hay que obtener la direccion resultante para sacar el value que necesitamos del arreglo aplanado
			
			#
			contadorTemporal = 0
			for key in memories[secondPositionMemories][secondKey][quadruples[counter][2]].options['arrayIndexes']:
				#.options['arrayIndexes'][counterVerifyIterador].items[0].value.value
				arrayIndexTemporal.append(memories[secondPositionMemories][secondKey][quadruples[counter][2]].options['arrayIndexes'][contadorTemporal].items[0].value.value)
				contadorTemporal += 1
			
			#FIN 

			#vamos a necesitar el offsetValue para firstValue
			secondOffset = offsetCalculator(arrayIndexTemporal)

			#vaciar arrayIndexTemporal
			arrayIndexTemporal = list()

			#finalmente le asignamos el elemento del arreglo a firstValue
			secondValue = memories[secondPositionMemories][secondKey][quadruples[counter][2]].value[secondOffset]

		else:
			#si no es array, sacamos el valor directamente
			secondValue = memories[secondPositionMemories][secondKey][quadruples[counter][2]].value


	if(isTemporal(quadruples[counter][3])):
		#si el tercero es temporal (en una suma no deberia serlo)
		thirdKey ="temporals"
		memories[thirdPositionMemories][thirdKey][quadruples[counter][3]] = ParseTree.Variable(0,"number",quadruples[counter][3],None,None, None)
		thirdVariable = memories[thirdPositionMemories][thirdKey][quadruples[counter][3]]
	else:
		thirdKey ="variables"
		if(not isLocal(quadruples[counter][3])):
			thirdPositionMemories = 0
		#sin importar lo que pase igual vamos a recibir el objeto expression
		thirdVariable = memories[thirdPositionMemories][thirdKey][quadruples[counter][3]]

	#checar si un elemento esta vacio
	if (firstValue is None):
		#crear error
		
		errorS = str(memories[firstPositionMemories][firstKey][quadruples[counter][1]].identifier) +  " is trying to be used when it's empty."
		giveUp = True
		return

	if (secondValue is None):
		#crear error
		errorS = str(memories[secondPositionMemories][secondKey][quadruples[counter][2]].identifier) +  " is trying to be used when it's empty."
		giveUp = True
		return

	#thirdVariable = ParseTree.Variable(0,"number",quadruples[counter][3],None,None, None)

	#ecuación final
	#memories[thirdPositionMemories][thirdKey][quadruples[counter][3]].value = memories[firstPositionMemories][firstKey][quadruples[counter][1]].value - memories[secondPositionMemories][secondKey][quadruples[counter][2]].value
	thirdVariable.value = firstValue - secondValue

	printMemories()

def f_multiplication():

	global arrayIndexTemporal
	global giveUp
	global errorS

	#NECESITAMOS una referencia al objeto final
	thirdVariable = None
	#valor final a usar en ecuacion
	firstValue = None
	secondValue = None

	#variables reservadas para offsets en caso de arreglos
	firstOffset = None
	secondOffset = None
	thirdOffset = None

	firstPositionMemories = len(memories) - 1
	secondPositionMemories = len(memories) - 1
	thirdPositionMemories = len(memories) - 1

	if(isTemporal(quadruples[counter][1])):
		firstKey ="temporals"
		firstValue = memories[firstPositionMemories][firstKey][quadruples[counter][1]].value
	else:
		firstKey ="variables"
		if(not isLocal(quadruples[counter][1])):
			firstPositionMemories = 0
		#Hay que ver si estamos lidiando con un arreglo o no
		if(isArray(memories[firstPositionMemories][firstKey][quadruples[counter][1]])):
			#empieza lo bueno
			#hay que obtener la direccion resultante para sacar el value que necesitamos del arreglo aplanado
			
			#
			contadorTemporal = 0
			for key in memories[firstPositionMemories][firstKey][quadruples[counter][1]].options['arrayIndexes']:
				#.options['arrayIndexes'][counterVerifyIterador].items[0].value.value
				arrayIndexTemporal.append(memories[firstPositionMemories][firstKey][quadruples[counter][1]].options['arrayIndexes'][contadorTemporal].items[0].value.value)
				contadorTemporal += 1
			
			#FIN 

			#vamos a necesitar el offsetValue para firstValue
			firstOffset = offsetCalculator(arrayIndexTemporal)

			#vaciar arrayIndexTemporal
			arrayIndexTemporal = list()

			#finalmente le asignamos el elemento del arreglo a firstValue
			firstValue = memories[firstPositionMemories][firstKey][quadruples[counter][1]].value[firstOffset]

		else:
			#si no es array, sacamos el valor directamente
			firstValue = memories[firstPositionMemories][firstKey][quadruples[counter][1]].value

	if(isTemporal(quadruples[counter][2])):
		secondKey ="temporals"
		secondValue = memories[secondPositionMemories][secondKey][quadruples[counter][2]].value
	else:
		secondKey ="variables"
		if(not isLocal(quadruples[counter][2])):
			secondPositionMemories = 0
		#Hay que ver si estamos lidiando con un arreglo o no
		if(isArray(memories[secondPositionMemories][secondKey][quadruples[counter][2]])):
			#empieza lo bueno
			#hay que obtener la direccion resultante para sacar el value que necesitamos del arreglo aplanado
			
			#
			contadorTemporal = 0
			for key in memories[secondPositionMemories][secondKey][quadruples[counter][2]].options['arrayIndexes']:
				#.options['arrayIndexes'][counterVerifyIterador].items[0].value.value
				arrayIndexTemporal.append(memories[secondPositionMemories][secondKey][quadruples[counter][2]].options['arrayIndexes'][contadorTemporal].items[0].value.value)
				contadorTemporal += 1
			
			#FIN 

			#vamos a necesitar el offsetValue para firstValue
			secondOffset = offsetCalculator(arrayIndexTemporal)

			#vaciar arrayIndexTemporal
			arrayIndexTemporal = list()

			#finalmente le asignamos el elemento del arreglo a firstValue
			secondValue = memories[secondPositionMemories][secondKey][quadruples[counter][2]].value[secondOffset]

		else:
			#si no es array, sacamos el valor directamente
			secondValue = memories[secondPositionMemories][secondKey][quadruples[counter][2]].value


	if(isTemporal(quadruples[counter][3])):
		#si el tercero es temporal (en una suma no deberia serlo)
		thirdKey ="temporals"
		memories[thirdPositionMemories][thirdKey][quadruples[counter][3]] = ParseTree.Variable(0,"number",quadruples[counter][3],None,None, None)
		thirdVariable = memories[thirdPositionMemories][thirdKey][quadruples[counter][3]]
	else:
		thirdKey ="variables"
		if(not isLocal(quadruples[counter][3])):
			thirdPositionMemories = 0
		#sin importar lo que pase igual vamos a recibir el objeto expression
		thirdVariable = memories[thirdPositionMemories][thirdKey][quadruples[counter][3]]

	#checar si un elemento esta vacio
	if (firstValue is None):
		#crear error
		
		errorS = str(memories[firstPositionMemories][firstKey][quadruples[counter][1]].identifier) +  " is trying to be used when it's empty."
		giveUp = True
		return

	if (secondValue is None):
		#crear error
		errorS = str(memories[secondPositionMemories][secondKey][quadruples[counter][2]].identifier) +  " is trying to be used when it's empty."
		giveUp = True
		return

	#thirdVariable = ParseTree.Variable(0,"number",quadruples[counter][3],None,None, None)
	

	#ecuación final
	#memories[thirdPositionMemories][thirdKey][quadruples[counter][3]].value = memories[firstPositionMemories][firstKey][quadruples[counter][1]].value + memories[secondPositionMemories][secondKey][quadruples[counter][2]].value
	thirdVariable.value = firstValue * secondValue

	printMemories()

def f_division():
	
	global arrayIndexTemporal
	global giveUp
	global errorS

	#NECESITAMOS una referencia al objeto final
	thirdVariable = None
	#valor final a usar en ecuacion
	firstValue = None
	secondValue = None

	#variables reservadas para offsets en caso de arreglos
	firstOffset = None
	secondOffset = None
	thirdOffset = None

	firstPositionMemories = len(memories) - 1
	secondPositionMemories = len(memories) - 1
	thirdPositionMemories = len(memories) - 1

	if(isTemporal(quadruples[counter][1])):
		firstKey ="temporals"
		firstValue = memories[firstPositionMemories][firstKey][quadruples[counter][1]].value
	else:
		firstKey ="variables"
		if(not isLocal(quadruples[counter][1])):
			firstPositionMemories = 0
		#Hay que ver si estamos lidiando con un arreglo o no
		if(isArray(memories[firstPositionMemories][firstKey][quadruples[counter][1]])):
			#empieza lo bueno
			#hay que obtener la direccion resultante para sacar el value que necesitamos del arreglo aplanado
			
			#
			contadorTemporal = 0
			for key in memories[firstPositionMemories][firstKey][quadruples[counter][1]].options['arrayIndexes']:
				#.options['arrayIndexes'][counterVerifyIterador].items[0].value.value
				arrayIndexTemporal.append(memories[firstPositionMemories][firstKey][quadruples[counter][1]].options['arrayIndexes'][contadorTemporal].items[0].value.value)
				contadorTemporal += 1
			
			#FIN 

			#vamos a necesitar el offsetValue para firstValue
			firstOffset = offsetCalculator(arrayIndexTemporal)

			#vaciar arrayIndexTemporal
			arrayIndexTemporal = list()

			#finalmente le asignamos el elemento del arreglo a firstValue
			firstValue = memories[firstPositionMemories][firstKey][quadruples[counter][1]].value[firstOffset]

		else:
			#si no es array, sacamos el valor directamente
			firstValue = memories[firstPositionMemories][firstKey][quadruples[counter][1]].value

	if(isTemporal(quadruples[counter][2])):
		secondKey ="temporals"
		secondValue = memories[secondPositionMemories][secondKey][quadruples[counter][2]].value
	else:
		secondKey ="variables"
		if(not isLocal(quadruples[counter][2])):
			secondPositionMemories = 0
		#Hay que ver si estamos lidiando con un arreglo o no
		if(isArray(memories[secondPositionMemories][secondKey][quadruples[counter][2]])):
			#empieza lo bueno
			#hay que obtener la direccion resultante para sacar el value que necesitamos del arreglo aplanado
			
			#
			contadorTemporal = 0
			for key in memories[secondPositionMemories][secondKey][quadruples[counter][2]].options['arrayIndexes']:
				#.options['arrayIndexes'][counterVerifyIterador].items[0].value.value
				arrayIndexTemporal.append(memories[secondPositionMemories][secondKey][quadruples[counter][2]].options['arrayIndexes'][contadorTemporal].items[0].value.value)
				contadorTemporal += 1
			
			#FIN 

			#vamos a necesitar el offsetValue para firstValue
			secondOffset = offsetCalculator(arrayIndexTemporal)

			#vaciar arrayIndexTemporal
			arrayIndexTemporal = list()

			#finalmente le asignamos el elemento del arreglo a firstValue
			secondValue = memories[secondPositionMemories][secondKey][quadruples[counter][2]].value[secondOffset]

		else:
			#si no es array, sacamos el valor directamente
			secondValue = memories[secondPositionMemories][secondKey][quadruples[counter][2]].value


	if(isTemporal(quadruples[counter][3])):
		#si el tercero es temporal (en una suma no deberia serlo)
		thirdKey ="temporals"
		memories[thirdPositionMemories][thirdKey][quadruples[counter][3]] = ParseTree.Variable(0,"number",quadruples[counter][3],None,None, None)
		thirdVariable = memories[thirdPositionMemories][thirdKey][quadruples[counter][3]]
	else:
		thirdKey ="variables"
		if(not isLocal(quadruples[counter][3])):
			thirdPositionMemories = 0
		#sin importar lo que pase igual vamos a recibir el objeto expression
		thirdVariable = memories[thirdPositionMemories][thirdKey][quadruples[counter][3]]

	#checar si un elemento esta vacio
	if (firstValue is None):
		#crear error
		
		errorS = str(memories[firstPositionMemories][firstKey][quadruples[counter][1]].identifier) +  " is trying to be used when it's empty."
		giveUp = True
		return

	if (secondValue is None):
		#crear error
		errorS = str(memories[secondPositionMemories][secondKey][quadruples[counter][2]].identifier) +  " is trying to be used when it's empty."
		giveUp = True
		return

	#thirdVariable = ParseTree.Variable(0,"number",quadruples[counter][3],None,None, None)


	#ecuación final
	#memories[thirdPositionMemories][thirdKey][quadruples[counter][3]].value = memories[firstPositionMemories][firstKey][quadruples[counter][1]].value + memories[secondPositionMemories][secondKey][quadruples[counter][2]].value
	if(secondValue != 0):
		thirdVariable.value = firstValue / secondValue
	else:
		tsOne = ""
		tsTwo = ""

		if(str(firstValue) != quadruples[counter][1]):
			tsOne = "(" + str(firstValue) + ")"
		if(str(secondValue) != quadruples[counter][2]):
			tsTwo = "(" + str(secondValue) + ")"

		errorS = "Halting division by Zero! (" + quadruples[counter][1] +  tsOne + "/" + quadruples[counter][2] + tsTwo + ")"
		giveUp = True

	printMemories()

def f_modulus():
	
	global arrayIndexTemporal
	global giveUp
	global errorS

	#NECESITAMOS una referencia al objeto final
	thirdVariable = None
	#valor final a usar en ecuacion
	firstValue = None
	secondValue = None

	#variables reservadas para offsets en caso de arreglos
	firstOffset = None
	secondOffset = None
	thirdOffset = None

	firstPositionMemories = len(memories) - 1
	secondPositionMemories = len(memories) - 1
	thirdPositionMemories = len(memories) - 1

	if(isTemporal(quadruples[counter][1])):
		firstKey ="temporals"
		firstValue = memories[firstPositionMemories][firstKey][quadruples[counter][1]].value
	else:
		firstKey ="variables"
		if(not isLocal(quadruples[counter][1])):
			firstPositionMemories = 0
		#Hay que ver si estamos lidiando con un arreglo o no
		if(isArray(memories[firstPositionMemories][firstKey][quadruples[counter][1]])):
			#empieza lo bueno
			#hay que obtener la direccion resultante para sacar el value que necesitamos del arreglo aplanado
			
			#
			contadorTemporal = 0
			for key in memories[firstPositionMemories][firstKey][quadruples[counter][1]].options['arrayIndexes']:
				#.options['arrayIndexes'][counterVerifyIterador].items[0].value.value
				arrayIndexTemporal.append(memories[firstPositionMemories][firstKey][quadruples[counter][1]].options['arrayIndexes'][contadorTemporal].items[0].value.value)
				contadorTemporal += 1
			
			#FIN 

			#vamos a necesitar el offsetValue para firstValue
			firstOffset = offsetCalculator(arrayIndexTemporal)

			#vaciar arrayIndexTemporal
			arrayIndexTemporal = list()

			#finalmente le asignamos el elemento del arreglo a firstValue
			firstValue = memories[firstPositionMemories][firstKey][quadruples[counter][1]].value[firstOffset]

		else:
			#si no es array, sacamos el valor directamente
			firstValue = memories[firstPositionMemories][firstKey][quadruples[counter][1]].value

	if(isTemporal(quadruples[counter][2])):
		secondKey ="temporals"
		secondValue = memories[secondPositionMemories][secondKey][quadruples[counter][2]].value
	else:
		secondKey ="variables"
		if(not isLocal(quadruples[counter][2])):
			secondPositionMemories = 0
		#Hay que ver si estamos lidiando con un arreglo o no
		if(isArray(memories[secondPositionMemories][secondKey][quadruples[counter][2]])):
			#empieza lo bueno
			#hay que obtener la direccion resultante para sacar el value que necesitamos del arreglo aplanado
			
			#
			contadorTemporal = 0
			for key in memories[secondPositionMemories][secondKey][quadruples[counter][2]].options['arrayIndexes']:
				#.options['arrayIndexes'][counterVerifyIterador].items[0].value.value
				arrayIndexTemporal.append(memories[secondPositionMemories][secondKey][quadruples[counter][2]].options['arrayIndexes'][contadorTemporal].items[0].value.value)
				contadorTemporal += 1
			
			#FIN 

			#vamos a necesitar el offsetValue para firstValue
			secondOffset = offsetCalculator(arrayIndexTemporal)

			#vaciar arrayIndexTemporal
			arrayIndexTemporal = list()

			#finalmente le asignamos el elemento del arreglo a firstValue
			secondValue = memories[secondPositionMemories][secondKey][quadruples[counter][2]].value[secondOffset]

		else:
			#si no es array, sacamos el valor directamente
			secondValue = memories[secondPositionMemories][secondKey][quadruples[counter][2]].value


	if(isTemporal(quadruples[counter][3])):
		#si el tercero es temporal (en una suma no deberia serlo)
		thirdKey ="temporals"
		memories[thirdPositionMemories][thirdKey][quadruples[counter][3]] = ParseTree.Variable(0,"number",quadruples[counter][3],None,None, None)
		thirdVariable = memories[thirdPositionMemories][thirdKey][quadruples[counter][3]]
	else:
		thirdKey ="variables"
		if(not isLocal(quadruples[counter][3])):
			thirdPositionMemories = 0
		#sin importar lo que pase igual vamos a recibir el objeto expression
		thirdVariable = memories[thirdPositionMemories][thirdKey][quadruples[counter][3]]

		#checar si un elemento esta vacio
	if (firstValue is None):
		#crear error
		
		errorS = str(memories[firstPositionMemories][firstKey][quadruples[counter][1]].identifier) +  " is trying to be used when it's empty."
		giveUp = True
		return

	if (secondValue is None):
		#crear error
		errorS = str(memories[secondPositionMemories][secondKey][quadruples[counter][2]].identifier) +  " is trying to be used when it's empty."
		giveUp = True
		return

	#thirdVariable = ParseTree.Variable(0,"number",quadruples[counter][3],None,None, None)

	#ecuación final
	#memories[thirdPositionMemories][thirdKey][quadruples[counter][3]].value = memories[firstPositionMemories][firstKey][quadruples[counter][1]].value + memories[secondPositionMemories][secondKey][quadruples[counter][2]].value
	if(secondValue != 0):
		thirdVariable.value = firstValue % secondValue
	else:
		tsOne = ""
		tsTwo = ""

		if(str(firstValue) != quadruples[counter][1]):
			tsOne = "(" + str(firstValue) + ")"
		if(str(secondValue) != quadruples[counter][2]):
			tsTwo = "(" + str(secondValue) + ")"

		errorS = "Halting division by Zero! (" + quadruples[counter][1] +  tsOne + "%" + quadruples[counter][2] + tsTwo + ")"
		giveUp = True

	printMemories()

def f_assign():

	global arrayIndexTemporal
	global giveUp
	global errorS

	#NECESITAMOS una referencia al objeto final
	thirdVariable = None
	#valor final a usar en ecuacion
	firstValue = None

	#variables reservadas para offsets en caso de arreglos
	firstOffset = None
	thirdOffset = None

	firstPositionMemories = len(memories) - 1
	thirdPositionMemories = len(memories) - 1

	if(isTemporal(quadruples[counter][1])):
		firstKey ="temporals"
		firstValue = memories[firstPositionMemories][firstKey][quadruples[counter][1]].value
	else:
		firstKey ="variables"
		if(not isLocal(quadruples[counter][1])):
			firstPositionMemories = 0
		#Hay que ver si estamos lidiando con un arreglo o no
		if(isArray(memories[firstPositionMemories][firstKey][quadruples[counter][1]])):
			#empieza lo bueno
			#hay que obtener la direccion resultante para sacar el value que necesitamos del arreglo aplanado
			
			#TEMPORAL EN LO QUE DANIELITO PONE BIEN LOS ARRAYINDEXES
			contadorTemporal = 0
			for key, variable in memories[firstPositionMemories][firstKey][quadruples[counter][1]].options['arrayIndexes']:
				#.options['arrayIndexes'][counterVerifyIterador].items[0].value.value
				arrayIndexTemporal.append(memories[firstPositionMemories][firstKey][quadruples[counter][1]].options['arrayIndexes'][contadorTemporal].items[0].value.value)
				contadorTemporal += 1
			
			#FIN TEMPORALES

			#vamos a necesitar el offsetValue para firstValue
			firstOffset = offsetCalculator(arrayIndexTemporal)

			#vaciar arrayIndexTemporal
			arrayIndexTemporal = list()

			#finalmente le asignamos el elemento del arreglo a firstValue
			firstValue = memories[firstPositionMemories][firstKey][quadruples[counter][1]].value[firstOffset]

		else:
			#si no es array, sacamos el valor directamente
			firstValue = memories[firstPositionMemories][firstKey][quadruples[counter][1]].value



	if(isTemporal(quadruples[counter][3])):
		thirdKey ="temporals"
		if not quadruples[counter][3] in memories[thirdPositionMemories][thirdKey]:
			memories[thirdPositionMemories][thirdKey][quadruples[counter][3]] = ParseTree.Variable(None,memories[firstPositionMemories][firstKey][quadruples[counter][1]].type,quadruples[counter][3])
		thirdVariable = memories[thirdPositionMemories][thirdKey][quadruples[counter][3]]

	else:
		thirdKey ="variables"
		if(not isLocal(quadruples[counter][3])):
			thirdPositionMemories = 0
		#si es arreglo, vamos a necesitar
		if(isArray(memories[thirdPositionMemories][thirdKey][quadruples[counter][3]])):
			
			#TEMPORAL EN LO QUE DANIELITO PONE BIEN LOS ARRAYINDEXES
			contadorTemporal = 0
			for key in memories[thirdPositionMemories][thirdKey][quadruples[counter][3]].options['arrayIndexes']:
				#.options['arrayIndexes'][counterVerifyIterador].items[0].value.value
				arrayIndexTemporal.append(memories[thirdPositionMemories][thirdKey][quadruples[counter][3]].options['arrayIndexes'][contadorTemporal].items[0].value.value)
				contadorTemporal += 1
			
			#FIN TEMPORALES
			print(arrayIndexTemporal)
			#vamos a necesitar el offsetValue para thirdVariable[thirdoffset]
			thirdOffset = offsetCalculator(arrayIndexTemporal)
			#vaciar arrayIndexTemporal
			arrayIndexTemporal = list()
			
		#sin importar lo que pase igual vamos a recibir el objeto expression
		thirdVariable = memories[thirdPositionMemories][thirdKey][quadruples[counter][3]]

	
	#checar si un elemento esta vacio
	if (firstValue is None):
		#crear error
		print("WAAA")
		errorS = str(memories[firstPositionMemories][firstKey][quadruples[counter][1]].identifier) +  " is trying to be used when it's empty."
		giveUp = True
		return

	#if (secondValue is None):
		#crear error
	#	errorS = str(memories[secondPositionMemories][secondKey][quadruples[counter][2]].identifier) +  " is trying to be used when it's empty."
	#	giveUp = True


	#ecuación final
	#memories[thirdPositionMemories][thirdKey][quadruples[counter][3]].value = memories[firstPositionMemories][firstKey][quadruples[counter][1]].value
	if thirdOffset is None:
		thirdVariable.value = firstValue
	else:
		print(thirdVariable.value)
		thirdVariable.value[thirdOffset] = firstValue

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
		   'endver' : f_endver,
		   #verificacion de arreglo/matriz
		   'display' : f_display,
		   'enddisplay' : f_enddisplay,
		   #si acaba el programa
		   'end' : f_end
}

#funcion para sacar el offset para el arreglo aplanado
#su parametro es una lista, la cual es los arrayIndexes
#esta funcion tambien toma la primer de la fila de FilaListasIterador, y lo popea al acabar
def offsetCalculator(myArrayIndexes):

	global FilaListasIterador

	#total empieza en 0
	total = 0

	#agarramos una copia de la lista de iteradores, haciendo pop
	miListaIteradores = FilaListasIterador.pop(0)
	
	#empezando ciclos
	i = 0
	while (i < len(miListaIteradores)):
		multB = miListaIteradores[i] 
		j = len(myArrayIndexes) - 1 #iterador para siguiente ciclo
		while(j > i):
			multB *= myArrayIndexes[j]
			j -= 1
			
		total += multB

		i += 1 

	#FilaListasIterador
	print("aaaaaa")
	print(total)

	return total



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

#prints que si van a pasar (los demas son de pruebas)
if (errorS is ""):
	for n in myResults:
		print(n)
else:
	print(errorS)

# mem['t2'] = mem['a'] + mem[8]
# .....
# .....
# mem['z'] = mem['t6']