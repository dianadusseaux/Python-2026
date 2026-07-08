entrada = input("Ingrese un valor entero: ") #El valor ingresado es un str

try:
    numero = int(entrada)
    print(f"Número ingresado: {numero}")
except ValueError: #error por tipo de dato
    print(f"Error de valor: el valor ingresado no es número entero")
except Exception as e: #errores genericos e inesperados
    print(f"Error inesperado{e}")
else:
    print("Conversión fue exitosa!")
finally:
    print("Finalización del bloque")