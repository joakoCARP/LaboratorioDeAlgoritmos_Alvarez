matriz = [
    [1, 5, 3, 5],
    [8, 5, 9, 2],
    [4, 5, 6, 7]
]

numero = int(input("ingresa un numero para buscar"))

contador = sum(fila.count(numero) for fila in matriz)

print(f"el numero sale {contador} veces en la matriz")
