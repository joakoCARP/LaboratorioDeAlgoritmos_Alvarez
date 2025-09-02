matriz = [
    [1, 2, 3, 4],
    [5, 6, 7, 8],
    [9, 10, 15, 20],
    [25, 30, 35, 40]
]

numerogrande = max(max(fila) for fila in matriz)

print(f"El número mas grande de la matriz es {numerogrande}")
