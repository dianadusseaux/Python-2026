from colorama import init, Fore
init() #inicializando paquete colorama

print(Fore.YELLOW + '=====BUCLES=====')

#Bucle while
edad = 15
num = 0

#Bucle infinito
#while edad < 18:  
#    print("Eres menor de edad, no puedes manejar")

#Bucle infinito N°2
#while True:
#    print(num)
#    num+-2 ==> es lo mismo que num+- 2

#Bucle while
#Impresión de numeros de 0 al 100(incrementando de 2 en 2)

while num <= 100:
    print(num)
    num += 2
print(Fore.RED + "Primer bucle terminado")

#Impresión de numeros de 100 al 200 + condición ELSE
#El else esta al nivel del while
while num<= 200:
    print(num)
    num += 2
else:
    print("Mi condición es igual o mayor a 200")
print(Fore.CYAN + "Segundo bucle terminado")
#Con while no funciona el elif

#Combinar while con un if dentro
while num <= 300:
    print(num)
    num += 2
    if num == 250:
        print("Mi condición es igual a 250")
print(Fore.GREEN + "Tercer bucle terminado!")

#Utilizando el break
#La palabra break quiebra un bucle solo se puede utilizar en conjunto con el while
while num <=400:
    print(num)
    num += 2
    if num == 350:
        print(Fore.MAGENTA + "Se detiene el bucle")
        break
print(num)
print(Fore.MAGENTA + "Cuarto bucle terminado!")

#Utilizando el continue
num = 0 #se recetea num

while num <= 50:
    print(num)
    num += 1
    if num == 40:
        continue
    print(num)

#Bucle infinito controlado + Break
"""while True:
    parametro = input(">>> Ingrese la palabra secreta: ")
    if parametro == "exit":
        break
    else:
        print(parametro)"""

#Bucle FOR
#FOR N°1
print(Fore.GREEN + "===== BUCLES FOR =====")
for i in (1,2,3,4,5,6,7,8,9,10):
    print(i)

print(Fore.CYAN + "\n2° Bucle For")

#Iterando una lista (2do FOR)
listita = [1,2,3,4,5,6,7,8,9,10]

for i in listita:
    print(i)

print(Fore.MAGENTA + "\n3° Bucle For")

#Iterando de una tercera forma (3°FOR)
for i in range(1,101):
    print(i)












