#Hacer estadisticas

#pendiente

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

    print(rangos)
    mas_usuarios = []

    for i, rango in enumerate(rangos):
        if mas_usuarios == []:
            mas_usuarios.append(i)
        elif rango["usuarios"] > rangos[mas_usuarios[0]]["usuarios"]:
            mas_usuarios[0] = i
        elif rango["usuarios"] == rangos[mas_usuarios[0]]["usuarios"]:
            mas_usuarios.append(i)
            
    print("\nRango(s) de edad con mas jugadores: ", end="")

    for indice in mas_usuarios:
        if indice != mas_usuarios[-1]:
            print("{} y {} anos". format(rangos[indice]["min"], rangos[indice]["max"]), end=", ")
        else:
            print("{} y {} anos". format(rangos[indice]["min"], rangos[indice]["max"]), end=".\n")

    print("Cantidad total de puntos de genero femenino:", puntos_femenino)
    print("Cantidad total de puntos de genero masculino:", puntos_masculino)
    if partidas != 0:
        print("Promedio de disparos realizados para ganar:", disparos_totales / partidas)
    else:
        print("Promedio de disparos realizados para ganar: 0") #no se
    

