usuarios_registrados = {"origon":{"nombre":"oriana", "edad":18, "genero":"F"}}   #En el futuro sera el archivo de texto

def validar_entero_positivo(n):
    es_entero = False
    try:
        int(n)
        if int(n) >= 0:
            es_entero = True
    except:
        es_entero = False
    return es_entero

def pedir_entero_positivo_validado(mensaje):
    n = input(mensaje)
    while not validar_entero_positivo(n):
        n = input(mensaje)
    return n

def tiene_espacios(s):
    hay_espacios = False
    for char in user:
        if char == " ":
            hay_espacios = True
    return hay_espacios
    
class Usuario:
    def __init__(self, username, nombre, edad, genero, puntaje):
        self.username = username
        self.nombre = nombre
        self.edad = edad
        self.genero = genero
        self.puntaje = 0


#á é í ó ú ñ Á É Í Ó Ú Ñ 
#Pidiendo nombre de usuario sin espacios, solo con minusculas y con menos de 30 caracteres
user = input("Ingrese su nombre de usuario: ")

while tiene_espacios(user) or user != user.lower() or len(user) >= 30:
    print(tiene_espacios(user), user != user.lower(), len(user) >= 30)
    user = input("Ingrese su nombre de usuario. Solo puede utilizar letras minúsculas, no puede contener espacios y no puede tener más de 30 caracteres: ")

#Si el usuario no esta en el archivo de texto, se le pediran sus datos basicos
if user in usuarios_registrados:
    print("Bienvenido de vuelta!") #Tentativo
else:
    nombre = input("Ingrese su nombre completo: ")
    edad = pedir_entero_positivo_validado("Ingrese su edad: ")
    genero = input("Ingrese su genero: ")
    while genero.lower() != "m" and genero.lower() != "f":
        genero = input("Ingrese su genero: ")
