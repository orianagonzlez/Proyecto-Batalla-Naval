from time import sleep
from colorama import init, Fore, Style
from FuncionesComunes import pedir_entero_positivo_validado, separador
from Usuarios import control_usuarios
from Juego import jugar
from Estadisticas import calculo_estadisticas, top10

init(autoreset=True)

def main():
    '''
    Función que controla todo el juego Batalla Naval (jugar, actualizar datos, cambiar de usuario, estadísticas, finalizar).
    '''
    separador()

    print(Fore.MAGENTA + Style.BRIGHT + '''

     ██████╗  █████╗ ████████╗ █████╗ ██╗     ██╗      █████╗         ███╗   ██╗ █████╗ ██╗   ██╗ █████╗ ██╗     
     ██╔══██╗██╔══██╗╚══██╔══╝██╔══██╗██║     ██║     ██╔══██╗        ████╗  ██║██╔══██╗██║   ██║██╔══██╗██║     
     ██████╔╝███████║   ██║   ███████║██║     ██║     ███████║        ██╔██╗ ██║███████║██║   ██║███████║██║     
     ██╔══██╗██╔══██║   ██║   ██╔══██║██║     ██║     ██╔══██║        ██║╚██╗██║██╔══██║╚██╗ ██╔╝██╔══██║██║     
     ██████╔╝██║  ██║   ██║   ██║  ██║███████╗███████╗██║  ██║        ██║ ╚████║██║  ██║ ╚████╔╝ ██║  ██║███████╗
     ╚═════╝ ╚═╝  ╚═╝   ╚═╝   ╚═╝  ╚═╝╚══════╝╚══════╝╚═╝  ╚═╝        ╚═╝  ╚═══╝╚═╝  ╚═╝  ╚═══╝  ╚═╝  ╚═╝╚══════╝
    ''')

    separador()
    print("\n \nBienvenido al juego Batalla Naval! \n \n")

    sleep(1)

    user = control_usuarios(0)
    print(user)


    continuar = 1
    while continuar:

        sleep(3)
        separador()
        top10()
        separador()

        sleep(2)
        print(Fore.MAGENTA + Style.NORMAL + "Qué desea hacer?")
        print('''
    1. Jugar
    2. Actualizar datos
    3. Cambiar de usuario
    4. Ver estadísticas
    5. Finalizar programa
    ''')

        accion = pedir_entero_positivo_validado("Seleccione una opción: ")
        while accion < 1 or accion > 5:
            accion = pedir_entero_positivo_validado("Seleccione una opción: ")

        if accion == 1:
            separador()
            jugar(user.username)           
        elif accion == 2:
            separador()
            user = control_usuarios(1, username= user.username)
            print(user)          
        elif accion == 3:
            separador()
            user = control_usuarios(0)
            print(user)
        elif accion == 4:
            separador()
            calculo_estadisticas()
            sleep(2)
        else:
            print(Fore.MAGENTA + "\n\nHasta luego. Gracias por jugar!")
            separador()
            continuar = 0
        
main()
