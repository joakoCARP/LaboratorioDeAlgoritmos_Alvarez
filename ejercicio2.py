nombres = ['emiliano martinez', 'ernesto', 'esteban quito', 'josefinaaa', 'miguel borja', 'monsterrat', 'belgrano', 'paapparapapa', 'pepe', 'yanosequeponer']

contador = 0
vocales = 'aeiouAEIOU'

for nombre in nombres:
    for letra in nombre:
        if letra in vocales:
            contador += 1
            print("vocales:", contador)
