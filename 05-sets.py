#SERTS (CONJUNTOS)

#CREANDO LOS PRIMEROS CONJUNTOS (DE DOS FORMAS DIFERENTES)
colores_primarios = {"azul", "rojo", "amarillo"}
colores_secundarios = set({"naranja", "verde", "violeta"})
print(type(colores_primarios))

print(f"CONJUNTO 1: {colores_primarios}")
print(f"CONJUNTO 2: {colores_secundarios}")

#CREANDO UN CONJUNTO NUEVO
colores_nuevos = {"azul", "rojo", "celeste", "azul", "rojo"}
print(f"CONJUNTO 3: {colores_nuevos}")
#en los sets no se consideran duplicados
#los sets no se pueden ordenar porque no tienen posicion como la lista o la tupla 
#cada vez que se ejecute en el terminal arrojara diferentes posiciones del contenido al interior del sets

#AGREGANDO UN NUEVO ELEMENTO AL SET colores_nuevos.add()
colores_nuevos.add("cafe")
print(f"CONJUNTO 3 ACTUALIZADO: {colores_nuevos}")

#ELIMINANDO UN ELEMENTO DEL SET DE colores_nuevos.discard()
colores_nuevos.discard("cafe")
print(f"CONJUNTO 3 ACTUALIZADO SIN EL COLOR CAFE: {colores_nuevos}")

#APLICANDO EL METODO INTERSECTION()
interseccion = colores_primarios.intersection(colores_nuevos)
print(f"CONJUNTO INTERSECTADO: {interseccion}")

#interseccion se realiza mediante los elementos comunes de ambos sets 

