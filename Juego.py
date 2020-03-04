import random

def posicionar_barcos(barco, lista_de_coord, tablero, posiciones):
    for coord in lista_de_coord:
        tablero[coord[1]][coord[0]] = barco
        posiciones.append(coord)

def validar_entero_positivo(n):
    es_entero = False
    try:
        int(n)
        if int(n) >= 0:
            es_entero = True
    except:
        es_entero = False
    return es_entero

def pedir_entero_positivo_validado(mensaje):
    n = input(mensaje)
    while not validar_entero_positivo(n):
        n = input(mensaje)
    return int(n)

def jugar():
    class Barco:

        def __init__(self, tamano):
            self.tamano = tamano

        def __str__(self):
            return "O"

        def posicion(self):
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

        portavion = Barco(3)
        posicionar_barcos(portavion, portavion.posicion(), tablero, posiciones_barcos)

        buque = Barco(2)
        posicionar_barcos(buque, buque.posicion(), tablero, posiciones_barcos)

        submarino1 = Barco(1)
        posicionar_barcos(submarino1, submarino1.posicion(), tablero, posiciones_barcos)

        submarino2 = Barco(1)
        posicionar_barcos(submarino2, submarino2.posicion(), tablero, posiciones_barcos)

        submarino3 = Barco(1)
        posicionar_barcos(submarino3, submarino3.posicion(), tablero, posiciones_barcos)

        submarino4 = Barco(1)
        posicionar_barcos(submarino4, submarino4.posicion(), tablero, posiciones_barcos)

        while disparos_necesarios != 0:

            print("Puntaje:", puntaje, end="\n \n")

            print("", end="\t")
            for j in range(1,11):
                print(j, end="    ")

            for i, fila in enumerate(tablero, 1):
                print("\n")
                print(i, end="\t")
                for columna in fila:
                    print(columna, end="    ")

            x = pedir_entero_positivo_validado("\n \n Ingrese la coordenada x donde desea disparar. Debe ser un numero entre 1 y 10: ")
            while x > 10:
                x = pedir_entero_positivo_validado("\n Ingrese la coordenada x donde desea disparar. Debe ser un numero entre 1 y 10: ")
        
            y = pedir_entero_positivo_validado("\n Ingrese la coordenada y donde desea disparar. Debe ser un numero entre 1 y 10: ")
            while y > 10:
                y = pedir_entero_positivo_validado("\n Ingrese la coordenada y donde desea disparar. Debe ser un numero entre 1 y 10: ")


            if tablero[y - 1][x - 1] == "O":
                print("fallaste")
                tablero[y - 1][x - 1] = "X"
                disparos_realizados += 1
                if puntaje >= 2:
                    puntaje -= 2
                else:
                    puntaje = 0
            elif tablero[y - 1][x - 1] == "X":
                disparos_repetidos += 1
                print("\nDisparo ya realizado\n")
            else:
                tablero[y - 1][x - 1] = "F"
                print("acertaste")
                disparos_realizados += 1
                puntaje += 10
                disparos_necesarios -= 1

            
            

        if disparos_realizados == 9:
            print("¿Eres un Robot? lo que acabas de hacer es poco probable ...")
        elif disparos_realizados < 45:
            print("Excelente Estrategia")
        elif disparos_realizados <= 70:
            print("Buena Estrategia; pero hay que mejorar")
        else:
            print("Considérese Perdedor, tiene que mejorar notablemente")

        print("Username:")
        print("Cantidad de disparos realizados:", disparos_realizados)
        print("Puntaje total:", puntaje)
        print("Cantidad de disparos repetidos:", disparos_repetidos)

        #Preguntando si se quiere jugar otra partida
        continuar = input("Ingrese 1 si desea volver a jugar y 0 en caso contrario: ")
        while continuar != "1" and continuar != "0":
            continuar = input("Ingrese 1 si desea volver a jugar y 0 en caso contrario: ")
        continuar = int(continuar)

jugar()