"""Al desarrollar sistemas inform´aticos, los usuarios suelen ingresar datos con espacios
accidentales o formatos incorrectos. El sistema de la biblioteca de la ULagos recibi´o el
RUT de un estudiante, pero viene “sucio” con espacios al inicio, al final y con puntos
intermedios: “ 19.543.872-K ”..."""

#a) Guarde el RUT original en una variable de tipo string.

rut = " 19.543.872-k "

"""b) Utilice el metodo propio de Python para eliminar los espacios en blanco de los
extremos."""

rut_sin_espacio = rut.strip() #quta los espacios / slit separa en lista

#c) Utilice un m´etodo propio de Python para eliminar los puntos (.).
rut_final = rut_sin_espacio.replace(".","")


"""d) Calcule el largo total del RUT ya limpio (sin espacios ni puntos) y muestre el
resultado por pantalla junto al RUT con su nuevo formato."""


largo_de_rut = len(rut_final)

print(f"largo del rut = {largo_de_rut} / rut: {rut_final}")
