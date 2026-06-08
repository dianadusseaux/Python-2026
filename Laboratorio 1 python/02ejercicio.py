codigo_identificador = input("Estudiante ingrese el codigo verificador por favor" )

codigo_identificador = codigo_identificador.strip()

codigo_identificador = (codigo_identificador.replace("_", ""))

codigo_final = codigo_identificador.upper()

largo_codigo_final = len(codigo_final)

print(f"El codigo final es: {codigo_final}")
print(f"la longitud en numero de caracteres es de: {largo_codigo_final}")