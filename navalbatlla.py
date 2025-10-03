import random

def generartablero():
    return [[" " for _ in range(5)] for _ in range(5)]

def ubicarbarcos(tablero, cantidad = 3):
    barcos = set()
    while len(barcos) < cantidad:
        fila = random.randint(0, 4)
        columna = random.randint(0, 4)
        if tablero[fila][columna] == " ":
            tablero[fila][columna] = "B"
            barcos.add((fila, columna))
    return barcos

def mostrartablero(tablero, ocultar = True):
    print("0 1 2 3 4")
    for idx, fila in enumerate(tablero):
        if ocultar:
            filamostrar = [" " if casilla == "b" else casilla for casilla in fila]
        else:
            filamostrar = fila
        print(f"{idx} {'|'.join(filamostrar)}")

def disparar(tablero, barcos):
    while True:
        try:
            fila = int(input("elegi una fila del 0 al 4"))
            columna = int(input("elegi una columna del 0 al 4"))
            if 0 <= fila < 5 and 0 <= columna < 5:
                if tablero[fila][columna] == "B":
                    print("le diste a un barco wacho")
                    tablero[fila][columna] = "X"
                    barcos.remove((fila, columna))
                    return True
                elif tablero[fila][columna] == " ":
                    print("le diste al agua")
                    tablero[fila][columna] = "O"
                    return False
                else:
                    print("ya disparaste ahi, elegi otra casilla")
            else:
                print("coordenadas fuera de rango")
        except ValueError:
            print("ingresa numeros validos")

def barcoshundidos(barcos):
    return len(barcos) == 0

def juego_batallanaval():
    tablero = generartablero()
    barcos = ubicarbarcos(tablero)
    print("bienvenido a la batalla naval")
    mostrartablero(tablero)

    while not barcoshundidos(barcos):
        disparar(tablero, barcos)
        mostrartablero(tablero)
    print("victoria, hundiste todos los barcos")

juego_batallanaval()
