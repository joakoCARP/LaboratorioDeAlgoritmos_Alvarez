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

    
