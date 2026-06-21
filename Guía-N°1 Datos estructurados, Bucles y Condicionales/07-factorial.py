"""n! = n*(n-1)*(n-2)..,3*2*1

factorial(x) = {1                   si x = 0
                x * factorial(x-1)  si x >= 0 }2"""

def factorial(n):
    resultado = 1
    for i in range(1, n + 1):
        resultado *= i
    return resultado

print(factorial(5))

"""
Javiera ojeda
Diana Dusseaux
"""