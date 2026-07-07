#a) crear un diccionario con la variable censo_2017
censo_2017 = {
    14 : {
        "Nombre Región" : "Los_Rios" ,
        "Superficie" : 18429 ,
        "Habitantes" : 404432 ,
    },
    
    12 : {
        "Nombre Región" : "Magallanes",
        "Superficie" : 1382291,
        "Habitantes" : 166533,
    }
}

print(f"El diccionario inicial es: {censo_2017}")

#b) calcular la densidad poblacional

#for i in censo_2017:

#densidad poblacional = habitantes/superficie
densidadl = float(round((censo_2017["14"]["Habitantes"])/(censo_2017["14"]["Superficie"]),3))
print(f"La densidad poblacional de la región de Los Rios es de: {densidadl}")

densidadm = float(round((censo_2017["12"]["Habitantes"])/(censo_2017["12"]["Superficie"]),3))
print(f"La densidad poblacional de la región de Magallanes es de: {densidadm}")

#c) agregar capitales

censo_2017[14] = ["Capital"] = "Valdivia"
censo_2017[14] = ["Comunas"] = [Rio Bueno, La Unión, Paillaco]
censo_2017[14] = ["Coordenadas_simuladas"] = (23.5 , 85.6)
censo_2017[14] = ["Zonas_exclusivas"] = {"Urbana" , "Rural" , "Fronteriza"}

censo_2017[12] = ["Capital"] = "Punta Arenas"
censo_2017[12] = ["Comunas"] = [Cabo de Hornos, Puerto Williams, Porvenir]
censo_2017[12] = ["Coordenadas_simuladas"] = (69.7 , 96.9)
censo_2017[12] = ["Zonas_exclusivas"] = {"Urbana" , "Rural" , "Fronteriza"}
print(f"{censo_2017}")


#d)cambiar el nombre magallanes
censo_2017[12]["Nombre Región"] = ["Magallanes y Antártica Chilena"]

#e)menu interactivo
#que solicite al usuario ingresar por teclado el ID 12 o 14 para consultar comunas

while True:
    menu = int(input("Ingrese por favor la ID siendo 14 la Región de Los Ríos y 12 la Región de magallanes (en caso de no querer ingresar la ID ingrese el número 0): "))
    if menu == 12:
        print(f"Las comunas de la Región de los rios son: Rio bueno, La Unión, Paillaco")
        
    elif menu == 14:
        print(f"Las comunas de la Región de Magallanes son: Cabo de Hornos, Puerto Williams, Porvenir")
        
    elif menu == 0:
        print(f"Entendido, que tenga buen dia!")
        break
    else:
        print(f"Seleccione 12, 14 o 0")
        

#f)Imprimir el diccionario en una tupla
print(f"Los valores finales del diccionario son: {censo_2017.items()}")
