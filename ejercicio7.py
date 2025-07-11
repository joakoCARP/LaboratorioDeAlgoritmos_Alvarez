numero = int(input("ingrese un numero entero"))
sumadedigitos = 0

for digito in str(abs(numero)):
    sumadedigitos += int(digito)

print(f"La suma de los digitos es {sumadedigitos}")
