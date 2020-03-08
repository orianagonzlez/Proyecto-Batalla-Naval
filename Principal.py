#Funcion principal
from FuncionesComunes import pedir_entero_positivo_validado
from Usuarios import control_usuarios
from Juego import jugar

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
        4. Finalizar programa
        ''')

        accion = pedir_entero_positivo_validado("Selecione una opcion: ")
        while accion < 1 or accion > 4:
            accion = pedir_entero_positivo_validado("Selecione una opcion: ")

        if accion == 1:
            jugar(user.username)
        elif accion == 2:
            user = control_usuarios(1, username=user.username)
        elif accion == 3:
            user = control_usuarios(0)
            print(user)
        else:
            continuar = 0
        
main()



