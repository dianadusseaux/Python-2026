islas = {
    15:{
        "capital": "chiloe",
        "poblacion": 1425,
        "superficie": 12654,
    },
    14:{
        "capital": "castro" ,
        "poblacion": 2145,
        "superficie": 75454,
    }
}

print(f"Los datos del diccionario son: {islas}")

densidad_15 = (round(islas[15]["poblacion"])/(islas[15]["superficie"]))
print(f"La densidad de el diccionario 15 es: {densidad_15:.3f}")

densidad_14 = (round(islas[14]["poblacion"])/(islas[14]["superficie"]))
print(f"La densidad de el diccionario 14 es: {densidad_14:.3f}")
# escribir el 3f esta restrigiendo la salidad de 3 decimales

# Agregar nuevos elementos
islas[15]["comunas"] = "chonchi"
islas[15]["supermercado"] = ["belen", "la rotonda", "economar"]
islas[15]["plaza"] = {"castro","chonchi","dalcahue"}
islas[15]["habitantes"] = (25154)

print(f"Los valores finales del diccionario son: {islas.items()}")

utiles_escolares = ["goma", "lapiz", "cuaderno", "goma", "cuaderno"]
utiles_escolares.append("correcto")
utiles_escolares.remove("goma")
utiles_escolares = sorted(utiles_escolares)
unica = list(set(utiles_escolares))

duplicada = utiles_escolares.copy()

print(f"La lista de utiles escolares es: {utiles_escolares}")
print(f"{unica}")
print(f"{duplicada}")