from random import randint

def jugar():
    class Barco:

        def __init__(self, tamano):
            self.tamano = tamano

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

                x = randint(0, 9)
                y = randint(0, 9)

                if self.tamano != 1:
                    orientacion = randint(0, 1)

                    for i in range(self.tamano):
                        if orientacion == 0:
                            if x + i > 9:
                                dentro_tablero = False
                            elif tablero_barcos[x + i][y] != "O":
                                ocupada = True
                            else:
                                if x + i != 9:
                                    if tablero_barcos[x + i + 1][y] != "O":
                                        contigua = True
                                if x + i != 0:
                                    if tablero_barcos[x + i - 1][y] != "O":
                                        contigua = True
                                if y != 9:
                                    if tablero_barcos[x + i][y + 1] != "O":
                                        contigua = True
                                if y != 0:
                                    if tablero_barcos[x + i][y - 1] != "O":
                                        contigua = True
                        else:
                            if y + i > 9:
                                dentro_tablero = False
                            elif tablero_barcos[x][y + i] != "O":
                                ocupada = True
                            else:
                                if x != 9:
                                    if tablero_barcos[x + 1][y + i] != "O":
                                        contigua = True
                                if x != 0:
                                    if tablero_barcos[x - 1][y + i] != "O":
                                        contigua = True
                                if y + i != 9:
                                    if tablero_barcos[x][y + i + 1] != "O":
                                        contigua = True
                                if y + i != 0:
                                    if tablero_barcos[x][y + i - 1] != "O":
                                        contigua = True
                            #TODO: QUE CHEQUEE CONTIGUO, DENTRO Y OCUPADADO PARA SUBMARINO
            print("sali")
            for i in range(self.tamano):
                if self.tamano != 1:
                    if orientacion == 0:
                        tablero_barcos[x + i][y] = "B"
                    else:
                        tablero_barcos[x][y + i] = "B"
                else:
                    tablero_barcos[x][y] = "B"

    #Creando bucle que asegurara que el usuario pueda jugar tantas veces como quiera
    continuar = 1    
    while continuar:
        #TODO
        tablero_barcos = [
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

        tablero_disparos = [
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
        
        portavion = Barco(3)
        portavion.posicion()

        buque = Barco(2)
        buque.posicion()

        submarino1 = Barco(1)
        submarino1.posicion()

        submarino2 = Barco(1)
        submarino2.posicion()

        submarino3 = Barco(1)
        submarino3.posicion()

        submarino4 = Barco(1)
        submarino4.posicion()

        for fila in tablero_barcos:
            for columna in fila:
                print(columna, end=" ")
            print("")
        
        



        print("jugando partida")

        #Preguntando si se quiere jugar otra partida
        continuar = input("Ingrese 1 si desea volver a jugar y 0 en caso contrario: ")
        while continuar != "1" and continuar != "0":
            continuar = input("Ingrese 1 si desea volver a jugar y 0 en caso contrario: ")
        continuar = int(continuar)

jugar()