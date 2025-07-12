import random
import string

def ejercicio1():
    numero = int(input("ingrese un numero entero"))
    primo = True
    if numero < 2:
        primo = False
    else:
        for i in range(2, int(numero ** 0.5) + 1):
            if numero % i == 0:
                primo = False
                break
    if primo:
        print("el numero es primo")
    else:
        print("el numero no es primo")

def ejercicio2():
    numero = int(input("ingrese un numero entero no negativo"))
    factorial = 1
    if numero < 0:
        print("no se puede calcular el factorial de un numero negativo")
    else:
        for i in range(1, numero + 1):
            factorial *= i
        print(f"el factorial de {numero} es {factorial}")

def ejercicio3():
    x = int(input("ingrese la cantidad de terminos de la secuencia de fibonacci"))
    a, b = 0, 1
    for i in range(x):
        print(a)
        a, b = b, a + b

def ejercicio4():
    frase = input("ingrese una frase")
    vocales = "aeiouAEIOU"
    contador = 0
    for letra in frase:
        if letra in vocales:
            contador += 1
    print(f"la frase tiene {contador} vocales")

def ejercicio5():
    texto = input("ingrese una palabra o frase")
    invertido = texto[::-1]
    print(f"la cadena invertida es {invertido}")

def ejercicio6():
    while True:
        print("\nmenu de opciones")
        print("1: saludar")
        print("2: despedirse")
        print("3: terminar programa")
        opcion = input("seleccione una opcion")
        if opcion == "1":
            print("hola")
        elif opcion == "2":
            print("chau")
        elif opcion == "3":
            print("programa terminado.")
            break
        else:
            print("opcion invalida. Intente de nuevo.")

def ejercicio7():
    numero = int(input("ingrese un numero entero"))
    sumadedigitos = 0
    for digito in str(abs(numero)):
        sumadedigitos += int(digito)
    print(f"la suma de los digitos es {sumadedigitos}")

def ejercicio8():
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

def ejercicio9():
    def entrada():
        while True:
            mensaje = input("ingrese el mensaje (solo letras y espacios)").lower()
            if all(c in string.ascii_lowercase + " " for c in mensaje):
                return mensaje
            else:
                print("el mensaje contiene caracteres no permitidos. Pone otro devuelta.")
    def cifrar(mensaje):
        clave = input("ingrese la clave (numero entero)")
        if not clave.lstrip('-').isdigit():
            print("clave invalida. Tiene que ser un numero entero.")
            return
        clave = int(clave)
        resultado = ""
        for c in mensaje:
            if c == " ":
                resultado += " "
            else:
                posi = ord(c) - ord('a')
                nuevaposi = (posi + clave) % 26
                resultado += chr(nuevaposi + ord('a'))
        print(f"mensaje cifrado: {resultado}")
    def descifrado(mensaje):
        clave = input("ingrese la clave (numero entero): ")
        if not clave.lstrip('-').isdigit():
            print("Clave invalida. Tiene que ser un numero entero.")
            return
        clave = int(clave)
        resultado = ""
        for c in mensaje:
            if c == " ":
                resultado += " "
            else:
                posi = ord(c) - ord('a')
                nuevaposi = (posi - clave) % 26
                resultado += chr(nuevaposi + ord('a'))
        print(f"mensaje descifrado: {resultado}")
    def menu():
        while True:
            print("\nmenu")
            print("1: cifrar mensaje")
            print("2: descifrar mensaje")
            print("3: salir")
            opcion = input("seleccione una opcion")
            if opcion == "1":
                mensaje = entrada()
                cifrar(mensaje)
            elif opcion == "2":
                mensaje = entrada()
                descifrado(mensaje)
            elif opcion == "3":
                print("programa terminado")
                break
            else:
                print("opcion invalida. Intente de nuevo.")
    menu()

def ejercicio10():
    print("bienvenidos al juego Mafia. hay 3 Roles: mafia, Policia, y civil")
    print("por favor ingresa el nombre de 4 jugadores")
    jugador1 = input("nombre del jugador 1: ")
    jugador2 = input("nombre del jugador 2: ")
    jugador3 = input("nombre del jugador 3: ")
    jugador4 = input("nombre del jugador 4: ")
    nombres = [jugador1, jugador2, jugador3, jugador4]
    mafia = random.choice(nombres)
    resto = [nombre for nombre in nombres if nombre != mafia]
    policia = random.choice(resto)
    civil = [nombre for nombre in resto if nombre != policia]
    roles = {
        mafia: "mafia",
        policia: "policia",
        civil[0]: "civil",
        civil[1]: "civil"
    }
    print("\nya se juegan los primeros 45 minutos en el monumental. cada jugador va a descubrir su rol en secreto\n")
    for nombre in nombres:
        print(f"turno de {nombre}. Presiona enter para ver tu rol")
        input()
        print(f"tu rol es {roles[nombre]}")
        input("presiona enter para continuar\n")

def mostrarMenu():
    print("\nmenu de ejercicios:")
    print("1: verificacion numero primo")
    print("2: calculo de factorial de un número")
    print("3: secuencia Fibonacci")
    print("4: contador de vocales")
    print("5: invertir una palabra")
    print("6: menu interactivo")
    print("7: suma digitos de un numero")
    print("8: calculadora de factoriales")
    print("9: cifrado y descifrado de un mensaje")
    print("10: juego mafia")
    print("0: salir")

while True:
    mostrarMenu()
    opcion = input("selecciona una opcion")
    if opcion == "1":
        ejercicio1()
    elif opcion == "2":
        ejercicio2()
    elif opcion == "3":
        ejercicio3()
    elif opcion == "4":
        ejercicio4()
    elif opcion == "5":
        ejercicio5()
    elif opcion == "6":
        ejercicio6()
    elif opcion == "7":
        ejercicio7()
    elif opcion == "8":
        ejercicio8()
    elif opcion == "9":
        ejercicio9()
    elif opcion == "10":
        ejercicio10()
    elif opcion == "0":
        print("Programa terminado.")
        break
    else:
        print("Opcion invalida. Proba de nuevo.")
