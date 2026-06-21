parrafo = tuple("El Proyecto Integrador del primer semestre, se evaluara y desarrollara en 3 asignaturas en conjunto: Taller de Introduccion a la Ingenieria donde trabajaran el desarrollo practico del proyecto, Habilidades Comunicativas donde desarrollaran las habilidades de presentacion y redaccion y por ultimo Programacion, donde aplicaran tecnicas para codificar y disenar el software del proyecto.")

parrafo_nuevo = "".join(parrafo)
print(parrafo_nuevo)
# Reemplazamos las comas y puntos por nada (los eliminamos)
parrafo_nuevo = parrafo_nuevo.replace(",", "").replace(".", "").replace(":", "")
parrafo_nuevo = parrafo_nuevo.split()
palabra = input("Ingrese la palabra que desee buscar: ")
if palabra in parrafo_nuevo:
    print(f"La palabra “{palabra}” se encuentra {parrafo_nuevo.count(palabra)} vez/veces")
else:
    print("Esa palabra no esta en el texto")

"""
Javiera ojeda
Diana Dusseaux
"""