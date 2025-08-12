import random
import string

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
        programaDivision()
    elif opcion == "0":
        print("Programa terminado.")
        break
    else:
        print("Opcion invalida. Proba de nuevo.")

mostrarMenu()
