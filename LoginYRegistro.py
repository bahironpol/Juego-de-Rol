from Clases import usuario

Persona = usuario()

print("Bienvenido al sistema ¿Qué acción desea realizar?")
Accion = int(input("""
               1.- Logearse
               2.- Registrarse
               """))

if Accion == 1:
    Nombre = input("Ingrese su nombre de usuario: ")
    Contraseña = input("Ingrese su contraseña: ")
    while Nombre == '' or Contraseña == '':
        print("No deje campos vacios")
        Nombre = input("Ingrese su nombre de usuario: ")
        Contraseña = input("Ingrese su contraseña: ")
    
    UsuarioExistente = Persona.Login(f'{Nombre}', f'{Contraseña}')
    
    while UsuarioExistente != True:
        print("Las credenciales proveidas no son validas")
        Nombre = input("Ingrese su nombre de usuario: ")
        Contraseña = input("Ingrese su contraseña: ")
    else:
        print("Bienvenido al sistema")
        

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
    
    while Persona.ValidarCorreo(Correo) != True:
        Correo = input("El correo ingresado no es valido \n Por favor reingrese su correo")
        Persona.correo = Correo

    while Persona.ValidarExistencia(Nombre, Correo) != True:
        Nombre = input("Reingrese su nombre ")
        Persona.nombre = Nombre
        Correo = input("Reingrese su Correo ")
        Persona.correo = Correo
    Persona.Registrarse(Nombre, Correo, Contraseña, Rol)
    print("Se ha registrado exitosamente")
