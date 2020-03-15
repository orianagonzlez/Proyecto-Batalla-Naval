import random
from time import sleep
from colorama import init, Fore, Style
from FuncionesComunes import pedir_entero_positivo_validado, separador

init(autoreset=True)

class Barco:
    '''
    Clase padre de los barcos que pertenecen a la flota del juego. Su unico atributo es el tamaño del barco.
    '''

    def __init__(self, tamano):
        self.tamano = tamano

    def __str__(self):
        '''
        Función que permite que al imprimir una instancia de la clase se imprime lo indicado en vez de la posición que ocupa en la memoria.
        '''
        return "B"

    def posicion(self, tablero):
        '''
        Función que recibe como argumento el tablero de juego y genera las coordenadas que ocupara el barco en él dependiendo de su tamaño.

        Para esto, verifica que las coordenadas:
        - Esten dentro del tablero
        - No esten ocupadas
        - No tengan barcos en sus posiciones contiguas (arriba, abajo, izquierda y derecha)

        Si todo esto se cumple, retorna la lista de coordenadas.
        '''
            
            
        contigua = True
        dentro_tablero = False
        ocupada = True

        while contigua or not dentro_tablero or ocupada:
            contigua = False
            dentro_tablero = True
            ocupada = False

            #Generamos la coordenada inicial del barco
            x = random.randint(0, 9)
            y = random.randint(0, 9)

            coordenadas = []
            #Inicializamos orientacion en 2, si el tamaño del objeto es mayor a 1 este valor cambiara a 0 si la orientacion es 
            #horizontal y a 1 si es vertical
            orientacion = 2

            if self.tamano > 1:
                orientacion = random.randint(0, 1)
                
            #Añadimos a la lista todas las coordenadas que ocupara el barco dependiendo de su tamaño
            for i in range(self.tamano):
                if orientacion == 0:
                    coordenadas.append((x + i, y))
                elif orientacion == 1:
                    coordenadas.append((x, y + i))
                else:
                    coordenadas.append((x, y))

            #En caso de que alguna coordenada en la lista de coordenadas que ocupara el barco no este dentro del tablero, este ocupada 
            #o tenga un barco en las posiciones contiguas, se repite el bucle, volviendo a escogerse aleatoriamente la coordenada inicial 
            for coordenada in coordenadas:
                if coordenada[0] > 9 or coordenada[1] > 9:
                    dentro_tablero = False
                    break
                elif tablero[coordenada[1]][coordenada[0]] != "O":
                    ocupada = True
                    break
                else:
                    if coordenada[0] != 9:
                        if tablero[coordenada[1]][coordenada[0] + 1] != "O":
                            contigua = True
                            break
                    if coordenada[0] != 0:
                        if tablero[coordenada[1]][coordenada[0] - 1] != "O":
                            contigua = True
                            break
                    if coordenada[1] != 9:
                        if tablero[coordenada[1] + 1][coordenada[0]] != "O":
                            contigua = True
                            break
                    if coordenada[1] != 0:
                        if tablero[coordenada[1] - 1][coordenada[0]] != "O":
                            contigua = True
                            break

        return coordenadas

class Portavion(Barco):
    '''
    Clase hija de Barco, corresponde al buque de 3 posiciones, también conocida como portavión.
    '''
    def __init__(self, tamano=3):
        Barco.__init__(self, tamano)

    def capacidad(self):
        '''
        Función que retorna la capacidad del buque de 3 posiciones.
        '''
        return "Este buque tiene la capacidad de aterrizar helicópteros en el para el transporte de tropas."

class Buque(Barco):
    '''
    Clase hija de Barco, corresponde al buque de 2 posiciones.
    '''
    def __init__(self, tamano=2):
        Barco.__init__(self, tamano)

    def capacidad(self):
        '''
        Función que retorna la capacidad del buque de 2 posiciones.
        '''
        return "Este buque tiene la capacidad de comunicarse con tierra y los otros miembros de la flota."

class Submarino(Barco):
    '''
    Clase hija de Barco, corresponde al submarino de 1 posición.
    '''
    def __init__(self, tamano=1):
        Barco.__init__(self, tamano)

    def capacidad(self):
        '''
        Función que retorna la capacidad del submarino de 1 posición.
        '''
        return "Este submarino tiene la capacidad de poder sumergirse y emerger del agua."

def posicionar_barcos(barco, lista_de_coord, tablero):
    '''
    Función que toma como argumentos el objeto, la lista de coordenadas que ocupa el barco y el tablero de juego. 
    
    Se encarga de ubicar en cada coordenada que ocupa el barco el objeto del que se trata (ya sea una instancia de Portavión, Buque o Submarino).
    '''
    for coord in lista_de_coord:
        tablero[coord[1]][coord[0]] = barco

def instrucciones(portavion, buque, submarino):
    '''
    Funcion que imprime las instrucciones del juego. Recibe como argumento un objeto de cada clase hija de Barco.
    '''
    print(Fore.MAGENTA + "|| INSTRUCCIONES DEL JUEGO ||")
    print('''    

El objetivo es descubrir en la menor cantidad de disparos la flota de barcos.

Dicha flota esta conformada por:
''')
    print(Fore.CYAN + "\t•", "1 buque que ocupa 3 posiciones del tablero. {}".format(portavion.capacidad()),
          Fore.CYAN + "\n\t•", "1 buque que ocupa 2 posiciones del tablero. {}".format(buque.capacidad()),
          Fore.CYAN + "\n\t•", "4 submarinos que ocupan 1 posición del tablero cada uno. {}".format(submarino.capacidad()))

    print('''
Si el barco ocupa más de 1 posición, su orientación puede ser vertical u horizontal. 
Ningún barco tiene otros barcos en sus posiciones contiguas (arriba, abajo, izquierda o derecha).
Por cada disparo acertado se ganan 10 puntos y por cada disparo fallado se pierden 2 puntos.

Suerte!
    ''')
    separador()

def imprimir_tablero(tablero):
    '''
    Función para imprimir el tablero de juego de forma decente.
    '''
    print("", end="\t")
    for j in range(1,11):
        print(Fore.BLUE + str(j), end="    ")

    for i, fila in enumerate(tablero, 1):
        print("\n")
        print(Fore.BLUE + str(i), end="\t")
        for columna in fila:
            if columna == "F":
                print(Fore.GREEN + columna, end="    ")
            elif columna == "X":
                print(Fore.RED + columna, end="    ")
            else:
                print(columna, end="    ")
    print("\n")

def actualizar_puntaje(username, puntaje, disparos):
    '''
    Función para actualizar el puntaje total, numero de disparos y cantidad de partidas del usuario en la base de datos de usuarios.

    Toma como argumentos el nombre de usuario, el puntaje obtenido en la partida y los disparos realizados para ganar.
    '''
    with open("BaseDeDatosUsuarios.txt", "r") as archivo_usuarios:
        datos_usuarios = archivo_usuarios.readlines()

    for i, usuario in enumerate(datos_usuarios):
        usuario_as_lista = usuario[:-1].split(",")
        if usuario_as_lista[0] == username:

            usuario_as_lista[4] = str(int(usuario_as_lista[4]) + puntaje)
            usuario_as_lista[5] = str(int(usuario_as_lista[5]) + disparos)
            usuario_as_lista[6] = str(int(usuario_as_lista[6]) + 1)

            usuario_as_str = ",".join(usuario_as_lista) + "\n"

            datos_usuarios[i] = usuario_as_str

            with open("BaseDeDatosUsuarios.txt", "w") as archivo_usuarios:
                archivo_usuarios.writelines(datos_usuarios)

def jugar(username):
    '''
    Función que controla todo el juego. Ubica los barcos, controla los disparos e imprime las estadísticas al final de la partida. 
    '''
    
    #Creando bucle que asegurara que el usuario pueda jugar tantas veces como quiera
    continuar = 1    
    while continuar:

        tablero = [
        ['O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O'], 
        ['O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O'], 
        ['O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O'], 
        ['O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O'], 
        ['O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O'], 
        ['O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O'], 
        ['O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O'], 
        ['O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O'], 
        ['O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O'], 
        ['O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O']
        ]
        
        puntaje = 0
        disparos_realizados = 0
        disparos_repetidos = 0
        disparos_necesarios = 9

        #Creando objetos y ubicandolos en el tablero
        portavion = Portavion()
        posicionar_barcos(portavion, portavion.posicion(tablero), tablero)

        buque = Buque()
        posicionar_barcos(buque, buque.posicion(tablero), tablero)

        submarino1 = Submarino()
        posicionar_barcos(submarino1, submarino1.posicion(tablero), tablero)

        submarino2 = Submarino()
        posicionar_barcos(submarino2, submarino2.posicion(tablero), tablero)

        submarino3 = Submarino()
        posicionar_barcos(submarino3, submarino3.posicion(tablero), tablero)

        submarino4 = Submarino()
        posicionar_barcos(submarino4, submarino4.posicion(tablero), tablero)

        instrucciones(portavion, buque, submarino1)
        sleep(3)

        while disparos_necesarios != 0:

            print("Puntaje:", puntaje, end="\n \n")

            imprimir_tablero(tablero)

            #Pidiendo coordenada donde se desea disparar
            x = pedir_entero_positivo_validado("\nIngrese la coordenada horizontal (x) donde desea disparar. Debe ser un número entre 1 y 10: ")
            while x > 10 or x < 1:
                x = pedir_entero_positivo_validado("\nIngrese la coordenada horizontal (x) donde desea disparar. Debe ser un número entre 1 y 10: ")
        
            y = pedir_entero_positivo_validado("\nIngrese la coordenada vertical (y) donde desea disparar. Debe ser un número entre 1 y 10: ")
            while y > 10 or y < 1:
                y = pedir_entero_positivo_validado("\nIngrese la coordenada vertical (y) donde desea disparar. Debe ser un número entre 1 y 10: ")

            #Verifica si el disparo acertó, falló o si es repetido
            if tablero[y - 1][x - 1] == "O":
                print(Fore.RED + "\nFallaste. Sigue intentando, tu puedes!\n")
                tablero[y - 1][x - 1] = "X"
                disparos_realizados += 1
                if puntaje >= 2:
                    puntaje -= 2
                else:
                    puntaje = 0
            elif tablero[y - 1][x - 1] == "X" or tablero[y - 1][x - 1] == "F":
                disparos_repetidos += 1
                print(Fore.MAGENTA + "\nDisparo ya realizado! Por favor ingresa otra coordenada.\n")
            else:
                tablero[y - 1][x - 1] = "F"
                print(Fore.GREEN + "\nAcertaste. Sigue así!\n")
                disparos_realizados += 1
                puntaje += 10
                disparos_necesarios -= 1

        separador()
        print(Fore.MAGENTA + "|| FIN DEL JUEGO ||\n\n")
        if disparos_realizados == 9:
            print("¿Eres un Robot? lo que acabas de hacer es poco probable...")
        elif disparos_realizados < 45:
            print("Excelente Estrategia!")
        elif disparos_realizados <= 70:
            print("Buena Estrategia, pero hay que mejorar!")
        else:
            print("Considérese Perdedor, tiene que mejorar notablemente!")
        
        sleep(2)
        #Imprimiendo estadísticas de la partida
        print(Fore.CYAN + "\n\t•", "Username:", username)
        print(Fore.CYAN + "\t•", "Cantidad de disparos realizados:", disparos_realizados)
        print(Fore.CYAN + "\t•", "Puntaje total:", puntaje)
        print(Fore.CYAN + "\t•", "Cantidad de disparos repetidos:", disparos_repetidos, "\n\n")
        imprimir_tablero(tablero)

        print('\n')

        actualizar_puntaje(username, puntaje, disparos_realizados)

        sleep(2)
        #Preguntando si se quiere jugar otra partida
        continuar = input("Ingrese 1 si desea volver a jugar y 0 en caso contrario: ")
        while continuar != "1" and continuar != "0":
            continuar = input("Ingrese 1 si desea volver a jugar y 0 en caso contrario: ")
        continuar = int(continuar)
        separador()