numero = int(input("ingrese un numero entero no negativo"))
factorial = 1

if numero < 0:
    print("no se puede calcular el factorial de un numero negativo")
else:
    for i in range(1, numero + 1):
        factorial *= i
    print(f"el factorial de {numero} es {factorial}")
