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