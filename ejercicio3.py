filas = 4

columnas = 4

matriz = []

for i in range(filas):
    filaactual = []
for j in range(columnas):
    valor = int(input(f"Ingresa el elemento[{i}][{j}]: "))
    filaactual.append(valor)

matriz.append(filaactual)

print("\nLa matriz cargada es:")

for fila in matriz:
    print(fila)
