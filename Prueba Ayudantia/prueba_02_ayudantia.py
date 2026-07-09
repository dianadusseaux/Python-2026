##list(set())
print(f"=====Prueba 2=====")
print(f"=====Ejercicio 1=====")
# Guardar los productos vendidos en una lista
producto = ["pan","leche","pan","queso","leche","jugo","pan"]

#a) Muestre cuantoa productos fueron ingresandos en total
productos_contados = len(producto)
print(f"Cantidad total de productos ingresados: {productos_contados}")

#b)Eliminar preductos repetidos
productos_sin_repetir = list(set(producto))
print(f"La lista sin productos repetidos es: {productos_sin_repetir}")

#c)Recorra el set e imprima cada producto
for i in productos_sin_repetir:
    print(productos_sin_repetir)
    break

#d)Indique si el jugo fue vendido o no utilizando condicional

while True:
    vendido = input("Indique por favor si el jugo fue vendido (si o no): ")
    if vendido == si:
        print(f"El jugo fue vendido!")
    elif vendido == no:
        print(f"El jugo aun no es vendido")
        break
    else:
        print(f"Respuesta no valida, ingrese si o no")

print(f"=====Ejercicio 2=====")

notas = {
    "ana" : 6.2,
    "luis": 4.8,
    "pedro" : 3.9,
    "sofia" : 5.5
}

#a) Recorra el diccionario mostrando el nombre y nota de cada estudiante
for i in notas:
    print(notas)

#b) indique si el estudiante esta aprobado o reprobado

if notas >= 4.0:
    print(f"Felicidades usted a aprobado!")
elif notas <= 3.9:
    print("Usted esta reprobado")

#c) Indique cuantos alumnos fueros aprobados



