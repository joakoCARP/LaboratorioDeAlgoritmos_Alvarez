matriz = [
    [1, 2, 3, 4],
    [5, 6, 7, 8],
    [9, 10, 15, 20],
    [25, 30, 35, 40]
]

for i, fila in enumerate(matriz):
    sumafila = sum(fila)
    print(f"suma de filas {i}: {sumafila}")

for j in range(len(matriz[0])):
    sumacolumna = sum(fila[j] for fila in matriz)
    print(f"suma de columnas {j}: {sumacolumna}")
