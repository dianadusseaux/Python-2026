#a)inicialización del tablero
tablero = {
    #fila1
    "a1" : "TorreB",
    "a2" : "CaballoB",
    "a3" : "AlfilB",
    "a4" : "ReinaB",
    "a5" : "ReyB",
    "a6" : "AlfilB",
    "a7" : "CaballoB",
    "a8" : "TorreB",
    
    #fila2
    "b1" : "PeonB",
    "b2" : "PeonB",
    "b3" : "PeonB",
    "b4" : "PeonB",
    "b5" : "PeonB",
    "b6" : "PeonB",
    "b7" : "PeonB",
    "b8" : "PeonB",
    
    #fila3
    "c1" : ".",
    "c2" : ".",
    "c3" : ".",
    "c4" : ".",
    "c5" : ".",
    "c6" : ".",
    "c7" : ".",
    "c8" : ".",
    
    #fila4
    "d1" : ".",
    "d2" : ".",
    "d3" : ".",
    "d4" : ".",
    "d5" : ".",
    "d6" : ".",
    "d7" : ".",
    "d8" : ".",
    
    #fila5
    "e1" : ".",
    "e2" : ".",
    "e3" : ".",
    "e4" : ".",
    "e5" : ".",
    "e6" : ".",
    "e7" : ".",
    "e8" : ".",
    
    #fila6
    "f1" : ".",
    "f2" : ".",
    "f3" : ".",
    "f4" : ".",
    "f5" : ".",
    "f6" : ".",
    "f7" : ".",
    "f8" : ".",
    
    #fila7
    "g1" : "PeonN",
    "g2" : "PeonN",
    "g3" : "PeonN",
    "g4" : "PeonN",
    "g5" : "PeonN",
    "g6" : "PeonN",
    "g7" : "PeonN",
    "g8" : "PeonN",
    
    #fila8
    "h1" : "TorreN",
    "h2" : "CaballoN",
    "h3" : "AlfilN",
    "h4" : "ReinaN",
    "h5" : "ReyN",
    "h6" : "AlfilN",
    "h7" : "CaballoN",
    "h8" : "TorreN",
}

#b)Mapa de simbolos ASCII
simbolos = {
    #blancas
    "TorreB" : "R",
    "CaballoB" : "N",
    "AlfilB" : "B",
    "ReinaB" : "Q",
    "ReyB" : "K",
    "PeonB" : "P",
    
    #negras
    "TorreN" : "r",
    "CaballoN" : "n",
    "AlfilN" : "b",
    "ReinaN" : "q",
    "ReyN" : "k",
    "PeonN" : "p",
}

#c)Tablero dibujado
def mostrar_tablero(): #creando funcion |1=def, 2=nombre_de_funcion():, 3=codigo identado(dentro de la funcion)
    columnas = "abcdefgh"
    print(f"  {columnas}  ")
    print(f"8 {simbolos [tablero['h1']]}{simbolos [tablero['h2']]}{simbolos [tablero['h3']]}{simbolos [tablero['h4']]}{simbolos [tablero['h5']]}{simbolos [tablero['h6']]}{simbolos [tablero['h7']]}{simbolos [tablero['h8']]} 8")
    print(f"7 {simbolos [tablero['g1']]}{simbolos [tablero['g2']]}{simbolos [tablero['g3']]}{simbolos [tablero['g4']]}{simbolos [tablero['g5']]}{simbolos [tablero['g6']]}{simbolos [tablero['g7']]}{simbolos [tablero['g8']]} 7")
    print(f"6 {tablero['f1']}{tablero['f2']}{tablero['f3']}{tablero['f4']}{tablero['f5']}{tablero['f6']}{tablero['f7']}{tablero['f8']} 6")
    print(f"5 {tablero['e1']}{tablero['e2']}{tablero['e3']}{tablero['e4']}{tablero['e5']}{tablero['e6']}{tablero['e7']}{tablero['e8']} 5")
    print(f"4 {tablero['d1']}{tablero['d2']}{tablero['d3']}{tablero['d4']}{tablero['d5']}{tablero['d6']}{tablero['d7']}{tablero['d8']} 4")
    print(f"3 {tablero['c1']}{tablero['c2']}{tablero['c3']}{tablero['c4']}{tablero['c5']}{tablero['c6']}{tablero['c7']}{tablero['c8']} 3")
    print(f"2 {simbolos [tablero['b1']]}{simbolos [tablero['b2']]}{simbolos [tablero['b3']]}{simbolos [tablero['b4']]}{simbolos [tablero['b5']]}{simbolos [tablero['b6']]}{simbolos [tablero['b7']]}{simbolos [tablero['b8']]} 2")
    print(f"1 {simbolos [tablero['a1']]}{simbolos [tablero['a2']]}{simbolos [tablero['a3']]}{simbolos [tablero['a4']]}{simbolos [tablero['a5']]}{simbolos [tablero['a6']]}{simbolos [tablero['a7']]}{simbolos [tablero['a8']]} 1")
    print(f"  {columnas}  ")
mostrar_tablero ()

def procesar_movimiento(origen,destino,capturadas):
    if origen not in tablero:
        print("Error")
        return


#d)Interacción con el usuario

capturadas = []

while True:
    mostrar_tablero()
    origen = input("Ingrese la casilla de origen o salir para terminar: ")
    if origen.lower() == 'salir':break
    destino = input("Ingrese la casilla de destino: ")
procesar_movimiento(origen,destino,capturadas)

pieza_origen = tablero[origen]
pieza_destino = tablero[destino]

if pieza_destino != ".":
    capturadas.append(pieza_destino)
print(f"¡Capturo a pieza {pieza_destino} en {destino}!")

tablero[destino] = pieza_origen
tablero[origen] = "."

print(f"piezas capturadas{capturadas}")


"""
Javiera ojeda
Diana Dusseaux
"""

