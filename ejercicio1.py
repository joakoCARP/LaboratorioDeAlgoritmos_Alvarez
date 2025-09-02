matriz = [
    [1, 2, 3, 4],
    [5, 6, 7, 8],
    [9, 10, 11, 12],
    [13, 14, 15, 41]
]

esquinas = (
    matriz[0][0] + matriz[0][3] + matriz[3][0] + matriz[3][3]    
)

print(f"la suma de las esquinas es {esquinas}")
