nombres = 'emiliano martinez', 'ernesto', 'esteban quito', 'josefinaaa', 'miguel borja', 'monsterrat', 'belgrano', 'paapparapapa', 'pepe', 'yanosequeponer'

nombremaslargo = ''

for nombre in nombres:
    if len(nombre) > len(nombremaslargo):
        nombremaslargo = nombre
        print(nombremaslargo)
