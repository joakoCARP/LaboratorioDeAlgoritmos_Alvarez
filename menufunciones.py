import random
import string

def menuBanco():
    print("\nMenú de la cuenta bancaria:")
    print("1. Depositar dinero")
    print("2. Retirar dinero")
    print("3. Salir")

def banco():
    saldo = 1000
    while True:
        menuBanco()
        try:
            opcion = input("elegi una opcion (1 a 3")
            if opcion == "1":
                monto = float(input("ingresa un monto para depositar"))
                if monto <= 0:
                    print("no podes depositar 0 o menos")
                else:
                    saldo += monto
                    print(f"tu saldo actual es: ${saldo:.2f}")
            elif opcion == "2":
                monto = float(input("ingresa un monto para retirar"))
                if monto <= 0:
                    print("queres sacar 0 pesos o menos maquinola?")
                elif monto > saldo:
                    print("no podes sacar mas de lo que tenes pancho")
                else:
                    saldo -= monto
                    print(f"tu saldo actual es: ${saldo:.2f}")
            elif opcion == "3":
                print("gracias por usar el banco, chau")
                break
            else:
                print("elegi una opcion valida")
        except ValueError:
            print("hubo un error, intenta de nuevo")

def imc(peso, altura):
    return peso / (altura ** 2)

def clasificacion(imc):
    if imc < 18.5:
        return "bajo de peso"
    elif 18.5 <= imc < 24.9:
        return "peso normal"
    elif 25 <= imc < 29.9:
        return "sobrepeso"
    elif 30 <= imc < 34.9:
        return "obesidad ligera"
    else: return "obesidad"

def calculadora():
    try:
        peso = float(input("ingrese su peso (kg)"))
        altura = float(input("ingrese su altura (mts)"))
    
        if peso <= 0 or altura <= 0:
            print("no existis amigo")
            return
        indice = imc(peso, altura)
        categoria = clasificacion(imc)

        print(f"tu IMC es: {indice:.2f}")
        print(f" tu categoria es: {categoria}")
    except ValueError:
        print("datos invalidos, ingresa de nuevo")

def reemplazo(frase, vocalNueva):
    vocales = "aeiouAEIOU"
    fraseModificada = ""
    for letra in frase:
        if letra in vocales:
            if letra.isupper():
                fraseModificada += vocalNueva.upper()
            else:
                fraseModificada += vocalNueva
        else:
            fraseModificada += letra
            return fraseModificada

def repetir():
    print("ingresa frases, se van a repetir con vocales randoms, para terminar el programa, escribi agusfornite2008")

    while True:
        frase = input("ingresa una frase")
        if frase.lower() == "agusfornite2008":
            print("programa finalizado")
        
        for vocal in "aeiou":
            fraseModificada = reemplazo(frase, vocal)
            print(f"vocal: {vocal}, {fraseModificada}")

def invertirPalabras(frase):
    palabras = frase.split()
    palabrasInvertidas = palabras[::-1]
    fraseInvertida = "".join(palabrasInvertidas)
    return fraseInvertida

frase = input("ingresa una frase")
resultado = invertirPalabras(frase)
print(resultado)

listaNombres = []

def menuNombres():
    print("\n menu")
    print("1. agregar nombre")
    print("2. mostrar nombre por posicion")
    print("3. ver nombres")
    print("4. salir")

while True:
    menuNombres()
    opcion = input("elegi una opcion (1 al 4) ")
    if opcion == "1":
        nombre = input("ingresa un nombre")
        listaNombres.append(nombre)
        print(f"se agregó '{nombre}'")
    elif opcion == "2":
        if not listaNombres:
            print("no hay nombres en la lista, agrega una")
        continue
    try:
        posicion = int(input("ingresa la posicion del nombre"))
        if 1 <= posicion <= len(listaNombres):
            print(f"el nombre en la posicion {posicion} es: {listaNombres[1]}")
        else:
            print("posicion fuera de rango")
    except ValueError:
        print("ingresa un numero entero")
    if opcion == "3":
        if listaNombres:
            print("lista de nombres:")
            for i, nombre in enumerate(listaNombres, start=1):
                print(f"{i}. {nombre}")
        else:
            print("la lista esta vacia")

    elif opcion == "4":
        print("chau")
        break

    else:
        print("elegi entre 1 y 4")

def mostrarMenu():
    print("\nmenu de ejercicios:")
    print("1: cuenta bancaria")
    print("2: indice de masa corporal")
    print("3: programa que da vocales distintas por frase")
    print("4: palabra invertida")
    print("5: lista de nombres")
    print("0: salir")

while True:
    mostrarMenu()
    opcion = input("selecciona una opcion")
    if opcion == "1":
        dividir()
    elif opcion == "2":
        calculadora()
    elif opcion == "3":
        repetir()
    elif opcion == "4":
        invertirPalabras()
    elif opcion == "5":
        menuNombres()
    elif opcion == "0":
        print("Programa terminado.")
        break
    else:
        print("Opcion invalida. Proba de nuevo.")

mostrarMenu()
