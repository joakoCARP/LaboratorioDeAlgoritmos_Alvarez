matriz = [
    [1, 2, 3, 4],
    [5, 6, 7, 8],
    [9, 10, 15, 20],
    [25, 30, 35, 40]
]

transposicion = [[matriz[j][i] for j in range(len(matriz))] for i in range(len(matriz[0]))]

print("matriz transpuesta:")
for fila in transposicion:
    print(fila)
