
nombre_estudiante = input("usuario ingrese su nombre completo, separando su nombre y apellidos con espacios")

nombre_estudiante = nombre_estudiante.strip()

nombre_estudiante = nombre_estudiante.lower()

nombre_estudiante = nombre_estudiante.replace(" ",".")

print(nombre_estudiante + "@alumnos.ulagos.cl")