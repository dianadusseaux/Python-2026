#DICCIONARIOS

# Primera forma de declarar diccionario
paciente = {
    "nombre" : "Lorena",
    "edad" : 29,
    "ciudad" : "Ancud",
    "fechas_atencion" : [5,8,12],
    "diagnostico" : ("resfrio comun"),
    "informacion_extra" : {
        "tipo_de_sangre" : "A+",
        "hemograma" : False
    }
} #Es recomendable usar los diccionarios con espaciado para no confundirlos con sets

# Segunda forma de declarar diccionario
medico = dict(
    nombre = "Diana",
    edad = 21,
    especialidad = "Cardiologo"
)

print(type(paciente))
print(f"===FICHA PACIENTE=====\n{paciente}\n")
print(f"===FICHA medico=====\n{medico}\n")

# CONSULTA DE INFORMACION A DICCIONARIOS

# ¿Como consulto el nombre del paciente sin traer el diccionario completo?
print(f"Nombre del paciente a consultar: {paciente["nombre"]}") # A diferencia de las listas se busca desde el nombre de la clave  

# Metodo get() obtiene el valor de una clave, si no existe retorna None (o un valor por defecto)
print(paciente.get("Nombre"))
print(paciente.get("rut", "N/D (No data)"))

# Retornar las claves, los valores o ambas como pares
print(paciente.keys()) # dict_keys(["nombre","edad",....]) ->solo claves
print(paciente.values()) # dict_values(["nombre","edad",....]) ->solo valores
print(paciente.items()) # dict_items(["nombre","edad",....]) ->so

#retorna el numero  de claves que tiene
print(len(medico))
print(len(paciente))

# MODIFICACION DEL DICCIONARIO
# Agregar una clave nueva al diccionario por paciente
paciente["telefono"] = "+56934568669"
print(f"=====FICHA PACIENTE=====\n{paciente}\n")

# Sobrescribir valor de una clave
# Forma 1
paciente["edad"] = 20
print("\n=====FICHA PACIENTE CON  EDAD ACTUALIZADA=====\n")
print(paciente)

# Fusiona otro diccionario (o pares clave-valor) en el actual
# Util para actualizar varios campos a la vez (actualizar varias claves)
paciente.update({"edad":21,"ciudad": "Castro"})
print(paciente["edad"])
print(paciente["ciudad"])
print(f"=====FICHA PACIENTE CON  EDAD ACTUALIZADA=====\n{paciente}")

# Eliminar una clave sin retorno
del(paciente["informacion_extra"])
print(f"=====FICHA PACIENTE=====\n{paciente}")
# Eliminar una clave y retornar su valor (a diferencia de del, que no la retorna) -> pop()
edad_eliminada = paciente.pop("edad")
print(f"Edad eliminada: {edad_eliminada}") # Se recupera el valor antes de eliminarla
print(f"=====FICHA PACIENTE=====\n{paciente}")

# OTRAS UTILIDADES DEL DICCIONARIO

# Con in se verifica si una clave existe en el diccionario (sin usar condicionales todavia)
print("nombre" in paciente)
print("rut" in paciente)

# Con copy() se crea una copia independiente del diccionario
paciente2 = paciente.copy()
paciente2["nombre"] = "BBBB"
print(paciente["nombre"])
print(paciente2["nombre"])
print(paciente2)

# Con clear() elimina todos los elementos del diccionario, dejandolo vacio (aun existe pero esta vacio)
medico2 = medico.copy()
print(medico2)
medico2.clear()
print(medico2) # ->{}

#el diccionario siempre es un par clave, valor 

#controles = {} esto es un diccionario vacio

#para indentar son 4 espacios

#funciones con datos iterables ej: map(funcion,iterable)
#funcion join sirve para unir 

n = [1, 2, 3, 4, 5] #la funcion map sirve para reemplazar un for
n_str = list(map(str,n))
print(f"Lista de numeros como strings: {",".join(n_str)}")

filter() #sirve para filtrar
lambda #es una función directa
zip() #toma 2 o mas iterables y los combina en un solo iterable de tuplas(siempre los va a transformar en una tupla)

#metodos para datos iterables
#01-funcion_zip
a = [1, 2, 3, 4, 5]
b = ["A", "B", "C", "D"]

comprimir = list(zip(a,b))

