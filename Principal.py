#Funcion principal
from time import sleep
from colorama import init, Fore, Back, Style
from FuncionesComunes import pedir_entero_positivo_validado
from Usuarios import control_usuarios
from Juego import jugar
from Estadisticas import calculo_estadisticas, top10

init(autoreset=True)

def main():
    
    '''
    Funcion que controla todo el programa.
    '''
#dotmatrix

    print(Fore.MAGENTA + Style.BRIGHT + '''

██████╗  █████╗ ████████╗ █████╗ ██╗     ██╗      █████╗         ███╗   ██╗ █████╗ ██╗   ██╗ █████╗ ██╗     
██╔══██╗██╔══██╗╚══██╔══╝██╔══██╗██║     ██║     ██╔══██╗        ████╗  ██║██╔══██╗██║   ██║██╔══██╗██║     
██████╔╝███████║   ██║   ███████║██║     ██║     ███████║        ██╔██╗ ██║███████║██║   ██║███████║██║     
██╔══██╗██╔══██║   ██║   ██╔══██║██║     ██║     ██╔══██║        ██║╚██╗██║██╔══██║╚██╗ ██╔╝██╔══██║██║     
██████╔╝██║  ██║   ██║   ██║  ██║███████╗███████╗██║  ██║        ██║ ╚████║██║  ██║ ╚████╔╝ ██║  ██║███████╗
╚═════╝ ╚═╝  ╚═╝   ╚═╝   ╚═╝  ╚═╝╚══════╝╚══════╝╚═╝  ╚═╝        ╚═╝  ╚═══╝╚═╝  ╚═╝  ╚═══╝  ╚═╝  ╚═╝╚══════╝

    ''' + "\n \n")

    print("Bienvenido al juego Batalla Naval! \n \n")

    sleep(3)

    user = control_usuarios(0)
    print(user)


    continuar = 1
    while continuar:

        sleep(5)
        top10()

        sleep(3)
        print('''
    Que desea hacer?

    1. Jugar
    2. Actualizar datos
    3. Cambiar de usuario
    4. Ver estadisticas
    5. Finalizar programa
        ''')

        accion = pedir_entero_positivo_validado("Seleccione una opcion: ")
        while accion < 1 or accion > 5:
            accion = pedir_entero_positivo_validado("Seleccione una opcion: ")

        if accion == 1:
            jugar(user.username)
            sleep(3)
        elif accion == 2:
            user = control_usuarios(1, username= user.username)
            print(user)
            sleep(3)
        elif accion == 3:
            user = control_usuarios(0)
            print(user)
            sleep(3)
        elif accion == 4:
            calculo_estadisticas()
            sleep(3)
        else:
            continuar = 0
        
main()



