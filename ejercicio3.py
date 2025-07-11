x = int(input("ingrese la cantidad de terminos de la secuencia de fibonacci"))
a, b = 0, 1
for i in range(x):
    print(a)
    a, b = b, a + b
