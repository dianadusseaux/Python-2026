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
if nombre == "diana" #if --> si(condicional) |":"|--> entonces ! se lee = si(la condición es verdadera) entonces se va a ejecutar...
    print("es correcto")
    #condicional descartador pero con especificación de condición 
elif nombre == "estefania" #elif --> combinación entre(else <--> if)! else = sino ! if = si ! se lee = sino si...
    print("no es diana pero si estefania")
    #condicional descartador
else:                 #else ---> sino ! se lee = sino entonces...
    print("no es correcto")

#"=" --> es igual a 
#"==" --> comparación
#pass se utiliza para continuar si no se encuentra nada

estado = True
while estado == True #while es --> mientras
   respuesta = str(input("usuario ¿desea agregar un estudiante al diccionario 'estudiantes'? (s/n): "))
   if respuesta == "s":
        nombre_estudiante = str(input("Ingrese el nombre del estudiante que quiere agregar: "))
        edad=input("Ingrese la edad del estudiante que indico antes: ")
   elif respuesta == "n":
       print("entendido, usted no quiere seguir. adios!")
       estado = False
   else:
       print("la opcion indicada no es correcta, recuerde escribir o 's' para si o 'n' para no.")


