# number a = 1;
# number b = 7;
# number c = a + 8;
# number z =  (a + b - b + c) * b / c

#Esta es la memoria de nuestro programa durante ejecución
mem = {
	#Dividimos las variables con las temporales
	 'variables' : { 
	 '8' : 8,
	 'a' : 1,
     'b' : 7,
     'c' : None,
     'z' : None,
     },

     'temporals' : {

     }
    
 }

#creamos el quadruplo principal
quadruples = []

#ejemplo de cuadruplo generado

quadruples.append(['+', 'a', '8', '[t1]'])
quadruples.append(['=', '[t1]',  None, 'c'])
#empieza el if
quadruples.append(['>', 'a', 'c', '[t2]'])
quadruples.append(['gotof', '[t1]',  None, '10'])
quadruples.append(['+', 'a', 'b','[t3]'])
quadruples.append(['-', '[t3]','c','[t4]'])
quadruples.append(['+', '[t4]','c','[t5]'])
quadruples.append(['*', '[t5]','b','[t6]'])
quadruples.append(['%', '[t6]','c','[t7]'])
quadruples.append(['=', '[t7]', None,'z'])

#Creación de contador (apuntador) para cuadruplos
counter = 0

#Necesitare una pila de saltos para llamadas de función
callPSaltos = list()

#Y Necesitare una pila de saltos para saltos de if y while
ifWhilePSaltos = list()

#Tambien pueden haber casos donde el contador no avanza y envez se mueve
counterGo = True

#Creacion de lista que guarda el quadruple apuntado (opcional)
loadedQuadruple = []

#Como alternativa al switch, definimos las funciones por separado
def gotof():
	print ("numa un gotof")
	if(isTemporal(quadruples[counter][1])):
		firstKey ="temporals"
	else:
		firstKey ="variables"

	if(isTemporal(quadruples[counter][3])):
		thirdKey ="temporals"
	else:
		thirdKey ="variables"

	mem[thirdKey][quadruples[counter][3]] = mem[firstKey][quadruples[counter][1]] > mem[secondKey][quadruples[counter][2]]

	print(mem)

def greater():
	print ("numa un geater")
	if(isTemporal(quadruples[counter][1])):
		firstKey ="temporals"
	else:
		firstKey ="variables"

	if(isTemporal(quadruples[counter][2])):
		secondKey ="temporals"
	else:
		secondKey ="variables"

	if(isTemporal(quadruples[counter][3])):
		thirdKey ="temporals"
	else:
		thirdKey ="variables"

	mem[thirdKey][quadruples[counter][3]] = mem[firstKey][quadruples[counter][1]] > mem[secondKey][quadruples[counter][2]]

	print(mem)

def lesser():
	print ("numa un lesser")
	if(isTemporal(quadruples[counter][1])):
		firstKey ="temporals"
	else:
		firstKey ="variables"

	if(isTemporal(quadruples[counter][2])):
		secondKey ="temporals"
	else:
		secondKey ="variables"

	if(isTemporal(quadruples[counter][3])):
		thirdKey ="temporals"
	else:
		thirdKey ="variables"

	mem[thirdKey][quadruples[counter][3]] = mem[firstKey][quadruples[counter][1]] < mem[secondKey][quadruples[counter][2]]

	print(mem)

def plus():
	print ("numa un plus")
	if(isTemporal(quadruples[counter][1])):
		firstKey ="temporals"
	else:
		firstKey ="variables"

	if(isTemporal(quadruples[counter][2])):
		secondKey ="temporals"
	else:
		secondKey ="variables"

	if(isTemporal(quadruples[counter][3])):
		thirdKey ="temporals"
	else:
		thirdKey ="variables"

	mem[thirdKey][quadruples[counter][3]] = mem[firstKey][quadruples[counter][1]] + mem[secondKey][quadruples[counter][2]]

	print(mem)

def minus():
	print ("numa un minus")
	if(isTemporal(quadruples[counter][1])):
		firstKey ="temporals"
	else:
		firstKey ="variables"

	if(isTemporal(quadruples[counter][2])):
		secondKey ="temporals"
	else:
		secondKey ="variables"

	if(isTemporal(quadruples[counter][3])):
		thirdKey ="temporals"
	else:
		thirdKey ="variables"

	print()

	mem[thirdKey][quadruples[counter][3]] = mem[firstKey][quadruples[counter][1]] - mem[secondKey][quadruples[counter][2]]

	print(mem)

def multiplication():
	print ("numa una multiplication")
	if(isTemporal(quadruples[counter][1])):
		firstKey ="temporals"
	else:
		firstKey ="variables"

	if(isTemporal(quadruples[counter][2])):
		secondKey ="temporals"
	else:
		secondKey ="variables"

	if(isTemporal(quadruples[counter][3])):
		thirdKey ="temporals"
	else:
		thirdKey ="variables"

	mem[thirdKey][quadruples[counter][3]] = mem[firstKey][quadruples[counter][1]] * mem[secondKey][quadruples[counter][2]]

	print(mem)

def division():
	print ("numa un division")
	if(isTemporal(quadruples[counter][1])):
		firstKey ="temporals"
	else:
		firstKey ="variables"

	if(isTemporal(quadruples[counter][2])):
		secondKey ="temporals"
	else:
		secondKey ="variables"

	if(isTemporal(quadruples[counter][3])):
		thirdKey ="temporals"
	else:
		thirdKey ="variables"

	mem[thirdKey][quadruples[counter][3]] = mem[firstKey][quadruples[counter][1]] / mem[secondKey][quadruples[counter][2]]

	print(mem)

def modulus():
	print ("numa un modulus")
	if(isTemporal(quadruples[counter][1])):
		firstKey ="temporals"
	else:
		firstKey ="variables"

	if(isTemporal(quadruples[counter][2])):
		secondKey ="temporals"
	else:
		secondKey ="variables"

	if(isTemporal(quadruples[counter][3])):
		thirdKey ="temporals"
	else:
		thirdKey ="variables"

	mem[thirdKey][quadruples[counter][3]] = mem[firstKey][quadruples[counter][1]] % mem[secondKey][quadruples[counter][2]]

	print(mem)

def assign():
	print ("numa un assign")

	if(isTemporal(quadruples[counter][1])):
		firstKey ="temporals"
	else:
		firstKey ="variables"

	if(isTemporal(quadruples[counter][3])):
		thirdKey ="temporals"
	else:
		thirdKey ="variables"

	mem[thirdKey][quadruples[counter][3]] = mem[firstKey][quadruples[counter][1]]

	print(mem)

#una vez que declaramos todas las funciones de switch, 
options = {'+': plus,
		   '-': minus,
		   '*': multiplication,
		   '/': division,
		   '%' : modulus,
		   '=': assign,
		   '>': greater,
		   'gotof' : gotof,
}

#adicionalmente necesitamos funciones que se ejecutan si la variable el temporal o no
def isTemporal(expression):
	if(expression[0] == "[" and expression[len(expression)-1] == "]"):
		return True
	return False

while counter < len(quadruples):
	counterGo = True
	options[quadruples[counter][0]]()
	if(counterGo):
		counter = counter + 1
pass

# mem['t2'] = mem['a'] + mem[8]
# .....
# .....
# mem['z'] = mem['t6']