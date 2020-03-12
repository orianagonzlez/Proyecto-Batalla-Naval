from colorama import init, Fore, Back, Style

init(autoreset=True)

#Funciones usadas en varios archivos

def validar_entero_positivo(n):
    '''
    Funcion para verificar si el argumento pasado es un numero.
    '''
    es_entero = False
    try:
        int(n)
        if int(n) >= 0:
            es_entero = True
    except:
        es_entero = False
    return es_entero

def pedir_entero_positivo_validado(mensaje):
    '''
    Funcion para pedir un numero positivo hasta que el usuario ingrese realmente un numero positivo.
    '''
    n = input(mensaje)
    while not validar_entero_positivo(n):
        n = input(mensaje)
    return int(n)

def validar_nombre(nombre):
    nombre = nombre.replace(" ", "")
    return nombre.isalpha()

def imprimir_vineta(color, estilo):
    print(color + estilo + "•", end=" ")

