from colorama import init, Fore, Style

init(autoreset=True)

def top10():
    '''
    Funcion que elabora el top 10.
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
    print(Style.DIM + "*Se muestra: nombre_de_usuario\puntuacion_total\disparos_realizados")



def calculo_estadisticas():

    rangos = [{"min": 5, "max": 18, "usuarios": 0},{"min": 19, "max": 45, "usuarios": 0},{"min": 46, "max": 60, "usuarios": 0},{"min": 61, "max": 100, "usuarios": 0}]
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
            if rango["min"] <= int(user[2]) and rango["max"] >= int(user[2]):
                rango["usuarios"] += 1

    mas_usuarios = []

    for i, rango in enumerate(rangos):
        if mas_usuarios == []:
            mas_usuarios.append(i)
        elif rango["usuarios"] > rangos[mas_usuarios[0]]["usuarios"]:
            mas_usuarios[0] = i
        elif rango["usuarios"] == rangos[mas_usuarios[0]]["usuarios"]:
            mas_usuarios.append(i)

    promedio_disparos = disparos_totales / partidas

    print(Fore.CYAN + Style.BRIGHT + "\n \n" + '''
███████╗███████╗████████╗ █████╗ ██████╗ ██╗███████╗████████╗██╗ ██████╗ █████╗ ███████╗
██╔════╝██╔════╝╚══██╔══╝██╔══██╗██╔══██╗██║██╔════╝╚══██╔══╝██║██╔════╝██╔══██╗██╔════╝
█████╗  ███████╗   ██║   ███████║██║  ██║██║███████╗   ██║   ██║██║     ███████║███████╗
██╔══╝  ╚════██║   ██║   ██╔══██║██║  ██║██║╚════██║   ██║   ██║██║     ██╔══██║╚════██║
███████╗███████║   ██║   ██║  ██║██████╔╝██║███████║   ██║   ██║╚██████╗██║  ██║███████║
╚══════╝╚══════╝   ╚═╝   ╚═╝  ╚═╝╚═════╝ ╚═╝╚══════╝   ╚═╝   ╚═╝ ╚═════╝╚═╝  ╚═╝╚══════╝
    
    ''')
         
    print(Fore.MAGENTA + Style.NORMAL + "• Rango(s) de edad con mas jugadores: ", end="")

    for indice in mas_usuarios:
        if indice != mas_usuarios[-1]:
            print("{} y {} anos". format(rangos[indice]["min"], rangos[indice]["max"]), end=", ")
        else:
            print("{} y {} anos". format(rangos[indice]["min"], rangos[indice]["max"]), end=".\n \n")

    
    print(Fore.MAGENTA + Style.NORMAL + "• Cantidad total de puntos de genero femenino:", puntos_femenino, "\n")
    
    print(Fore.MAGENTA + Style.NORMAL + "• Cantidad total de puntos de genero masculino:", puntos_masculino, "\n")

    if partidas != 0:
        print(Fore.MAGENTA + Style.NORMAL + "• Promedio de disparos realizados para ganar:", round(promedio_disparos, 2), "\n")
    else:
        print(Fore.MAGENTA + Style.NORMAL + "• Promedio de disparos realizados para ganar:", "0") #probar

    
