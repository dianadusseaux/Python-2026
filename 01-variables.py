nombre = "Diana"
apellido = "Dusseaux"
edad = "22"

#comentario en una linea
"""comentario en
varias lineas"""

"""tupla() no contiene datos repetidos
lista[] 
diccionario[]"""

"""{}=Llaves
[]=Llaves cuadradas o corchetes
()Parentesis
str es una funcion que cambia un valor a texto
input=se utiliza para que la persona escriba la información
metodo=funcion (ambas son funciones predeterminadas)
para guardar la información debemos creer una variable"""

#formas de imprimir texto

#forma 1 clasica separando variables y texto por comas
print("mi nombre es", nombre, apellido,"mi edad es", edad)

#forma 2 utilizando f=string
print(f"mi nombre es {nombre} y mi apellido es {apellido} y tengo {edad} años")

#forma 3 concatenación(utilizando en operador +)
print("mi nombre es" + nombre + "y mi apellido es" + apellido + "y tengo" + str(edad) + "años")

#utilizando el metodo input y creando una variable llamada carrera
carrera = input("¿Que carrera estudias?")

