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

"""Algoritmo temperaturacelsius
	Definir celsius, fahrenheit Como Real
	Escribir "Ingrese la temperatura en grados celsius"
	Leer celsius
	Fahrenheit <- (celsius * 1.8) + 32//no se utiliza coma en decimal se ocupa un "punto"
	Escribir "La temperatura de grados celcius a fahrenheit es:" Fahrenheit "°F"
	
FinAlgoritmo
"""
temperatura_c = input("usuario ingrese la temperatura en grados celsius para transformar a fahrenheit")
fahrenheit = (float(temperatura_c) * 1.8) + 32
print(f"la temperatura es: , {fahrenheit} la cual equivale a la temperatura anterior en celsius que era{temperatura_c}")

