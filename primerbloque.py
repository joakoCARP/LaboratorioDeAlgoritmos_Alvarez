import tiempo

def ejercicioA():
    for i in range(1, 101):
        if i % 3 == 0:
            print(i)

def ejercicioB():
    edad = int(input("ingrese su edad"))
    if edad < 18:
        print("sos menor de edad")
    elif edad == 18:
        print("justito tenes 18")
    else:
        print("sos mayor de edad")

def ejercicioC():
    palabra = input("ingrese una palabra")
    print(f"la palabra tiene {len(palabra)} letras")

def ejercicioD():
    contraseñaSecreta = "python123"
    intentos = 5
    while intentos > 0:
        intento = input("adivina la contraseña secreta")
        if intento == contraseñaSecreta:
            print("bien. La adivinaste")
            break
        else:
            intentos -= 1
            print(f"incorrecto. Te quedan {intentos} intentos")
    else:
        print("no adivinaste la contraseña. Mala suerte che")

def ejercicioE():
    mayor = None
    for i in range(10):
        numero = int(input(f"ingrese numeros {i+1}")) 
        if mayor is None or numero > mayor:
            mayor = numero
    print(f"el numero mas alto que ingresaste fue {mayor}")

def ejercicioF():
    nombre = input("ingrese su nombre")
    print(f"Hola, {nombre.title()}")

def ejercicioG():
    print("tabla del 7:")
    for i in range(1, 11):
        print(f"7 x {i} = {7 * i}")

def ejercicioH():
    for i in range(10, 0, -1):
        print(i)
    print("oa oa mami somo la luuuuu")

def ejercicioI():
    numero = int(input("ingrese un numero"))
    if numero % 2 == 0:
        print("es par")
    else:
        print("es impar")

def ejercicioJ():
    frase = input("ingresa una frase")
    vocales = "aeiouAEIOU"
    contador = 0
    for letra in frase:
        if letra in vocales:
            contador += 1
    print(f"la frase tiene {contador} vocales")

def ejercicioK():
    numero = int(input("ingresa un numero entre el 1 y el 12 para ver su tabla de multiplicacion"))
    for i in range(1, 13):
        print(f"{numero} x {i} = {numero * i}")

def ejercicioL():
    acumulado = 0
    while acumulado <= 100:
        try:
            numero = float(input("ingresa un numero"))
            acumulado += numero
            print(f"acumulado actual: {acumulado}")
        except ValueError:
            print("ingresa un numero valido")
    print("el total acumulado superó 100")

def ejercicioM():
    palabra = input("ingresa una palabra")
    for letra in palabra:
        print(letra)

def ejercicioN():
    edad = int(input("ingresa tu edad"))
    votar = edad >= 16
    manejar = edad >= 18
    if votar and manejar:
        print("podes votar y manejar")
    elif votar:
        print("podes votar, pero no manejar")
    elif manejar:
        print("podes manejar, pero no votar")
    else:
        print("no podes votar ni manejar")

def ejercicioO():
    for numero in range(50, -1, -5):
        print(numero)

def ejercicioP():
    while True:
        contraseña = input("ingresa una contraseña")
        contraseña2 = input("repeti la contraseña")
        if contraseña == contraseña2:
            print("acceso permitido")
            break
        else:
            print("las contraseñas no coinciden. Intenta de nuevo")

def ejercicioQ():
    while True:
        nombre = input("ingresa un nombre")
        if len(nombre) > 10:
            print("el nombre es muy largo, fin del programa")
            break
        else:
            print(f"nombre ingresado: {nombre}")

def ejercicioR():
    for segundo in range(60):
        print(f"segundos: {segundo}")
        tiempo.sleep(1)
    print("Un minuto ha pasado")

def ejercicioS():
    oracion = input("escribi una oración")
    cantidadA = oracion.count('a')
    print(f"la oracion tiene {cantidadA} letras 'a'")

def menu():
    print("\nmenu de ejercicios primer bloque")
    print("1: ejercicio A")
    print("2: ejercicio B")
    print("3: ejercicio C")
    print("4: ejercicio D")
    print("5: ejercicio E")
    print("6: ejercicio F")
    print("7: ejercicio G")
    print("8: ejercicio H")
    print("9: ejercicio I")
    print("10: ejercicio J")
    print("11: ejercicio K")
    print("12: ejercicio L")
    print("13: ejercicio M")
    print("14: ejercicio N")
    print("15: ejercicio O")
    print("16: ejercicio P")
    print("17: ejercicio Q")
    print("18: ejercicio R")
    print("19: ejercicio S")
    print("20: salir")

while True:
    mostrarMenu()
    opcion = input("selecciona una opcion")
    if opcion == "1":
        ejercicioA()
    elif opcion == "2":
        ejercicioB()
    elif opcion == "3":
        ejercicioC()
    elif opcion == "4":
        ejercicioD()
    elif opcion == "5":
        ejercicioE()
    elif opcion == "6":
        ejercicioF()
    elif opcion == "7":
        ejercicioG()
    elif opcion == "8":
        ejercicioH()
    elif opcion == "9":
        ejercicioI()
    elif opcion == "10":
        ejercicioJ()
    elif opcion == "11":
        ejercicioK()
    elif opcion == "12":
        ejercicioL()
    elif opcion == "13":
        ejercicioM()
    elif opcion == "14":
        ejercicioN()
    elif opcion == "15":
        ejercicioO()
    elif opcion == "16":
        ejercicioP()
    elif opcion == "17":
        ejercicioQ()
    elif opcion == "18":
        ejercicioR()
    elif opcion == "19":
        ejercicioS()
    elif opcion == "20":
        print("programa terminado.")
        break
    else:
        print("opcion invalida. Proba de nuevo.")
