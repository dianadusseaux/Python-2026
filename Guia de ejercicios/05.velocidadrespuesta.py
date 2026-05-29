lectura_tiempo1 = input(float("Administrador ingrese el tiempo de respuesta numero1"))
lectura_tiempo2 = input(float("Administrador ingrese el tiempo de respuesta numero2"))
lectura_tiempo3 = input(float("Administrador ingrese el tiempo de respuesta numero3"))

tiempos_respuestas = []
tiempos_respuestas.append(lectura_tiempo1)
tiempos_respuestas.append(lectura_tiempo2)
tiempos_respuestas.append(lectura_tiempo3)
print(tiempos_respuestas)

tiempos_promedio = (tiempos_respuestas[0] + tiempos_respuestas[1] + tiempos_respuestas[2]) / len(tiempos_respuestas)

min_tiempo = min(tiempos_respuestas) #mas rapido
max_tiempo = max(tiempos_respuestas) #mas lento

brecha_tiempo = (max_tiempo - min_tiempo)

print(f"A continuacion la lista completa de los tiempos de respuesta y datos: \n Tiempo de respuesta: {tiempos_respuestas} \n Tiempo promedio: {tiempos_promedio} \n Tiempo de la brecha: {brecha_tiempo}")