from Clases import Login, Registrarse, ValidarCorreo, ValidarExistencia, GameMaster, Jugador

print("Bienvenido al sistema ¿Qué acción desea realizar?")
Accion = int(input("""
               1.- Logearse
               2.- Registrarse
               """))

if Accion == 1:
    print("Bienvenido a la pantalla de ingreso de usuarios por favor ingrese los datos que le solicitaremos ")
    nombre = input("Ingrese su nombre de usuario: ")
    Contraseña = input("Ingrese su contraseña: ")
    while Nombre == '' or Contraseña == '':
        print("No deje campos vacios")
        Nombre = input("Ingrese su nombre de usuario: ")
        Contraseña = input("Ingrese su contraseña: ")
        
    UsuarioExistente = Login(f'{nombre}', f'{Contraseña}')
    
    while UsuarioExistente == False:
        print("Las credenciales proveidas no son validas")
        Nombre = input("Ingrese su nombre de usuario: ")
        Contraseña = input("Ingrese su contraseña: ")
        UsuarioExistente = Login(f'{nombre}', f'{Contraseña}')
    else:
        print("Bienvenido al sistema")
        
    match UsuarioExistente[1][4]:
        case "jugador":
            jugador = Jugador(UsuarioExistente[1][0], UsuarioExistente[1][1], UsuarioExistente[1][4])
            print(f"Bienvenido {jugador.nombre} ({jugador.rol})")
            
            
        case "game master":
            gamemaster = GameMaster(UsuarioExistente[1][1], UsuarioExistente[1][4])
            print(f"Bienvenido {gamemaster.nombre} ({gamemaster.rol})")
            
            

elif Accion == 2:
    print("Bienvenido a la pantalla de registro de usuarios por favor ingrese los datos que le solicitaremos ")
    Nombre = input("Ingrese su nombre de usuario: ")
    Correo = input("Ingrese su correo: ")
    Contraseña = input("Ingrese su contraseña: ")
    Rol = ''
    Opcion = int(input(f"""
                ¿Con cual de los siguientes roles se desea registrar?
                1.- Game Master
                2.- Jugador
                """))

    if Opcion == 1:
        Rol = "jugador"
    elif Opcion == 2:
        Rol = "game master"
    
    while ValidarCorreo(Correo) != True:
        Correo = input("El correo ingresado no es valido \n Por favor reingrese su correo")

    while ValidarExistencia(Nombre, Correo) != True:
        Nombre = input("Reingrese su nombre ")
        Correo = input("Reingrese su Correo ")
    Registrarse(Nombre, Correo, Contraseña, Rol)
    print("Se ha registrado exitosamente")
