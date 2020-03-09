import random
from FuncionesComunes import pedir_entero_positivo_validado

class Barco:

        def __init__(self, tamano):
            self.tamano = tamano

        def __str__(self):
            return "O"

        def posicion(self, tablero):
            '''Las posiciones no pueden ser contiguas
            Posicion lineal
            Posiciones dentro del tablero
            Buque y portavion pueden ser vertical u horizontal
            Verificar que la posicion no este ocupada'''
                
                
            contigua = True
            dentro_tablero = False
            ocupada = True

            print("iniciando bucle")

            while contigua or not dentro_tablero or ocupada:
                contigua = False
                dentro_tablero = True
                ocupada = False

                x = random.randint(0, 9)
                y = random.randint(0, 9)

                coordenadas = []
                #Inicializamos orientacion en 2, si el tamano del objeto es mayor a 1 este valor cambiara a 0 si la orientacion es 
                #horizontal y a 1 si es vertical
                orientacion = 2

                if self.tamano > 1:
                    orientacion = random.randint(0, 1)
                
                for i in range(self.tamano):
                    if orientacion == 0:
                        print("horixontal")
                        coordenadas.append((x + i, y))
                    elif orientacion == 1:
                        print("vertical")
                        coordenadas.append((x, y + i))
                    else:
                        coordenadas.append((x, y))

                print("")
                print(coordenadas, end="\n \n")

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

            print("sali")
            return coordenadas

class Portavion(Barco):
    def __init__(self, tamano):
        Barco.__init__(self, tamano)

    def capacidad(self):
        print("Este buque tiene la capacidad de aterrizar helicopteros en el para el transporte de tropas.")

class Buque(Barco):
    def __init__(self, tamano):
        Barco.__init__(self, tamano)

    def capacidad(self):
        print("Este buque tiene la capacidad de comunicarse con tierra y los otros miembros de la flota.")

class Submarino(Barco):
    def __init__(self, tamano):
        Barco.__init__(self, tamano)

    def capacidad(self):
        print("Este submarino tiene la capacidad de poder sumergirse y emerger del agua.")

def posicionar_barcos(barco, lista_de_coord, tablero, posiciones):
    for coord in lista_de_coord:
        tablero[coord[1]][coord[0]] = barco
        posiciones.append(coord)



def imprimir_tablero(tablero):
    '''
    Funcion para imprimir el tablero de juego de forma decente.
    '''
    print("", end="\t")
    for j in range(1,11):
        print(j, end="    ")

    for i, fila in enumerate(tablero, 1):
        print("\n")
        print(i, end="\t")
        for columna in fila:
            print(columna, end="    ")

def actualizar_puntaje(username, puntaje, disparos):
    '''
    Funcion para actualizar el puntaje del usuario en el archivo de texto.
    '''
    archivo_usuarios = open("BaseDeDatosUsuarios.txt", "r")

    datos_usuarios = archivo_usuarios.readlines()
    print(datos_usuarios)

    for i, usuario in enumerate(datos_usuarios):
        usuario_as_lista = usuario[:-1].split(",")
        if usuario_as_lista[0] == username:
            print("encontre usuairo")

            usuario_as_lista[4] = str(int(usuario_as_lista[4]) + puntaje)
            usuario_as_lista[5] = str(int(usuario_as_lista[5]) + disparos)
            usuario_as_lista[6] = str(int(usuario_as_lista[6]) + 1)

            usuario_as_str = ",".join(usuario_as_lista) + "\n"

            datos_usuarios[i] = usuario_as_str

            print("modificado", datos_usuarios)

            archivo_usuarios = open("BaseDeDatosUsuarios.txt", "w")

            archivo_usuarios.writelines(datos_usuarios)

def jugar(username):
    
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
        
        posiciones_barcos = []
        puntaje = 0
        disparos_realizados = 0
        disparos_repetidos = 0
        disparos_necesarios = 9

        portavion = Portavion(3)
        posicionar_barcos(portavion, portavion.posicion(tablero), tablero, posiciones_barcos)

        buque = Buque(2)
        posicionar_barcos(buque, buque.posicion(tablero), tablero, posiciones_barcos)

        submarino1 = Submarino(1)
        posicionar_barcos(submarino1, submarino1.posicion(tablero), tablero, posiciones_barcos)

        submarino2 = Submarino(1)
        posicionar_barcos(submarino2, submarino2.posicion(tablero), tablero, posiciones_barcos)

        submarino3 = Submarino(1)
        posicionar_barcos(submarino3, submarino3.posicion(tablero), tablero, posiciones_barcos)

        submarino4 = Submarino(1)
        posicionar_barcos(submarino4, submarino4.posicion(tablero), tablero, posiciones_barcos)

        while disparos_necesarios != 0:

            print("Puntaje:", puntaje, end="\n \n")

            imprimir_tablero(tablero)

            x = pedir_entero_positivo_validado("\n \n Ingrese la coordenada x donde desea disparar. Debe ser un numero entre 1 y 10: ")
            while x > 10:
                x = pedir_entero_positivo_validado("\n Ingrese la coordenada x donde desea disparar. Debe ser un numero entre 1 y 10: ")
        
            y = pedir_entero_positivo_validado("\n Ingrese la coordenada y donde desea disparar. Debe ser un numero entre 1 y 10: ")
            while y > 10:
                y = pedir_entero_positivo_validado("\n Ingrese la coordenada y donde desea disparar. Debe ser un numero entre 1 y 10: ")


            if tablero[y - 1][x - 1] == "O":
                print("\nFallaste\n")
                tablero[y - 1][x - 1] = "X"
                disparos_realizados += 1
                if puntaje >= 2:
                    puntaje -= 2
                else:
                    puntaje = 0
            elif tablero[y - 1][x - 1] == "X" or tablero[y - 1][x - 1] == "F":
                disparos_repetidos += 1
                print("\nDisparo ya realizado\n")
            else:
                tablero[y - 1][x - 1] = "F"
                print("\nAcertaste\n")
                disparos_realizados += 1
                puntaje += 10
                disparos_necesarios -= 1
        
        if disparos_realizados == 9:
            print("¿Eres un Robot? lo que acabas de hacer es poco probable ...")
        elif disparos_realizados < 45:
            print("Excelente Estrategia")
        elif disparos_realizados <= 70:
            print("Buena Estrategia, pero hay que mejorar")
        else:
            print("Considérese Perdedor, tiene que mejorar notablemente")
        
        

        print("\nUsername:", username)
        print("Cantidad de disparos realizados:", disparos_realizados)
        print("Puntaje total:", puntaje)
        print("Cantidad de disparos repetidos:", disparos_repetidos, "\n")
        imprimir_tablero(tablero)

        print('\n')

        actualizar_puntaje(username, puntaje, disparos_realizados)

        #Preguntando si se quiere jugar otra partida
        continuar = input("Ingrese 1 si desea volver a jugar y 0 en caso contrario: ")
        while continuar != "1" and continuar != "0":
            continuar = input("Ingrese 1 si desea volver a jugar y 0 en caso contrario: ")
        continuar = int(continuar)
