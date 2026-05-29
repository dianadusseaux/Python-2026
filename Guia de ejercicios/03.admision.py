"""3. El Departamento de Admisi´on de la Universidad requiere un script b´asico para registrar
correos institucionales. El programa debe solicitar al usuario que ingrese su nombre
completo por terminal. Debido a que los usuarios pueden escribir con may´usculas y
min´usculas desordenadas o con espacios de m´as, el programa debe estandarizar el texto.
Escribe un programa que:"""

#a) Solicite por terminal el nombre del estudiante.
nombre_estudiante = input("usuario ingrese su nombre completo, separando su nombre y apellidos con espacios")

#b) Remueva los espacios sobrantes de los extremos.
nombre_estudiante = nombre_estudiante.strip()

#c) Convierta todo el texto a min´usculas.
nombre_estudiante = nombre_estudiante.lower()

"""d) Reemplace los espacios intermedios por puntos (.) para simular la estructura de
un correo electr´onico.
"""
nombre_estudiante = nombre_estudiante.replace(" ",".")

"""e) Muestre en pantalla el resultado final con el texto @alumnos.ulagos.cl concatenado
al final."""

print(nombre_estudiante + "@alumnos.ulagos.cl")