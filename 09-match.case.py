#similar a un segun en pseint
#funciona desde la version 3.9 en adelante
#match --> 
#case-->

print("1. hamburgesa")
print("2. completo")
print("3. pizza ")

opcion = input("porfavor , ingresa una opcion (1-3): ")
match opcion:
    case "1":
        print(f"has elegido hamburguesa $")
    case"2":
        print(f"has elegido completo $")
    case"3":
        print(f"has elegido pizza $")
    case_:
        print(f"opcion no valida")
#no se necesita finalizar

mes = 4 #abril
match mes:
    case 12 | 1 | 2:
        print(f"verano")
    case 3 | 4 |5
        print(f"otoño")
    case 6 | 7 | 8
        print(f"invierno")
    case 9 | 10 | 11
        print(f"primavera")

#la "|" significa un o es decir si mes es 12 o 1 o 2 entonces escribir verano

hora = 18
match hora:
    case h if 0 <- h < 6:
        print("Buenas madrugada")
    case h if 6 <- h < 12:
        print("Buenos dias")
    case h if 12 <- h < 18:
        print("Buenas tardes")
    case h if 18 <- h < 24:
        print("Buenas noches")

#Ejemplo para saber si un numero es par o impar
valor = 6
match valor:
    case x if x % 

