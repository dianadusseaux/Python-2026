sueldo_base = 529000

#a) Crear un diccionario con nombres y valores instanciados
ventas_vendedores = {
    "Pedro" : [300000 , 400000, 250000, 320000, 280000],
    "Juan" : [250000, 270000, 310000, 120000, 290000],
    "Diego" : [120000 , 100000, 180000, 140000, 200000],
}


total_ventas_pedro = sum(ventas_vendedores["Pedro"])
total_ventas_juan = sum(ventas_vendedores["Juan"])
total_ventas_diego = sum(ventas_vendedores["Diego"])

#bono1 = 0.20
#bono = 0.10
#bono3 = 0.05


#b) ventas totales + bono que corresponde

if total_ventas_pedro >= 1500000:
    bono_porcentaje_pedro = 0.20
elif total_ventas_pedro >= 1000000:
    bono_porcentaje_pedro = 0.10
elif total_ventas_pedro >= 500000:
    bono_porcentaje_pedro = 0.05

monto_bono_pedro = sueldo_base * bono_porcentaje_pedro

if total_ventas_juan >= 1500000:
    bono_porcentaje_juan = 0.20
elif total_ventas_juan >= 1000000:
    bono_porcentaje_juan = 0.10
elif total_ventas_juan >= 500000:
    bono_porcentaje_juan= 0.05

monto_bono_juan = sueldo_base * bono_porcentaje_juan

if total_ventas_diego >= 1500000:
    bono_porcentaje_diego = 0.20
elif total_ventas_diego >= 1000000:
    bono_porcentaje_diego = 0.10
elif total_ventas_diego >= 500000:
    bono_porcentaje_diego = 0.05

monto_bono_diego = sueldo_base * bono_porcentaje_diego

#c) promedio ventas semanales
promedio_pedro = total_ventas_pedro / 5
promedio_juan = total_ventas_juan / 5
promedio_diego = total_ventas_diego / 5

sueldo_pedro = sueldo_base + monto_bono_pedro
sueldo_juan = sueldo_base + monto_bono_juan
sueldo_diego = sueldo_base + monto_bono_diego

#d)Imprimir los sueldos que le corresponden a cada vendedor
print(f"-------El sueldo de cada vendedor-------")
print(f"El sueldo que le corresponde a Pedro es de: ${sueldo_pedro}")
print(f"El sueldo que le corresponde a Juan es de: ${sueldo_juan}")
print(f"El sueldo que le corresponde a Diego es de: ${sueldo_diego}")


"""
Javiera ojeda
Diana Dusseaux
"""