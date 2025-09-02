matriz = [
    [4, 3, 7],
    [6, 5, 4],
    [8, 1, 2]
]

diagonalprincipal = sum(matriz[i][i] for i in range(3))

diagonalsecundaria = sum(matriz[i][2 - i] for i in range(3))

print(f"suma de la diagonal principal: {diagonalprincipal}")
print(f"suma de la diagonal secundaria: {diagonalsecundaria}")
