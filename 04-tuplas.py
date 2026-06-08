#TUPLAS

#TUPLA TIPO STRING
estudiantes = ("diana", "estefania")
print(type(estudiantes))
print(f"TUPLA: {estudiantes}")

#TUPLA COMPLETA CON DATOS ESTRUCTURADOS
datos = ([1,2,3,4,5], ("chonchi", "castro", "miraflores"), ("ulagos", "aiep", "ceduc"))
print(f"Datos de la lista: {datos}")

#POSICION
print(datos[0])
#Tambien se puede consutar la posicion , al igual que en la lista

#CON LAS LISTAS SE PUEDEN ELIMINAR LOS ELEMENTOS
lista_asignaturas = ["quimica", "programacion", "introduccion a la matematica", "introduccion a la ingenieria"]
print(f"LISTA: {lista_asignaturas}")

lista_asignaturas.pop()
print(f"LISTA CON ULTIMO ELEMENTO ELIMINADO: {lista_asignaturas}")

#¿QUE PASA SI QUIERO ELIMINAR EL ULTIMO ELEMENTO DE UNA TUPLA?
#respuesta: como es inmutable no se puede eliminar elementos de una tupla
"""estudiantes.pop()
print(f"TUPLA CON ULTIMO ELEMENTO ELIMINADO: {estudiantes}")"""

#OCUPAMOS EL METODO INDEX PARA CONSULTAR LA POSICION DE UN ELEMENTO
print(estudiantes.index("diana")) #se encuentra en la posicion 0

#METODO SORTED() PARA ORDENAR ELEMENTOS DE UNA TUPLA
print(sorted(estudiantes))
