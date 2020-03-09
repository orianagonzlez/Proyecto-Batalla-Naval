#Funcion principal
from FuncionesComunes import pedir_entero_positivo_validado
from Usuarios import control_usuarios
from Juego import jugar
from Estadisticas import calculo_estadisticas

def main():
    '''
    Funcion que controla todo el programa.
    '''
    print("-"*60 + "BATALLA NAVAL" + "-"*60 +"\n \n")
    print("Bienvenido al juego Batalla Naval! \n \n")


    user = control_usuarios(0)
    print(user)

    continuar = 1
    while continuar:
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
        elif accion == 2:
            user = control_usuarios(1, username= user.username)
            print(user)

        elif accion == 3:
            user = control_usuarios(0)
            print(user)
        elif accion == 4:
            calculo_estadisticas()
        else:
            continuar = 0
        
main()



