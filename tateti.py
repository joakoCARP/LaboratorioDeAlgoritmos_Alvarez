def crear():
    return [[" " for _ in range(3)] for _ in range(3)]

def mostrar(tablero):
    print("\n  0 1 2")
    for idx, fila in enumerate(tablero):
        print(f"{idx} {'|'.join(fila)}")

def ganador(tablero, jugador):
    for i in range(3):
        if all(tablero[i][j] == jugador for j in range(3)) or all(tablero[j][i] == jugador for j in range(3)):
            return True
    if all(tablero[i][i] == jugador for i in range(3)) or all(tablero[i][2-i] == jugador for i in range(3)):
        return True
    return False

def tablerolleno(tablero):
    return all(tablero[i][j] != " " for i in range(3) for j in range(3))

while True:
    tablero = crear()
    turno = "X"
    ganador = None

    print("bienvenido al tateti")
    mostrar(tablero)

    while True:
        print(f"turno de {turno}")
        fila = int(input("elegi una fila del 0 al 2"))
        columna = int(input("elegi una columna del 0 al 2"))

        if 0 <= fila < 3 and 0 <= columna < 3 and tablero[fila][columna] == " ":
            tablero[fila][columna] = turno
            mostrar(tablero)

            if ganador(tablero, turno):
                print(f"ganó {turno}")
                ganador = turno
                break
            elif tablerolleno(tablero):
                print("empate")
                break
            turno = "O" if turno == "X" else "X"
        else:
            print("casilla invalida, elegi de nuevo")

    reiniciar = input("queres jugar de nuevo? (si/no): ")
    if reiniciar.lower() != "si":
        print("gracias por jugar")
        break
