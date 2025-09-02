matriz = int(input("ingresa el tamaño de la matriz"))

matrizidentidad = [[1 if i == j else 0 for j in range(matriz)] for i in range(matriz)]
print("matriz de identidad:")
for fila in matrizidentidad:
    print(fila)
