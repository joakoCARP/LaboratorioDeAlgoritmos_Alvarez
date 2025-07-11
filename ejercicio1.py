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
