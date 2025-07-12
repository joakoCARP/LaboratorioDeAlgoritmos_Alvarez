#no se si se referia a hacer un menu asi profe
def holaMundo():
    for i in range(5):
        print("¡Hola, mundo!")

def tablaDel7():
    for i in range(1, 11):
        print(f"7 x {i} = {7 * i}")

def cuentaRegresiva():
    contador = 5
    while contador >= 1:
        print(contador)
        print("listo para despegar")
        contador -= 1
    print("despegue!")

def calcularFactorial():
    numero = int(input("ingrese un numero entero no negativo"))
    factorial = 1
    if numero < 0:
        print("no se puede calcular el factorial de un numero negativo")
    else:
        for i in range(1, numero + 1):
            factorial *= i
        print(f"el factorial de {numero} es {factorial}")

def contarVocales():
    frase = input("ingrese una frase: ")
    vocales = "aeiouAEIOU"
    contador = 0
    for letra in frase:
        if letra in vocales:
            contador += 1
    print(f"la frase tiene {contador} vocales")

while True:
    print("\nmenu de opciones:")
    print("1: imprimir ¡Hola, mundo! 5 veces")
    print("2: mostrar la tabla del 7")
    print("3: cuenta regresiva del 5 al 1")
    print("4: calcular el factorial de un numero")
    print("5: Contar las vocales en una frase")
    print("6: salir")
    opcion = input("seleccione una opcion")

    if opcion == "1":
        holaMundo()
    elif opcion == "2":
        tablaDel7()
    elif opcion == "3":
        cuentaRegresiva()
    elif opcion == "4":
        calcularFactorial()
    elif opcion == "5":
        contarVocales()
    elif opcion == "6":
        print("programa terminado")
        break
    else:
        print("opcion invalida. Intente de nuevo.")
