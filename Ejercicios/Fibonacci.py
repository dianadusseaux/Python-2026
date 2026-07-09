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