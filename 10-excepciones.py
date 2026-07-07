entrada = input("Ingrese un valor entero: ") #El valor ingresado es un str

try:
    numero = int(entrada)
    print(f"Número ingresado: {numero}")
except ValueError