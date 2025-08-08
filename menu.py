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
        print("tenes {edad} años")
        break
    except ValueError:
        print("edad no identificadad, intente de nuevo")
edad()
