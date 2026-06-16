from colorama import init, Fore
init() #inicializando paquete colorama

print(Fore.RED + 'texto Rojo')
print(Fore.MAGENTA + 'texto magenta')
print(Fore.BLUE + 'texto Azul')
print(Fore.YELLOW + 'texto Amarillo')

#Condicional IF
print(Fore.MAGENTA + "\n===== UTILIZANDO IF Y ELSE =====")

#Declarando variables
licencia = False
edad = 17
automovil = True

if licencia and edad >=18:
    print(Fore.YELLOW + "Puede conducir un automovil ya que es mayor de edad y tiene licencia")
else:
    print(Fore.YELLOW + "No puede conducir porque no es mayor de edad y no tiene licencia")

if licencia and edad >=18:
    print(Fore.CYAN + "Puede conducir un automovil ya que es mayor de edad y tiene licencia")
elif automovil:
    print(Fore.BLUE + "Tengo automovil pero no tengo licencia ni la edad necesaria para conducir")
else:
    print(Fore.RED + "No puedo conducir, ya que no tengo la edad, ni la licencia y tampoco automovil")

