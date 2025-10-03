def crearlista():
    lista = []
    while True:
        elem = input("agrega un elemento o escribi 'fin' para terminar")
        if elem.lower() == "fin":
            break
        lista.append(elem)
    print("lista creada:", lista)
    return lista

def busquedasecuencial(lista, valor):
    for i, elem in enumerate(lista):
        if elem == valor:
            return i
    return -1

def busquedabinaria(lista, valor):
    listaordenada = sorted(lista)
    izq, der = 0, len(listaordenada) - 1
    while izq <= der:
        medio = (izq + der) // 2
        if listaordenada[medio] == valor:
            return medio
        elif listaordenada[medio] < valor:
            izq = medio + 1
        else:
            der = medio - 1
    return -1

def ordeninsercion(lista):
    for i in range(1, len(lista)):
        clave = lista[i]
        j = i - 1
        while j >= 0 and lista[j] > clave:
            lista[j + 1] = lista[j]
            j -= 1
        lista[j + 1] = clave
    return lista

def ordenburbuja(lista):
    n = len(lista)
    for i in range(n):
        for j in range(0, n-i-1):
            if lista[j] > lista[j+1]:
                lista[j], lista[j+1] = lista[j+1], lista[j]
    return lista

def ordenseleccion(lista):
    n = len(lista)
    for i in range(n):
        min_idx = i
        for j in range(i+1, n):
            if lista[j] < lista[min_idx]:
                min_idx = j
        lista[i], lista[min_idx] = lista[min_idx], lista[i]
    return lista

lista = []

while True:
    print("menu")
    print("1: crear una lista y agregarle elementos")
    print("2: buscar en la lista")
    print("3: ordenar la lista")
    print("4: salir")
    opcion = input("elegi una opcion")

    if opcion == "1":
        lista = crearlista()
    elif opcion == "2":
        if not lista:
            print("la lista esta vacia")
            continue
        valor = input("que elemento queres buscar?")
        print("1: busqueda secuencial")
        print("2: busqueda binaria")
        tipo = input("elegi el tipo de busqueda")
        if tipo == "1":
            pos = busquedasecuencial(lista, valor)
            if pos != -1:
                print(f"elemento encontrado en la posicion {pos}")
            else:
                print("elemento no encontrado")
        elif tipo == "2":
            pos = busquedabinaria(lista, valor)
            if pos != -1:
                print(f"elemento encontrado en la posicion {pos} (en la lista ordenada)")
            else:
                print("elemento no encontrado")
        else:
            print("opcion invalida")
    elif opcion == "3":
        if not lista:
            print("la lista esta vacia")
            continue
        print("1: ordenar por insercion")
        print("2: ordenar por burbuja")
        print("3: ordenar por seleccion")
        tipo = input("elegi el tipo de ordenamiento")
        if tipo == "1":
            lista = ordeninsercion(lista)
            print("lista ordenada por insercion:", lista)
        elif tipo == "2":
            lista = ordenburbuja(lista)
            print("lista ordenada por burbuja:", lista)
        elif tipo == "3":
            lista = ordenseleccion(lista)
            print("lista ordenada por seleccion:", lista)
        else:
            print("opcion invalida")
    elif opcion == "4":
        print("programa terminado")
        break
    else:
        print("opcion invalida")
