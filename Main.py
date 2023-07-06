from LoginRegister import Login, Registrarse,ValidarNombre, ValidarContraseña, ValidarCorreo, ValidarExistencia
from Jugador import Jugador, MenuJugador
from GameMaster import GameMaster, MenuGM

print("Bienvenido al sistema ¿Qué acción desea realizar?")
Accion = input("""
               1.- Logearse
               2.- Registrarse
               """)

while Accion not in ['1', '2']:
    Accion = input("La opción es invalida por favor ingrese un opcion valida ")
if Accion == '1':
    print("Bienvenido a la pantalla de ingreso de usuarios por favor ingrese los datos que le solicitaremos ")
    Nombre = input("Ingrese su nombre de usuario: ")
    Contraseña = input("Ingrese su contraseña: ")
    while Nombre == '' or Contraseña == '':
        print("No deje campos vacios")
        Nombre = input("Ingrese su nombre de usuario: ")
        Contraseña = input("Ingrese su contraseña: ")
    UsuarioExistente = Login(f'{Nombre.lower()}', f'{Contraseña.lower()}')
    
    while UsuarioExistente[0] == False:
        print("Las credenciales proveidas no son validas")
        Nombre = input("Ingrese su nombre de usuario: ")
        Contraseña = input("Ingrese su contraseña: ")
        UsuarioExistente = Login(f'{Nombre.lower()}', f'{Contraseña.lower()}')
    else:
        print("Bienvenido al sistema")
        
    match UsuarioExistente[1][4]:
        case "jugador":
            jugador = Jugador(UsuarioExistente[1][0], UsuarioExistente[1][1], UsuarioExistente[1][4])
            print(f"Bienvenido {jugador.nombre} ({jugador.rol})")
            print("Bienvenido al perfil de Jugador por favor seleccione una de las 4 opciones disponibles")
            while True:
                Eleccion = int(input("""
                                 1.-Crear Personaje: Cree un personaje para jugar
                                 2.- Ver Personajes: Vea Todos sus personajes
                                 3.- Asociar Personaje a una partida: Asocie a alguno de sus personajes a una partida
                                 4.- Reequipar a un personaje: Seleccione uno de sus personajes y cambiele el equipamiento
                                 """))
                MenuJugador(jugador, Eleccion)
                Seguir = input("¿Desea continuar usando el menu? Si/No: ")
                if Seguir.lower() == "no":
                    break
                print("Seleccione otra opcion")
            print("Tenga un buen dia")
        case "game master":
            gamemaster = GameMaster(UsuarioExistente[1][1], UsuarioExistente[1][4])
            print(f"Bienvenido {gamemaster.nombre} ({gamemaster.rol})")
            print("Bienvenido al menu de creacion, Eliminación y modificación de elementos de juego de rol por favor que desea modificar")
            while True:
                Eleccion = int(input("""
                                 1.- Razas: Crear y eliminar razas jugables
                                 2.- Habilidades: Crear, Modificar o Eliminar Habilidades jugables
                                 3.- Poderes: Crear, Modificar o Eliminar Poderes jugables
                                 4.- Estados : Crear, Modificar o Eliminar estados del sistema
                                 5.- Equipamientos: Cree, Modifique o Elimine equipamientos
                                 6.- Partida: Cree una nueva partida.
                                 """))
                MenuGM(gamemaster, Eleccion)
                Seguir = input("¿Desea continuar usando el menu? Si/No: ")
                if Seguir.lower() == "no":
                    break
                print("Seleccione otra opcion")
            print("Tenga un buen dia")
            
elif Accion == '2':
    print("Bienvenido a la pantalla de registro de usuarios por favor ingrese los datos que le solicitaremos ")
    Nombre = input("Ingrese su nombre de usuario: ")
    Correo = input("Ingrese su correo: ")
    Contraseña = input("Ingrese su contraseña: ")
    while True:
        while ValidarNombre(Nombre) != True:
            Nombre = input("El nombre ingresado no es valido \nPor favor reingrese su nombre: ")
            
        while ValidarCorreo(Correo) != True:
            Correo = input("El correo ingresado no es valido \nPor favor reingrese su correo: ")
        
        while ValidarContraseña(Contraseña) != True:
            Contraseña = input("La contraseña ingresada no es valida \nPor favor reingrese su contraseña: ")

        while ValidarExistencia(Nombre, Correo) != True:
            print("Estas credenciales ya se encuentran en uso por favor utilice otras")
            Nombre = input("Reingrese su nombre ")
            Correo = input("Reingrese su Correo ")
        Nombre.lower()
        Correo.lower()
        break
    
    Rol = ''
    Opcion = input(f"""
            ¿Con cual de los siguientes roles se desea registrar?
            1.- Jugador
            2.- Game Master
            """)
    while Opcion not in ['1','2']:
        Opcion = input("La opción ingresada no es valida por favor seleccione nuevamente ")
    if Opcion == '1':
        Rol = "jugador"
    elif Opcion == '2':
        Rol = "game master"

    Registrarse(Nombre, Correo, Contraseña, Rol)
    print("Se ha registrado exitosamente")