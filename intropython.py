#corchetes , parentesis y llaves
#sensibilidad a siertos caracteres
#función f y función +
#float significa que va a cambiar el tipo de dato
#pool arrastrar 
#comit 
#si=if
#sino/de lo contrario=elif 
#entonces es igual a :

"""cuando escribimos print si se quiere poner una variable no se utilizan las comillas
Input es para que el usuario ingrese un valor se le puede agregar entre parentesis una instruccion como por ejemplo (usuario ingrese su edad por favor)
para guardar la informacion entregada en input se debe crear una variable"""


temperatura_c = input("usuario ingrese la temperatura en grados celsius para transformar a fahrenheit")
fahrenheit = (float(temperatura_c) * 1.8) + 32
print(f"la temperatura es: , {fahrenheit} la cual equivale a la temperatura anterior en celsius que era{temperatura_c}")

alumno = {
	"nombre_alumno1" : "Diana" , 
    "edad_alumno1" : 22 ,
    "aprobado" : "true" , 
}

#imprimiendo cada valor con iterasiones 
for clave in alumno:
    print(clave)

#recorre una cantidad finita de datos


#set/actualización de valor en diccionario
alumno["edad"] ==  23


#agregando dato o variable o una key con su valor
alumno = ["carrera"] = "ICINF"     

#eliminar una variable del diccionario
del alumno["edad"] #del --> delete/borrar

# .get de valores especificos en el diccionario
print(alumno.get("nombre"))                                                                                   

print(alumno.get("trabajo", "no existe"))

dato = str(input(f"ingrese el dato que quiere obtener: "))
print(alumno.get("edad", "no existe esa key"))

print(alumno.keys()) #devuelve el nombre de la variable
print(alumno.values()) #devuelve el contenido del diccionario
print(alumno.items()) #devuelve todo en formato tupla


alumno2 = {
	"nombre2" : "estefania" ,
    "edad2" : "22"
}

#verificando
if "nombre1" in alumno2:   #si "nombre1" esta en alumno2
    print("existe")       #escribir "existe"
elif "edad1" in alumno2:   #si "edad" esta en alumno2
    print("existe")        #escribir "existe"
else:                      #sino 
    print("no existe ninguna")  #escribir "no existe ninguna"

#if--> si condicional
#in--> en (hablando dentro de algo)
#elif = else if --< sino si
#else = sino--> descarta todo lo anterior y siosi si ejecuta lo programado

nombre = "diana"

len(alumno) #sirve parq contar tambien el diccionario

#asignando variable
nombre = "estefania"
#condicional
if nombre == "diana": #if --> si(condicional) |":"|--> entonces ! se lee = si(la condición es verdadera) entonces se va a ejecutar...
    print("es correcto")
    #condicional descartador pero con especificación de condición 
elif nombre == "estefania": #elif --> combinación entre(else <--> if)! else = sino ! if = si ! se lee = sino si...
    print("no es diana pero si estefania")
    #condicional descartador
else:                 #else ---> sino ! se lee = sino entonces...
    print("no es correcto")

#"=" --> es igual a 
#"==" --> comparación
#pass se utiliza para continuar si no se encuentra nada

estado = True
while estado == True: #while es --> mientras
    respuesta = str(input("usuario ¿desea agregar un estudiante al diccionario 'estudiantes'? (s/n): "))
    if respuesta == "s":
        nombre_estudiante = str(input("Ingrese el nombre del estudiante que quiere agregar: "))
        edad=input("Ingrese la edad del estudiante que indico antes: ")
    elif respuesta == "n":
        print("entendido, usted no quiere seguir. adios!")
        estado = False
    else:
        print("la opcion indicada no es correcta, recuerde escribir o 's' para si o 'n' para no.")

#Paso de pseint a Python

#PSEINT | PYTHON

# si --> if
#sino si --> si no se cumple especificamente el condicional anterior ejecutar 
#condición --> con palabras reservadas en ingles y logicamente
#entonces/hacer --> ':' (dos puntos)
#else --> sino(osea que no se cumplen los casos anteriores o arrojan logicamente un 'falso')
# y --> and(se deben cumplir ambas condiciones o las que yo separe con and)
# o --> or(solo es necesario que minimamente se cumpla una condicion y se ejecutara)

#Orden de jerarquia en condicionales
#IF
# |
#ELIF
# |
#ELSE


#Ejemplo simple de condicionales
nombre = "Diana" #-->asignación/seteo variable

#Uso condicionales

if nombre == "Diana": # == --> comparación/equivalencia
    print("El nombre es el correcto")
else: #este 'sino' se ejecuta solamente si no se cumplen las condiciones que lo proceden
    print("El nombre no es 'Diana'")

"""
Forma de leer ese ejemplo simple

si la variable es 'Diana' entonces devolver en pantalla el mensaje:'el nombre es el correcto'

si no se cumple exactamente la condición anterior devolver en pantalla el mensaje: 'El nombre NO es 'Diana''

"""

#Ejemplo comun condicional(elif)
nombre = "Diana"

if nombre == "Estefania": 
    print("El nombre no es 'Estefania'")
elif nombre == "Diana": # --> sino si (osea si no cumple el caso de arriba, verfica ahora este caso)
    print("El nombre es 'Diana'")
else: 
    print("El nombre no es 'Diana'")

#Ejemplo un poco mas complejo de condicional 1 (|=):
nombre = "Diana"
edad = 22

if nombre == "Estefania": 
    if edad!= 19: # != --> es lo contrario a ==
        print("El sujeto se llama Diana y no tiene 19 años")
else: 
    print("El nombre no es 'Diana'")

"""
forma de leer un ejemplo un poco mas complejo:
"""

#4)Ejemplo un poco mas complejo

#and --> ambos se deben cumplir si o si para ejecutarse
#or --> almenos uno se debe cumplir para ejecutarse

nombre = "Diana"
edad = 22
nacionalidad = "chilena"

if nombre == "Estefania" and edad == 22:  
    print("el nombre es correcto")
elif nombre == "Diana" or nacionalidad == "chilena":
    print("Es latina")
else: 
    print("El nombre no es 'Diana'")

#match case
#el case va indentado dentro del match

#Funciones
#def significa definir una función
#se pueden poner varios parametros dentro de la función
def saludar(nombre:str, edad:int):
    print(f"hola{nombre}, tu edad es {edad} ")

saludar(12, "Diana")

def aprobar(nombre,curso,nota_final):
    print(f"Hola {nombre}")
    print(f"Tu curso es {curso}")
    if nota_final >= 4.0:
        print("Aprobado")
    else:
        print("Reprobado")

aprobar("a",2,5)
aprobar("b",3,5)
aprobar("c",2,2)


