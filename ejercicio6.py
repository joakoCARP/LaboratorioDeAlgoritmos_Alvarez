while True:
    print("\nmenu de opciones:")
    print("1 - saludar")
    print("2 - despedirse")
    print("3 - terminar programa")
    opcion = input("seleccione una opcion ")

    if opcion == "1":
        print("hola")
    elif opcion == "2":
        print("chau")
    elif opcion == "3":
        print("programa terminado.")
        break
    else:
        print("opcion invalida. Intente de nuevo.")
