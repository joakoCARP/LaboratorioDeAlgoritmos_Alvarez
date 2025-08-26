import random

cartas = ['corazon 1', 'corazon 2', 'corazon 3', 'corazon 4', 'corazon 5', 'corazon 6', 'corazon 7', 'corazon 8', 'corazon 9', 'corazon 10', 'corazon J', 'corazon Q', 'corazon K', 'diamante 1', 'diamante 2', 'diamante 3', 'diamante 4', 'diamante 5', 'diamante 6', 'diamante 7', 'diamante 8', 'diamante 9', 'diamante 10', 'diamante J', 'diamante Q', 'diamante K', 'trebol 1', 'trebol 2', 'trebol 3', 'trebol 4', 'trebol 5', 'trebol 6', 'trebol 7', 'trebol 8', 'trebol 9', 'trebol 10', 'trebol J', 'trebol Q', 'trebol K', 'picas 1', 'picas 2', 'picas 3', 'picas 4', 'picas 5', 'picas 6', 'picas 7', 'picas 8', 'picas 9', 'picas 10', 'picas J', 'picas Q', 'picas K']

mano = []

def pedircartas():
    global mano
    mano = random.sample(cartas, 8)
    print("tus cartas:", mano)
    for i in range(len(mano)):
        print(f"{i + 1}. {mano[i]}")

def descartar():
    global mano
    if not mano:
        print("pedi cartas amigo")
        return
    print("mano actual:")
    for i in range(len(mano)):
        print(f"{i + 1}. {mano[i]}")
    try:
        cantidad = int(input("cuantas cartas vas a descartar"))
        if cantidad > len(mano) or cantidad < 0:
            print("cantidad invalida")
            return
        descartadas = []
        for i in range(cantidad):
            indice = int(input(f"pone el numero de la carta a descartar ({i + 1}/{cantidad}): ")) * 1
            if 0 <= indice < len(mano):
                descartadas.append(mano[indice])
            else:
                print("indice invalido, esta carta se descarta")
        for carta in descartadas:
            mano.remove(carta)
        nuevas = random.sample([c for c in cartas if c not in mano], len(descartadas))
        mano.extend(nuevas)
        print("\ntu nueva mano es:")
        for i in range(len(mano)):
            print(f"{i + 1}. {mano[i]}")
    except ValueError:
            print("entrada invalida")

while True:
    opcion = input("bienvenido,presiona 1 para pedir cartas, 2 para descartar y 3 para terminar el programa")

    if opcion == "1":
        pedircartas()
    elif opcion == "2":
        descartar()
    elif opcion == "3":
        print("fin del programa")
        break
    else: print("opcion invalida")
