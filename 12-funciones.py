#La función se puede utilizar en cualquier momento 
print("=====FUNCION MULTIPLICACION=====")
def multiplicacion(x): #Multiplica cualquier valor por 10
    return x * 10

y = multiplicacion(7) #Y es igual a resultado y 5 es igual a la x
print(f"El resultado de la función es {y}")

print("=====FUNCION SALUDO=====")
def saludo(nombre):
    print(f"Hola, mi nombre es + {nombre}")

saludo("Diana")
#saludo: La llamada a la función, imprime "Hola, mi nombre es Diana"(Lo que esta dentro de la función)

#PRINCIPIOS DE LAS FUNCIONES
#1)Unica responsabilidad 
#cada funcion debe estar centrada en realizar una tarea especifica
#2)Simplicidad
#3)Nombre descriptivo
#Cada función debe tener un nombre caracteristico si esta multiplicando debe ser ese el nombre de la funcion

print("=====FUNCION SUMA=====")
def suma(a, b): #puedo pasar 2 o mas parametros
    return a + b

#Llamada a la función con argumentos posicionales: 2 + a, 3 + b
resultado = suma(2, 3) #E l orden si importa: a=2; b=3
print(resultado)

print("=====FUNCION RESTA=====")
#Definición de la función "resta" con parámetros por defecto (b = 5)
def resta(a, b=5): #b no necesariamente siempre es 5 solo que en este caso esta por defecto
    return a - b

#Caso 1: Utilizando solo el argumento obligatorio "a" (b tomará su valor por defecto: 6)
resultado1 = resta(6) #Equivalente a suma(6, 5)
print("Resultado 1 (b por defecto):", resultado1) # 6 - 5 = 1

#Caso 2: Pasando ambos argumentos (ignora el valor por defecto de "b")
resultado2 = resta(4, 4) # a = 4; b = 4
print("Resultado 2 (b personalizado):", resultado2) # 4 - 4 = 0

print("=====FUNCION POTENCIA=====")
def calcular_potencia(base, exponente):
    return base ** exponente

#Llamada con argumentos por nombre(el orden no importa)
resultado3 = calcular_potencia(exponente=3, base=2)
print(resultado3)

#Recursividad: es una función que se llama a ella misma resolviendo un problema diviendolo en casos pequeños
#Ejemplo es similar al metodo dividir y venceras
#caracteristicas(tiene caso base y caso recursivo)
#los casos recursivos son las divisiones para lograr resolver el caso base"""

print("=====CALCULO FACTORIAL=====")
#calculo factorial normal
def factorial_normal(n):
    r= 1
    i = 2
    while i <= n:
        r *= i
        i += 1
    return r

print(factorial_normal(5))

#calculo facotial con recursividad
def factorial_recursivo(n):
    if n == 1:
        return 1
    else:
        return n * factorial_recursivo(n-1)#En esta linea se llama a la función dentro de una función

print(factorial_recursivo(5))

#python limita a 1000 llamadas la recursividad

print("=====FIBONACCI=====")
#Fibonacci metodo recursivo
def fibonacci_recursivo(n):
    #casos base(o y 1)
    if n == 0:
        return 0
    elif n == 1:
        return 1
    #caso recursivo
    return fibonacci_recursivo(n-1) + fibonacci_recursivo(n-2)

#ejemplo: 5to numero de fibonacci(se empieza desde el 0)
print(f"5to Número de Fibonacci: {fibonacci_recursivo(5)}")

#Fibonacci metodo iterativo
def fibonacci_iterativo(n):
    #casos base (o y 1)
    a, b = 0, 1
    for _ in range(n):
        a, b = b, a + b #Se actualizan los valores
    return a

#ejemplo: 5to numero de fibonacci(se empieza desde el 0)
print(f"5to Número de Fibonacci: {fibonacci_iterativo(5)}")

