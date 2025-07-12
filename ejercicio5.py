aneonacimiento = int(input("ingrese su año de nacimiento"))
mesnacimiento = int(input("ingrese su mes de nacimiento(1-12)"))
mesactual = int(input("ingrese el mes actual(1-12)"))

if mesactual > mesnacimiento:
    print("ya cumpliste este año")
elif mesactual == mesnacimiento:
    print("estas cumpliendo años este mes")
else:
    print("todavia no cumpliste años")
