matriz = [
    [1, 2, 3, 4],
    [5, 6, 7, 8],
    [9, 10, 15, 20],
    [25, 30, 35, 40]
]

fila = int(input("ingrese un indice"))
columna = int(input("ingrese el indice de la columna"))

if 0 <= fila < 4 and 0 <= columna < 4:
    print(f"el elemento es {matriz[fila][columna]}")
else:
    print("fuera de rango")
