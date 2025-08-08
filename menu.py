import random
import string

def dividir():
    try:
        num1 = float(input("ingresa el primer numero"))
        num2 = float(input("ingresa el segundo numero"))
        resultado = num1 / num2
        print(f"el resultado es {resultado}")
    except ZeroDivisionError:
        print("no se puede dividir por cero")
    except ValueError:
        print("ingresa numeros validos")

def edad():
    while True:
        try:
            edad = int(input("ingresa tu edad"))
            print(f"tenes {edad} años")
            break
        except ValueError:
            print("edad no identificada, intenta de nuevo")

nombres = ["Ana", "Pedro", "Sofía"]

def nombreIndice():
    while True:
        try:
            indice = int(input("ingresa un numero indice (0 a 2)"))
            print(f"el nombre en el índice es: {nombres[indice]}")
            break
        except ValueError:
            print("numero invaido. Intenta con un numero entero")
        except IndexError:
            print("indice fuera del rango. Proba con 0, 1 o 2.")

def numerosEnteros():
    try:
        num1 = int(input("ingresa el primer numero"))
        num2 = int(input("ingresa el segundo numero"))
        resultado = num1 + num2
        print(f"la suma es: {resultado}")
    except (ValueError, TypeError):
        print("error. No se puede ingresar texto o numeros con texto.")

def programaDivision():
    try:
        num1 = float(input("ingresa el primer numero"))
        num2 = float(input("ingresa el segundo numero"))
        resultado = num1 / num2
        print(f"el resultado de la division es: {resultado}")
    except ZeroDivisionError:
        print("no se puede dividir por cero")
    except ValueError:
        print("no pongas letras")
    finally:
        print("Fin del programa de cálculo.")

def mostrarMenu():
    print("\nmenu de ejercicios:")
    print("1: division entre numeros")
    print("2: verificacion edad")
    print("3: lista de nombres")
    print("4: programa de enteros")
    print("5: programa de division")
    print("0: salir")

while True:
    mostrarMenu()
    opcion = input("selecciona una opcion")
    if opcion == "1":
        dividir()
    elif opcion == "2":
        edad()
    elif opcion == "3":
        nombreIndice()
    elif opcion == "4":
        numerosEnteros()
    elif opcion == "5":
        programaDivision()
    elif opcion == "0":
        print("Programa terminado.")
        break
    else:
        print("Opcion invalida. Proba de nuevo.")

mostrarMenu()
