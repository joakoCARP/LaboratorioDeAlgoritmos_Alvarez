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
dividir()

def edad():
    while True:
    try:
        edad = int(input("ingresa tu edad"))
        print("tenes {edad} años")
        break
    except ValueError:
        print("edad no identificadad, intente de nuevo")
edad()

nombres = ["Ana", "Pedro", "Sofía"]

def nombreIndice():
    while True:
        try:
            indice = int(input("ingresa un número indice (0 a 2)"))
            print(f(el nombre en el índice es: {nombres[indice]}")
            break
        except ValueError:
            print("numero invaido. Intenta con un numero entero")
        except IndexError:
            print("indice fuera del rango. Proba con 0, 1 o 2.")

nombreIndice()

def numerosEnteros():
    try:
        num1 = int(input("ingresa el primer numero"))
        num2 = int(input("ingresa el segundo numero"))
        resultado = num1 + num2
        print(f(la suma es: {resultado}")
    except (ValueError, TypeError):
        print("error. No se puede ingresar texto o numeros con texto.")


numerosEnteros()

            
