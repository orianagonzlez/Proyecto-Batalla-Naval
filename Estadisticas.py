from colorama import init, Fore, Style

init(autoreset=True)

def top10():
    '''
    Función que lee la base de datos de los usuarios y elabora e imprime una lista de los 10 usuarios registrados con mayor puntuación total.

    Dicha lista se encuentra ordenada y la primera posición es ocupada por aquel usuario con la mayor puntuación total. 
    '''
    lista_top10 = []

    with open("BaseDeDatosUsuarios.txt", "r") as archivo_usuarios:
        all_users = archivo_usuarios.readlines()

    for usuario in all_users:
        user = usuario[:-1].split(",")

        lista_top10.append(user)

    lista_top10.sort(key= lambda usuario: int(usuario[4]), reverse=True)

    print(Fore.CYAN + Style.NORMAL + '''
        
████████╗ ██████╗ ██████╗        ██╗ ██████╗   *
╚══██╔══╝██╔═══██╗██╔══██╗      ███║██╔═████╗
   ██║   ██║   ██║██████╔╝      ╚██║██║██╔██║
   ██║   ██║   ██║██╔═══╝        ██║████╔╝██║
   ██║   ╚██████╔╝██║            ██║╚██████╔╝
   ╚═╝    ╚═════╝ ╚═╝            ╚═╝ ╚═════╝ 
          ''', "\n")

    for i, usuario in enumerate(lista_top10, 1):
        if i < 11:
            print(Fore.YELLOW + Style.NORMAL + "\t" + str(i) +".", end="") 
            print("\t" + usuario[0] + "/" + usuario[4] + "/" + usuario[5] + "\n")
        else:
            break
    print("*Se muestra: nombre_de_usuario\puntuacion_total_acumulada\disparos_realizados")

def calculo_estadisticas():
    '''
    Función que lee la base de datos de los usuarios y calcula e imprime lo siguiente:
    - Rangos de edad ordenados según número de usuarios.
    - Cantidad total de puntos en partidas por género (femenino y masculino).
    - Promedio de disparos hechos para ganar.
    '''

    #En cada rango se encuentra: [edad_minima, edad_maxima, usuarios_pertenecientes]
    rangos = [[5, 18, 0], [19, 45, 0], [46, 60, 0], [61, 100, 0]]
    puntos_femenino = 0
    puntos_masculino = 0
    disparos_totales = 0
    partidas = 0

    with open("BaseDeDatosUsuarios.txt", "r") as archivo_usuarios:
        all_users = archivo_usuarios.readlines()

    for usuario in all_users:
        user = usuario[:-1].split(",")

        if user[3] == "F":
            puntos_femenino += int(user[4])
        else:
            puntos_masculino += int(user[4])

        disparos_totales += int(user[5])
        partidas += int(user[6])

        for rango in rangos:
            if rango[0] <= int(user[2]) and rango[1] >= int(user[2]):
                rango[2] += 1

    
    rangos.sort(key= lambda rango: rango[2], reverse=True)

    print(Fore.CYAN + Style.BRIGHT + "\n \n" + '''
███████╗███████╗████████╗ █████╗ ██████╗ ██╗███████╗████████╗██╗ ██████╗ █████╗ ███████╗
██╔════╝██╔════╝╚══██╔══╝██╔══██╗██╔══██╗██║██╔════╝╚══██╔══╝██║██╔════╝██╔══██╗██╔════╝
█████╗  ███████╗   ██║   ███████║██║  ██║██║███████╗   ██║   ██║██║     ███████║███████╗
██╔══╝  ╚════██║   ██║   ██╔══██║██║  ██║██║╚════██║   ██║   ██║██║     ██╔══██║╚════██║
███████╗███████║   ██║   ██║  ██║██████╔╝██║███████║   ██║   ██║╚██████╗██║  ██║███████║
╚══════╝╚══════╝   ╚═╝   ╚═╝  ╚═╝╚═════╝ ╚═╝╚══════╝   ╚═╝   ╚═╝ ╚═════╝╚═╝  ╚═╝╚══════╝
    
    ''')
         
    print(Fore.MAGENTA + Style.NORMAL + "• Rangos de edad ordenados según número de jugadores: \n")

    for rango in rangos:
        print("\t- Entre {} y {} años: {} jugador(es)".format(rango[0], rango[1], rango[2]))

    print(Fore.MAGENTA + Style.NORMAL + "\n• Cantidad total de puntos de género femenino:", puntos_femenino, "\n")
    
    print(Fore.MAGENTA + Style.NORMAL + "• Cantidad total de puntos de género masculino:", puntos_masculino, "\n")

    if partidas != 0:
        promedio_disparos = disparos_totales / partidas
        print(Fore.MAGENTA + Style.NORMAL + "• Promedio de disparos realizados para ganar:", round(promedio_disparos, 2), "\n")
    else:
        print(Fore.MAGENTA + Style.NORMAL + "• Promedio de disparos realizados para ganar:", "0")
