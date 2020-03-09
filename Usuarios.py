from FuncionesComunes import pedir_entero_positivo_validado
  
class Usuario:
    def __init__(self, username, nombre, edad, genero, puntos_totales = "0", disparos = "0", partidas = "0"):
        self.username = username
        self.nombre = nombre
        self.edad = edad
        self.genero = genero
        self.puntos_totales = puntos_totales
        self.disparos = disparos
        self.partidas = partidas

    def __str__(self):
        return " Usuario: {} \n Nombre completo: {} \n Edad: {} \n Genero: {} \n Puntos totales: {}\n".format(self.username, self.nombre, self.edad, self.genero, self.puntos_totales)

def tiene_espacios(username):
    '''
    Funcion para detectar espacios en un string.
    '''
    hay_espacios = False
    for char in username:
        if char == " ":
            hay_espacios = True
    return hay_espacios

def verificar_username(username):
    '''
    Recibe como argumento el nombre de usuario y verifica si este ya se encuentra en el archivo de texto.

    Si el usuario ya esta registrado retorna verdadero, si no retorna falso.
    '''
    try:
        with open("BaseDeDatosUsuarios.txt", "r") as archivo_usuarios:
            all_users = archivo_usuarios.readlines()
        for usuario in all_users:
            user = usuario[:-1].split(",")
            print('user', user)
            if user[0] == username:
                return True
        return False
    except:
        print("Todavia no hay ningun usuario registrado. Ingrese los datos pedidos a continuacion para registrarse \n")

def buscar(username):
    '''
    Funcion para buscar al usuario en el archivo de texto que retorna al usuario como objeto
    '''
    with open("BaseDeDatosUsuarios.txt", "r") as archivo_usuarios:
        all_users = archivo_usuarios.readlines()
    for usuario in all_users:
        user = usuario[:-1].split(",")
        print(user)
        if user[0] == username:
            print("lo encontre")
            return Usuario(user[0], user[1], user[2], user[3], user[4])

def registrar():
    '''
    Funcion para registrar a un usuario en el archivo de texto
    '''

    print("Por favor, ingrese los siguientes datos.\n")

    #Pidiendo nombre de usuario sin espacios, solo con minusculas y con menos de 30 caracteres
    user = input("Ingrese su nombre de usuario: ")

    while tiene_espacios(user) or user != user.lower() or len(user) >= 30:
        print(tiene_espacios(user), user != user.lower(), len(user) >= 30)
        user = input("Ingrese su nombre de usuario. Solo puede utilizar letras minúsculas, no puede contener espacios y no puede tener más de 30 caracteres: ")

    #Si el usuario no esta en el archivo de texto, se le pediran sus datos basicos
    if verificar_username(user):
        print("Bienvenido de vuelta! A continuacion se muestran sus datos registrados:\n") 
        return buscar(user)
        
    else:
        nombre = input("Ingrese su nombre completo: ")
        edad = pedir_entero_positivo_validado("Ingrese su edad: ")
        genero = input("Ingrese su genero ('M' es masculino y 'F' es fememino): ")
        while genero.upper() != "M" and genero.upper() != "F":
            genero = input("Ingrese su genero: ")

        usuario = Usuario(user, nombre.title(), edad, genero.upper())

        with open("BaseDeDatosUsuarios.txt", "a+") as archivo_usuarios:
            archivo_usuarios.write("{},{},{},{},{},{},{}\n".format(usuario.username, usuario.nombre, usuario.edad, usuario.genero, usuario.puntos_totales, usuario.disparos, usuario.partidas))

        print("\nEl usuario '{}' se ha registrado correctamente\n".format(usuario.username))
        return usuario

def actualizar(username):
    '''
    Funcion para actualizar los datos de un usuario registrado en el archivo de texto.

    Toma como argumento el nombre de usuario.
    '''
    print('''
    Que dato desea modificar?

    1. Nombre de usuario
    2. Nombre completo
    3. Edad
    4. Genero
    ''')

    dato = pedir_entero_positivo_validado("Ingrese el numero de la opcion que desea modificar: ")
    while dato < 1 or dato > 4:
        dato = pedir_entero_positivo_validado("Ingrese el numero de la opcion que desea modificar: ")
    
    with open("BaseDeDatosUsuarios.txt", "r") as archivo_usuarios:
        datos_usuarios = archivo_usuarios.readlines()

    print(datos_usuarios)

    for i, usuario in enumerate(datos_usuarios):
        print("recorriendo usuarios")
        usuario_as_lista = usuario[:-1].split(",")
        if usuario_as_lista[0] == username:
            print("encontre ussuairo")
            if dato == 1:
                print("escogi", dato)
                nuevo_valor = input("Ingrese el nuevo nombre de usuario: ")

                while tiene_espacios(nuevo_valor) or nuevo_valor != nuevo_valor.lower() or len(nuevo_valor) >= 30:
                    nuevo_valor = input("Ingrese el nuevo nombre de usuario. Solo puede utilizar letras minúsculas, no puede contener espacios y no puede tener más de 30 caracteres: ")
                
                username = nuevo_valor
            elif dato == 2:
                print("escogi", dato)
                nuevo_valor = input("Ingrese su nombre completo: ")
                nuevo_valor = nuevo_valor.title()
            elif dato == 3:
                print("escogi", dato)
                nuevo_valor = str(pedir_entero_positivo_validado("Ingrese su edad: "))
            elif dato == 4:
                print("escogi", dato)
                nuevo_valor = input("Ingrese su genero ('M' es masculino y 'F' es fememino): ")
                while nuevo_valor.upper() != "M" and nuevo_valor.upper() != "F":
                    nuevo_valor = input("Ingrese su genero: ")

                nuevo_valor = nuevo_valor.upper()
            
            usuario_as_lista[dato - 1] = nuevo_valor

            usuario_as_str = ",".join(usuario_as_lista) + "\n"

            datos_usuarios[i] = usuario_as_str

            print("modificado", datos_usuarios)

            with open("BaseDeDatosUsuarios.txt", "w") as archivo_usuarios:
                archivo_usuarios.writelines(datos_usuarios)
    

            print("Sus datos han sido actualizados.\n")

            return buscar(username)



def control_usuarios(quiere_actualizar, username=""):
    '''
    Se encarga del registro y actualizacion de datos de los usuarios. 
    
    Si el argumento se traduce como verdadero se realiza una actualizacion de datos,
    de lo contrario se realiza el ingreso del usuario. 
    '''

    if quiere_actualizar:
        return actualizar(username)
    else:
        print("\nBienvenido al sistema de registro de usuarios de Batalla Naval.\n")
        return registrar()


    
