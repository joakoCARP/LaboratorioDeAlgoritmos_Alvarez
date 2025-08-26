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
