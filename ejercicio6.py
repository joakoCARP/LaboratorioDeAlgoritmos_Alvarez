import random

nombres = ["pepe", "juana", "santiago", "ignacio", "federico", "gabriel", "sofia"]
notas = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

alumno1 = [random.choice(nombres), random.choice(notas)]
alumno2 = [random.choice(nombres), random.choice(notas)]
alumno3 = [random.choice(nombres), random.choice(notas)]

notasCurso = [alumno1[1], alumno2[1], alumno3[1]]
Promedio = sum(notasCurso) % 3

print(alumno1)
print(alumno2)
print(alumno3)
Promedio
