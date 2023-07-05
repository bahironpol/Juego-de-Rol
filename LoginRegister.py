import re
from Database import conexion

def Login(nombre, contraseña):
    query = f"SELECT * from usuario WHERE nombre = '{nombre}' AND contraseña = '{contraseña}'"
    cursor = conexion.cursor()
    cursor.execute(query)
    datos = cursor.fetchone()
    existe = bool(datos)
    return existe, datos

def ValidarNombre(Nombre):
    LongitudNombre = len(Nombre)
    BuscadorCaracteres = r"[^A-Za-záéíóúñÁÉÍÓÚÑ\s]"
    CaracterInvalido = re.findall(BuscadorCaracteres, Nombre)
    
    if LongitudNombre <=0 or CaracterInvalido:
        return False
    return True
    
def ValidarCorreo(Correo):
    valido = re.match(r'\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,}\b', Correo)
    if not (valido) or  Correo == '':
        return False
    return True

def ValidarContraseña(Contraseña):
    LogintudPassword = len(Contraseña)
    if LogintudPassword < 8:
        return False
    return True
        
def ValidarExistencia(Nombre, Correo):
    query = f"SELECT * from usuario WHERE nombre = '{Nombre}' or correo = '{Correo}'"
    cursor = conexion.cursor()
    cursor.execute(query)
    datos = cursor.fetchall()
    existe = bool(datos)
    if existe:
        return False
    return True
        
def Registrarse(nombre, correo, contraseña, rol):       
    cursor = conexion.cursor() 
    InsertarUsuario = f"""
    INSERT INTO usuario (nombre, correo, contraseña, rol) values
    ('{nombre}', '{correo}','{contraseña}', '{rol}')"""
    cursor.execute(InsertarUsuario)

def MenuGM (GM, Opcion):
    if Opcion == 1:
        Eleccion = int(input("""¿Qué desea realizar con las razas? 
                        1.- Agregar una raza
                        2.- Eliminar una raza"""))
        if Eleccion == 1:
            GM.AgregarRaza()
        elif Eleccion == 2:
            GM.EliminarRaza()
            
    elif Opcion == 2:
        Eleccion = int(input("""¿Qué desea realizar con las habilidades? 
                        1.- Agregar una habilidad
                        2.- Modificar una habilidad
                        3.- Eliminar una habilidad"""))
        if Eleccion == 1:
            GM.AgregarHabilidad()
        elif Eleccion == 2:
            GM.EditarHabilidad()
        elif Eleccion == 3:
            GM.EliminarHabilidad()
            
    elif Opcion == 3:
        Eleccion = int(input("""¿Qué desea realizar con los poderes? 
                        1.- Agregar un Poder
                        2.- Modificar un poder
                        3.- Eliminar un poder"""))
        if Eleccion == 1:
            GM.AgregarPoder()
        elif Eleccion == 2:
            GM.EditarPoder()
        elif Eleccion == 3:
            GM.EliminarPoder()
            
    elif Opcion == 4:
        Eleccion = int(input("""¿Qué desea realizar con los estados? 
                        1.- Agregar un estado
                        2.- Modificar un estado
                        3.- Eliminar un estado"""))
        if Eleccion == 1:
            GM.AgregarEstado()
        elif Eleccion == 2:
            GM.EditarEstado()
        elif Eleccion == 3:
            GM.EliminarEstado()
            
    elif Opcion == 5:
        Eleccion = int(input("""¿Qué desea realizar con los equipamientos? 
                        1.- Agregar un equipamiento
                        2.- Modificar un equipamiento
                        3.- Eliminar un equipamiento"""))
        if Eleccion == 1:
            GM.AgregarEquipamiento()
        elif Eleccion == 2:
            GM.EditarEquipamiento()
        elif Eleccion == 3:
            GM.EliminarEquipamiento()
    elif Opcion == 6:
        GM.crearPartida()