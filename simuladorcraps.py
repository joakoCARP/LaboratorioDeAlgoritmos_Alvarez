import random
#importa el modulo random que sirve para randomizar los dados
def dados():
    dado1 = random.randint(1, 6)
    dado2 = random.randint(1, 6)
    suma = dado1 + dado2
    print(f"{dado1} + {dado2} = {suma}, conseguiste un {suma}")
    return suma
#dados() sirve para colocarle un valor aleatorio a los dados, para despues sumarlos, mostrar los valores en el print y devuelve la suma para agregarla al juego
def craps(): #lo que pasa en esta funcion es lo necesario para que el juego siga funcionando 
    print("bienvenido a craps")
    tiroUno = dados #tiroUno es el primer tiro que tenes al empezar el juego, si sacas un numero del 7 al 11, ganas , si sacas 2,3 o 12, perdes
    if tiroUno in [7, 11]:
        print("ganaste instantaneamente")
    elif tiroUno in [2, 3, 12]:
        print("perdiste instantaneamente")
    else:
        punto = tiroUno
        print(f"tenes {punto} puntos, para ganar tenes que sacar tus puntos") 
        while True:
            tiroDos = dados()
            if tiroDos == punto:
                print("volviste a sacar tus puntos, ganaste")
                break
            elif tiroDos == 7:
                print("sacaste un 7, perdiste")
                break
craps()
#sirve para poder ejecutar el juego en la consola
  
