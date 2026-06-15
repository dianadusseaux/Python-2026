laboratorio_1 = (float(input("Usuario ingrese la nota número 1 por favor: "))) #40%
laboratorio_2 = (float(input("Usuario ingrese la nota número 2 por favor: "))) #40%
laboratorio_3 = (float(input("Usuario ingrese la nota número 3 por favor: "))) #20%

notas = (list([laboratorio_1, laboratorio_2, laboratorio_3 ]))

promedio_nota1 = (notas[0])
promedio_nota2 = (notas[1])
promedio_nota3 = (notas[2])


ponderado_final = ((promedio_nota1[0]*0.4)+(promedio_nota2[1]*0.4)(promedio_nota3[2]*0.2))

print(f"Los valores de las notas entregadas son: {notas}")
print(f"El promedio final de todas las notas entregadas es: {ponderado_final}")