while True:
    letra = input("ingrese una letra o un punto para terminar")
    if letra == ".":
        print("programa terminado")
        break
    elif letra.lower() in "aeiou":
        print("es una vocal")
    else:
        print("no es una vocal")
