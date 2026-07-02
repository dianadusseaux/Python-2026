conceptos_repetidos = ["inmutable", "iterable", "inmutable", "hashable", "interpretado", "iterable"]
conceptos = list(set(conceptos_repetidos))
print([conceptos])


glosario ={
    "hashable" : "Objeto cuyo valor hash nunca cambia y puede ser clave.",
    "inmutable": "Objeto con un valor fijo que no se puede modificar.",
    "interpretado": "Lenguaje donde el código se ejecuta línea a línea.",
    "iterable": "Objeto capaz de devolver sus elementos uno a la vez.",
}

busqueda = input("Usuario ingrese un concepto a buscar: ")
resultado = (glosario[busqueda])
print(f"{resultado}")

registro_busqueda = {resultado}

print(f"(registro_busqueda)")

#Javiera Ojeda, Diana Dusseaux

