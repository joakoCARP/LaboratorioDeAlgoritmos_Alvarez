import random

nombres = ["pepe", "juana", "santiago", "ignacio", "federico", "gabriel", "sofia"]
notas = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
PromediosEscuela = 0
cursos = 0

while cursos < 3:
    opcion = input("presione 1 para generar un curso o 2 para salir")

    if opcion == "1":
        alumno1 = [random.choice(nombres), random.choice(notas)]
        alumno2 = [random.choice(nombres), random.choice(notas)]
        alumno3 = [random.choice(nombres), random.choice(notas)]

        notasCurso = [alumno1[1], alumno2[1], alumno3[1]]
        Promedio = sum(notasCurso) / 3

        print("alumno 1:", alumno1)
        print("alumno 2:", alumno2)
        print("alumno 3:", alumno3)
        print("promedio del curso:", Promedio)

        PromediosEscuela += Promedio
        cursos += 1
    elif opcion == "2":
        print("Cerrando Programa")
        break
    else:
        print("numero incorrecto")

if cursos == 3:
    promediofinal = PromediosEscuela / 3
    print(f"\nPromedio final de la escuela: {promediofinal:.2f}")
    if promediofinal >= 6:
        print("La escuela tiene buenos promedios")
    else:
        print("La escuela tiene malos promedios")
