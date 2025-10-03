import random  

nombres = [
    "juan", "pedro", "luis", "carlos", "sergio", "miguel", "javier", "andres",
    "martin", "fernando", "diego", "lucas", "Mmatias", "gonzalo", "facundo",
    "nicolas", "ramiro", "agustin", "tomas", "leonel", "ivan", "pablo", "emiliano"
]

posiciones = ["delantero", "volante", "central", "arquero"]

def generacion():
    equipo = []
    for _ in range(23):
        nombre = random.choice(nombres)
        rendimiento = random.randint(50, 100)
        posicion = random.choice(posiciones)
        equipo.append([nombre, posicion, rendimiento])
    return equipo

def valoraciontotal(equipo):
    return sum(jugador[2] for jugador in equipo)

def mostrarequipo(equipo, nombreequipo):
    print(f"\n{nombreequipo}:")
    for jugador in equipo:
        print(f"nombre: {jugador[0]}, posicion: {jugador[1]}, puntos de rendimiento: {jugador[2]}")

equipo1 = generacion()
equipo2 = generacion()

valoracion1 = valoraciontotal(equipo1)
valoracion2 = valoraciontotal(equipo2)

mostrarequipo(equipo1, "equipo 1")
print(f"valoracion del equipo 1: {valoracion1}")
mostrarequipo(equipo2, "equipo 2")
print(f"valoración del equipo 2: {valoracion2}")

if valoracion1 > valoracion2:
    print("el equipo 1 tiene mas chances de ganar")
elif valoracion2 > valoracion1:
    print("el Equipo 2 tiene mas chances de ganar")
else:
    print("ambos tienen la misma chance de ganar")
