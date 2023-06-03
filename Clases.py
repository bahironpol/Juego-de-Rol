import re
from BD import conexion

conexion.autocommit = True

def Login(nombre, contraseña):
    query = f"SELECT * from usuario WHERE nombre = '{nombre}' AND contraseña = '{contraseña}'"
    cursor = conexion.cursor()
    cursor.execute(query)
    datos = cursor.fetchone()
    existe = bool(datos)
    if existe:
        return existe, datos
    return existe

def Registrarse(nombre, correo, contraseña, rol):       
    cursor = conexion.cursor() 
    InsertarUsuario = f"""
    INSERT INTO usuario (nombre, correo, contraseña, rol) values
    ('{nombre}', '{correo}','{contraseña}', '{rol}')"""
    cursor.execute(InsertarUsuario)

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

class Jugador:
    def __init__(self, id, nombre, rol):
        self.nombre = nombre
        self.id = id
        self.rol = rol
        self.conexion = conexion
        self.cursor = conexion.cursor()       
        
class GameMaster:
    def __init__(self, nombre, rol):
        self.nombre = nombre
        self.rol = rol
        self.conexion = conexion
        self.cursor = conexion.cursor()