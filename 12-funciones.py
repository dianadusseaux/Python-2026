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




