import programa

def entrada():
    while True:
        mensaje = input("ingrese el mensaje (solo letras y espacios)").lower()
        if all(c in string.ascii_lowercase + " " for c in mensaje):
            return mensaje
        else:
            print("el mensaje contiene caracteres no permitidos. Pone otro devuelta.")

def cifrar(mensaje):
    clave = input("ingrese la clave (numero entero)")
    if not clave.lstrip('-').isdigit():
        print("clave invalida. Tiene que ser un numero entero.")
        return
    clave = int(clave)
    resultado = ""
    for c in mensaje:
        if c == " ":
            resultado += " "
        else:
            posi = ord(c) - ord('a')
            nuevaposi = (posi + clave) % 26
            resultado += chr(nuevaposi + ord('a'))
    print(f"mensaje cifrado: {resultado}")

def descifrado(mensaje):
    clave = input("ingrese la clave (numero entero)")
    if not clave.lstrip('-').isdigit():
        print("Clave invalida. Tiene que ser un numero entero.")
        return
    clave = int(clave)
    resultado = ""
    for c in mensaje:
        if c == " ":
            resultado += " "
        else:
            posi = ord(c) - ord('a')
            nuevaposi = (posi - clave) % 26
            resultado += chr(nuevaposi + ord('a'))
    print(f"mensaje descifrado: {resultado}")

def menu():
    while True:
        print("\nmenu")
        print("1: cifrar mensaje")
        print("2: descifrar mensaje")
        print("3: salir")
        opcion = input("seleccione una opcion")
        if opcion == "1":
            mensaje = entrada()
            cifrar(mensaje)
        elif opcion == "2":
            mensaje = entrada()
            descifrado(mensaje)
        elif opcion == "3":
            print("programa terminado")
            break
        else:
            print("opcion invalida. Intente de nuevo.")
if __name__ == "__main__":
    menu()
