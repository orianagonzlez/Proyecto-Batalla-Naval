from FuncionesComunes import pedir_entero_positivo_validado
  
class Usuario:
    def __init__(self, username, nombre, edad, genero, puntaje = 0):
        self.username = username
        self.nombre = nombre
        self.edad = edad
        self.genero = genero
        self.puntaje = puntaje

    def __str__(self):
        return " Usuario: {} \n Nombre completo: {} \n Edad: {} \n Genero: {} \n Puntaje: {}\n".format(self.username, self.nombre, self.edad, self.genero, self.puntaje)

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
        archivo_usuarios = open("BaseDeDatosUsuarios.txt", "r")

        for usuario in archivo_usuarios.readlines():
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
    archivo_usuarios =  open("BaseDeDatosUsuarios.txt", "r")  
    
    for usuario in archivo_usuarios.readlines():
        user = usuario[:-1].split(",")
        if user[0] == username:
            return(Usuario(user[0], user[1], user[2], user[3], user[4]))

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
        while genero.lower() != "m" and genero.lower() != "f":
            genero = input("Ingrese su genero: ")

        usuario = Usuario(user, nombre, edad, genero)

        archivo_usuarios = open("BaseDeDatosUsuarios.txt", "a+")

        archivo_usuarios.write("{},{},{},{},{}\n".format(usuario.username, usuario.nombre, usuario.edad, usuario.genero, usuario.puntaje))

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
    while dato < 1 and dato > 4:
        dato = pedir_entero_positivo_validado("Ingrese el numero de la opcion que desea modificar: ")
    
    archivo_usuarios = open("BaseDeDatosUsuarios.txt", "r")

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
            elif dato == 3:
                print("escogi", dato)
                nuevo_valor = pedir_entero_positivo_validado("Ingrese su edad: ")
            elif dato == 4:
                print("escogi", dato)
                nuevo_valor = input("Ingrese su genero ('M' es masculino y 'F' es fememino): ")
                while nuevo_valor.lower() != "m" and nuevo_valor.lower() != "f":
                    nuevo_valor = input("Ingrese su genero: ")
            
            usuario_as_lista[dato - 1] = nuevo_valor

            usuario_as_str = ",".join(usuario_as_lista) + "\n"

            datos_usuarios[i] = usuario_as_str

            print("modificado", datos_usuarios)

            archivo_usuarios = open("BaseDeDatosUsuarios.txt", "w")

            archivo_usuarios.writelines(datos_usuarios)

            print("Sus datos han sido actualizados.\n")
            print(buscar(username))
            print(username)
            return username



def control_usuarios(quiere_actualizar, username=""):
    '''
    Se encarga del registro y actualizacion de datos de los usuarios. 
    
    Si el argumento se traduce como verdadero se realiza una actualizacion de datos,
    de lo contrario se realiza el ingreso del usuario. 
    '''

    if quiere_actualizar:
        actualizar(username)
    else:
        print("Bienvenido al sistema de registro de usuarios de Batalla Naval.\n")
        return registrar()


    
