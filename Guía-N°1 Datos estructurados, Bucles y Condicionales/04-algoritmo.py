
n = int(input("Ingrese un numero para calcular el cubo: "))
impar_actual = 1

for i in range(1, n + 1):
    secuencia = []
    suma_fila = 0
    for sec in range(i):
        secuencia.append(str(impar_actual))
        suma_fila += impar_actual
        impar_actual += 2  
    operacion = " + ".join(secuencia)
    
    print(f"el cubo de {i} elevado a 3 es igual a la suma de {operacion} = {suma_fila}")