"""4. En f´ısica de part´ıculas, la precisi´on de los decimales es cr´ıtica. Un sensor de presi´on
hidr´aulica en un laboratorio de la universidad entrega una medida de 1024.7689 Pascales como tipo float. Escribe un programa que realice lo siguiente:"""

#a) Defina la variable con el valor del sensor




"""b) Convierta dicho valor a un n´umero entero (int), descartando los decimales, y
almac´enelo en una variable nueva."""



"""c) Utilice un m´etodo propio de Python para redondear el valor original del sensor a
exactamente 2 decimales y guarde el resultado en otra variable."""




"""d) Imprima un mensaje comparativo que muestre por terminal: el valor original, el
valor truncado como entero y el valor redondeado."""


valor_sensor = 1024.7689
valor_sensor_entero = int(valor_sensor)
valor_sensor_redondeado = round(valor_sensor,2) #round es la funcion que permite redondear el numero

print(f"A continuación se mostraran los valores que ha entregado el sensor \n valor original(inicial): {valor_sensor}  \n Valor del sensor pero entero: {valor_sensor_entero} \n Valor del sensor redondeado: {valor_sensor_redondeado}")

