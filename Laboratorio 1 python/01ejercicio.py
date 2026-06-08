muestra1 = (float(input("Ingrese las precipitaciones de la muestra numero 1: ")))
muestra2 = (float(input("Ingrese las precipitaciones de la muestra numero 2: ")))
muestra3 = (float(input("Ingrese las precipitaciones de la muestra numero 3: ")))
muestra4 = (float(input("Ingrese las precipitaciones de la muestra numero 4: ")))
muestra5 = (float(input("Ingrese las precipitaciones de la muestra numero 5: ")))

registro_lluvia = (list([muestra1 , muestra2, muestra3, muestra4, muestra5]))

registro_lluvia1 = (registro_lluvia[0])
registro_lluvia2 = (registro_lluvia[1])
registro_lluvia3 = (registro_lluvia[2])
registro_lluvia4 = (registro_lluvia[3])
registro_lluvia5 = (registro_lluvia[4])

promedio_registro_lluvia = (registro_lluvia1 + registro_lluvia2 + registro_lluvia3 + registro_lluvia4 + registro_lluvia5) / len(registro_lluvia)

registro_lluvia_min = min(registro_lluvia)
registro_lluvia_max = max(registro_lluvia)

brecha_pluvial = (registro_lluvia_max - registro_lluvia_min)

print(f"Los valores entregados de registro de lluvia durante el dia son: {registro_lluvia}")
print(f"El promedio de los 5 valores entregados es de: {promedio_registro_lluvia}")
print(f"La brecha pluvial entre el valor maximo y el valor minimo es de: {brecha_pluvial}")