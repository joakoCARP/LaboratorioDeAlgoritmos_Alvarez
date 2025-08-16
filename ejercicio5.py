import random

nombres = ["pepe", "juana", "santiago", "ignacio", "federico", "gabriel", "sofia"]
notas = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
listaAlumno = []

nombrealeatorio = random.choice(nombres)
notaaleatoria = random.choice(notas)
listaAlumno.append((nombrealeatorio, notaaleatoria))

print(listaAlumno)
