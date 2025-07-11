numero_secreto = 7
numero_elegido = None
while numero_elegido != numero_secreto:
    numero_elegido = int(input("adivina el numero secreto"))
    print("felicidades! adivinaste el numero")
else:
    print("sos malisimo amigo")
