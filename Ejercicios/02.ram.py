
manana = input(float("Ingrese el consumo de la mañana por favor"))
print(manana)

medio_dia = input(float("ingrese el consumo del medio dia por favor"))
print(medio_dia)

tarde = input(float("ingrese el consumo de la tarde por favor"))
print(tarde)

noche = input(float("ingrese el consumo de la noche por favor"))
print(noche)

ram = list([manana, medio_dia, tarde, noche])

consumo_manana = ram[0]

consumo_mediodia = ram[1]

consumo_tarde = ram[2]

consumo_noche = ram[3]

consumo = consumo_manana + consumo_mediodia + consumo_tarde + consumo_noche

promedio = consumo / len(ram)
print(f"El promedio de consumo de ram durante el dia es de {promedio}")
ram_maxima = max(ram)
ram_minima = min(ram)

rango_de_operacion = ram_maxima - ram_minima
print(f"La diferencia entre el consumo mas alto y mas bajo es de {rango_de_operacion}")



