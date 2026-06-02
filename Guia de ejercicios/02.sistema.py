
rut = " 19.543.872-k "

rut_sin_espacio = rut.strip() #quta los espacios / slit separa en lista

rut_final = rut_sin_espacio.replace(".","")

largo_de_rut = len(rut_final)

print(f"largo del rut = {largo_de_rut} / rut: {rut_final}")
