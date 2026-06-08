#LISTAS

#PRIMERA FORMA DE DECLARAR LISTA
lista1 = ["diana, 22, true"]
ramos = []#Lista vacia


#SEGUNDA FORMA DE DECLARAR LISTA
n = list((1,2,3,4,5))

print(type(n))
print(type(lista1))

#METODOS PARA LAS LISTAS

#01-COUNT() contar las cantidad de concurrencias de un elemento
print(lista1.count("diana"))

print(lista1[0]) #estoy imprimiendo el primer orden de la lista

print(ramos)

# Agregar un elemento al final de la lista
ramos.append("quimica")
print(ramos)

ramos.append("habilidades comunicativas")
print(ramos)

ramos.append("programacion")
print(ramos)

#Otra forma de insertar un elemento a la lista (de forma especifica)
ramos.insert(0, "Introducción a la Matemática")
print(ramos)

#Modificar un elemento en especifico de una lista
ramos[2]= "Habilidades comunicativas para Ingenerieros/as"
print(ramos)

#Eliminar un elemento de la lista
ramos.pop()
print(ramos)

#Ordenar los elementos de una lista de forma descendente a ascendente
#print(ramos.sort()) /7no se puede realizar porque primero se debe instanciar y luego ejecutar el print
ramos.sort()
print(ramos)

n.sort()
print(n)

#Ordenar elementos de una lista segun la cantidad de caracteres de cada elemento
ramos.sort(key=len)
print(ramos)

#key es un propiedad de sort
#len se utiliza para contar los caracteres

#Metodo extend (extender una lista a partir de otra)
ramos_segundo_semestre = ["ciudadania", "algebra", "introducción a la fisica"]
print(ramos_segundo_semestre)
print(ramos)

#Aplicando metodo index
print(ramos_segundo_semestre.index("algebra"))
