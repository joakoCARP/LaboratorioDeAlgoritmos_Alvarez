def calcularFactorial(numero):
    factorial = 1
    for i in range(1, numero + 1):
        factorial *= i
    return factorial

intentosMaximos = 5

while True:
    intentos = intentosMaximos
    while intentos > 0:
        entrada = input("ingrese un numero entero no negativo para calcular su factorial")
        if entrada.isdigit():
            numero = int(entrada)
            if numero >= 0:
                resultado = calcularFactorial(numero)
                print(f"el factorial de {numero} es {resultado}")
                break
            else:
                intentos -= 1
                print(f"no es valido ({intentos} intentos restantes)")
        else:
            intentos -= 1
            print(f"no es valido ({intentos} intentos restantes).")
    else:
        print("no tiene mas intentos")
        break
