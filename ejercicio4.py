matriz = [
    [1, 2, 3, 4],
    [5, 6, 7, 8],
    [9, 10, 11, 12],
    [13, 14, 15, 41]
]

elementos = sum(len(fila) for fila in matriz)
suma = sum(sum(fila) for fila in matriz)
promedio = suma / elementos

matriznueva = [
    [promedio if num < promedio else num for num in fila]
    for fila in matriz
]

print(f"el promedio es {promedio:.2f}")
print("matriz nueva:")
for fila in matriznueva:
    print(fila)
