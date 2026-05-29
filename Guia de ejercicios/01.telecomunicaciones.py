"""En el analisis de antenas y redes de telecomunicaciones, la impedancia de una linea de
transmision se compone de una parte real (resistencia) y una parte imaginaria (reactancia). Un ingeniero necesita calcular la impedancia total sumando los componentes
de dos tramos de la red de fibra optica de la universidad."""


"""a) Defina la impedancia del Tramo 1 como un numero complejo con parte real 50 y
parte imaginaria 30 (50 + 30j)."""

impadencia1 = 50 + 30j

"""b) Defina la impedancia del Tramo 2 de la misma forma, con parte real 40 y parte
imaginaria −10 (40 − 10j).
"""
impadencia2 = 40 - 10j

#c) Calcule la impedancia total sumando ambos tramos.

sumaimpadencia = impadencia1 + impadencia2

"""d) Muestre en pantalla la impedancia total, y luego imprima por separado solo la
parte real (convertida a n´umero entero int) y la parte imaginaria (convertida a
int) usando los atributos .real y .imag.
"""
#parte real
impadenciareal = int(sumaimpadencia.real)

#parte imaginaria
impadenciaimag = int(sumaimpadencia.imag)