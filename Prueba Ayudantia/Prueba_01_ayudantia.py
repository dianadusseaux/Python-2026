#Ejercicio 1
print("=====Ejercicio número 1=====")
nombre = input("Ingrese su nombre y apellido por favor: ")
edad = input("Ingrese su edad por favor: ")
carrera = input("Ingrese su carrera por favor: ")
estatura = float(input("Ingrese su estatura pór favor: "))

print(f"Nombre: {nombre}\nEdad: {edad} años\nCarrera: {carrera}\nEstatura: {estatura} cm")

#Ejercicio 2
print("=====Ejercicio número 2=====")
utiles_escolares = ["Lapiz", "Goma", "Cuaderno"]

util1 = utiles_escolares[0]
util2 = utiles_escolares[1]
util3 = utiles_escolares[1]

print(f"El primer util escolar ingresado en la lista llamada utiles escolares es: {util1}")
print(f"El segundo util escolar ingresado en la lista llamada utiles escolares es: {util2}")
print(f"El tercer util escolar ingresado en la lista llamada utiles escolares es: {util3}")

#Ejercicio 3
print("=====Ejercicio número 3=====")
mis_notas = []
nota1 =float(input("Ingrese su primera nota por favor: "))
nota2 =float(input("Ingrese su segunda nota por favor: "))
nota3 =float(input("Ingrese su tercera nota por favor: "))
nota4 =float(input("Ingrese su cuarta nota por favor: "))
nota5 =float(input("Ingrese su quinta nota por favor: "))

mis_notas.append(nota1)
mis_notas.append(nota2)
mis_notas.append(nota3)
mis_notas.append(nota4)
mis_notas.append(nota5)
print(f"Las notas ingresadas son: {mis_notas}")

nota_maxima = max(mis_notas)
print(f"La nota maxima es: {nota_maxima}")
nota_minima = min(mis_notas)
print(f"La nota minima es: {nota_minima}")

nota_promedio = sum(mis_notas) / len(mis_notas)
round(nota_promedio, 2)
print(f"El promedio de las 5 notas ingresadas es de: {nota_promedio}")

