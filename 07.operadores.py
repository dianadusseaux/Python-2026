#operadores en python
a = 10
b = 5
c = 4
d = 10

print("--- OPERADORES ARITMETICOS ---")
print(f"La suma entre la variable a y b es: {a + b}") #operador de suma
print(f"La resta entre la variable a y b es: {a - b}") #operador de resta
print(f"La multiplicación entre la variable a y b es: {a * b}") #operador de producto
print(f"La división entre la variable a y b es: {a / b}") #operador de división
print(f"La módulo entre la variable a y b es: {a % b}") #operador de módulo
print(f"La coeficiente entre la variable a y b es: {a // b}") #operador de división entera 
print(f"El resultado de b elevado a c (5^4): {b ** c}") #operador de potencia -> pow() hace lo mismo

# ¿Se puede hacer esta operación?
print("Hola" * (int((10*2) / 5)), "\n")

print("--- OPERADORES DE COMPARACIÓN ---") #La salida es un booleano (true o false)
print(a == b) #operador de igualdad
print(a |= b) #operador desigual, distinto o diferente
print(a > b) #operador mayor que
print(a < b) #operador menor que
print(a >= b) #operador mayor o igual que
print(a <= b) #operador menor o igual que 

print("\n===OPERADORES LÓGICOS===")
"""Trabajaremos con el siguiente ejemplo: 
Tenemos un vehículo que tiene bencina (variable bencina) y una opción que dice 
si esta encendido o no el vehiculo (variable encendido). 
Dependiendo del estado de cada variable, se irá cambiando por False o True.
"""

#variables booleanas
bencina = True
encendido = True
#edad = 19

#if = si
#else = sino

#utilizando el operador AND
if bencina and encendido:
    print("El vehiculo puede arrancar")
else:
    print("El vehiculo no puede arrancar")
    
#utilizando el operador OR
if bencina or encendido:
    print("El vehiculo puede arrancar")
else:
    print("El vehiculo no puede arrancar")



