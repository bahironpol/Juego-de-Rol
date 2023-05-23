import psycopg2
import re
conexion = psycopg2.connect(
    database="Juego_Rol",
    user="postgres",
    password ="postgres",
    host = "localhost",
    port="5432"
)

conexion.autocommit = True

class usuario:
    def __init__(self):
        self.nombre = None
        self.correo = None
        self.contraseña = None
        self.rol = None
        self.conexion = conexion
        self.cursor = conexion.cursor()
    
    def Login(self, nombre, contraseña):
        query = f"SELECT * from usuario WHERE nombre = '{nombre}' AND contraseña = '{contraseña}'"
        self.cursor.execute(query)
        datos = self.cursor.fetchone()
        existe = bool(datos)
        if existe:
            self.nombre = datos[1]
            self.correo = datos[2]
            self.contraseña = datos[3]
            self.rol = datos[4]
            return existe
        
    def ValidarCorreo(self, Correo):
        valido = re.match(r'\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,}\b', Correo)
        if not (valido):
            return False
        return True
        
    def ValidarExistencia(self, Nombre, Correo):
        query = f"SELECT * from usuario WHERE nombre = '{Nombre}' or correo = '{Correo}'"
        self.cursor.execute(query)
        datos = self.cursor.fetchall()
        existe = bool(datos)
        if existe:
            print("El nombre de usuario o correo ya se encuentran en uso por favor ingrese otros datos")
            return False
        return True
        
    def Registrarse(self, nombre, correo, contraseña, rol):        
        InsertarJugador = f"""
        INSERT INTO usuario (nombre, correo, contraseña, rol) values
        ('{nombre}', '{correo}','{contraseña}', '{rol}')"""
        self.cursor.execute(InsertarJugador)
           
class GameMaster(usuario):
    def __init__(self):
        super().__init__()
        

class Jugador(usuario):
    def __init__(self):
        super().__init__()
    def VerPersonajes():
        pass
    
    




 