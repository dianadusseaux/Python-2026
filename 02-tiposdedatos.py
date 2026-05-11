#DATOS NUMERICOS 

#NÚMEROS ENTEROS
edad=22

#NÚMEROS FLOTANTES(REALES)
estatura=1.58

#BOOLIANO
estudiando = True #(true/false)

#NÚMEROS COMPLEJOS
#Son los que contienen una parte de numero real y otra de imaginario  se utiliza la palabra complex para numeros complejos 
num_complejo = 4+2j #primera forma de crear un numero complejo
otro_complejo = complex(4..2) #segunda forma de crear un numero complejo


int
float

#OPERACION ARITMETICA BAASICA(AREA DE UN TRIANGULO)
base = 8
altura = 12.5

area = (base*altura)/2

print(f"el area del triangulo es de {area} cm")

#FORMATO DE SALIDAS DE NUMEROS
#f es por flotante
#2 es por la cantidad de decimales

#Salida del numero PI con dos decimales
print(f"El numero PI tiene un valor de {PI: .2f}")

#EL METODO REDONDEO
print(round(area))
print(round(PI, 3))

#TRANSFORMACIONES
print(float(edad))

#CADENAS DE TEXTOS
print(CADENA DE TEXTO)
carrera = "Ingenieria civil en informatica"
institucion = "Universidad de los lagos"

#IMPRIMIR LA POCISION DEL CARACTER
print(carrera[0]) #se imprime la primera letra
print(carrera[-1]) #se imprime la ultima letra
print(carrera[0:10]) #obteniendo una sub cadena (cortando strings) subcadenas
#el print (hola/2) esto no se puede hacer
#print (hola*4) se escribe el hola 4 veces
print(len(institucion))
#len sirve para leer la cantidad de caracteres en el texto, (tambien cuenta los espacios)
#es [0] representa en que posicion va cada letra en la que se ubica el numero entre corchetes

#ARREGLOS (LISTAS)
print("ARREGLOS(LISTAS)")
colores = ["azul" , "verde" , "rojo" , "amarillo"] #arreglo de strings
numeros =[1,2,3,4,5,6] #arreglo numerico
lista_mixta = ["gato" , 2 , 67.0 , "true"]

print(colores[0]) #se imprime el primer elemento de la lista colores
print(numerico[-1]) #se imprime el ultimo elemento de la lista numeros 

# las "," separan los elementos dentros de la lista
# /n es un salto de linea
#La cadena de texto es solo informacion no es una lista