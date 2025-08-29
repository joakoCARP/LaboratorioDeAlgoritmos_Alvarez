import random
def dar_carta():
    numerosposibles = (1, 2, 3, 4, 5, 6, 7, 8, 9 , 10 , 11, 12, 13)
    palosposibles = ("corazones", "diamantes", "treboles", "picas")
    carta = (random.choice(numerosposibles), random.choice(palosposibles))
    return carta

def generar_mano_y_valor():
    carta1 = dar_carta()
    carta2 = dar_carta()
    carta3 = dar_carta()
    numerossalidos = [carta1[0], carta2[0], carta3[0]]
    valordelamano = sum(numerossalidos)

    if palossalidos[0] == palossalidos[1] or palossalidos[0] == palossalidos[2] or palossalidos[1] == palossalidos[2]:
        valordelamano += 15
    if palossalidos[0] == palossalidos[1] == palossalidos[2]:
        valordelamano += 15

    print("carta 1:", carta1)
    print("carta 2:", carta2)
    print("carta 3:", carta3)
    return valordelamano

puntajetotal = 0
manosdadas = 0

def menu_juego ():
        juego = int(input("presiona 1 si queres una mano o presiona 2 para salir"))

    if juego == "1":
        valor = generar_mano_y_valor()
        puntajetotal += valor
        manosdadas += 1
    elif puntajetotal >= 100:
        print("ganaste, tu puntaje total es:", puntajetotal)
            break
    elif puntajetotal <= 100:
        print("perdiste, tu puntaje total es:", puntajetotal)
            break
    elif juego == "2":
        print("cerrando programa")
    else: print("numero incorrecto, elegi de nuevo")

menu_juego()
