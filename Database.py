import psycopg2

conexion = psycopg2.connect(
    database="Juego_Rol",
    user="postgres",
    password ="postgres",
    host = "localhost",
    port="5432"
)

conexion.autocommit = True

def CrearTablas():
    cur = conexion.cursor()
    TablaUsuario = '''
    CREATE TABLE usuario 
    (id serial not null PRIMARY KEY, 
    nombre varchar(25),
    correo varchar(50),
    contraseña varchar(150),
    rol varchar(20)
    )
    '''
    TablaEstado = '''
    CREATE TABLE estado
    (id serial not null PRIMARY KEY,
    nombre varchar(25),
    efecto varchar(150)
    )
    '''
    TablaRaza = '''
    CREATE TABLE raza 
    (id serial not null PRIMARY KEY,
    nombre varchar(25)
    )
    '''
    TablaHabilidad = '''
    CREATE TABLE Habilidad
    (id serial not null PRIMARY KEY,
    nombre varchar(50),
    descripcion varchar(200),
    fk_id_raza integer REFERENCES raza(id)
    )
    '''
    TablaPoder = '''
    CREATE TABLE Poder
    (id serial not null PRIMARY KEY,
    nombre varchar(50),
    descripcion varchar(200),
    fk_id_raza integer REFERENCES raza(id)
    )
    '''
    TablaPersonaje = '''
    CREATE TABLE personaje
    (id serial not null PRIMARY KEY,
    nombre varchar(50),
    nivel integer,
    fk_id_raza integer REFERENCES raza(id),
    fk_id_usuario integer REFERENCES usuario(id),
    fk_id_estado integer REFERENCES estado(id)
    )
    '''
    TablaPartida = '''
    CREATE TABLE partida
    (id serial not null PRIMARY KEY,
    nombre varchar(50)
    )
    '''
    TablaPersonaje_Partida = '''
    CREATE TABLE personaje_partida
    (id serial not null PRIMARY KEY,
    fk_id_personaje integer REFERENCES personaje(id),
    fk_id_partida integer REFERENCES partida(id)
    )
    '''
    TablaEquipamiento = '''
    CREATE TABLE equipamiento
    (id serial not null PRIMARY KEY,
    nombre varchar(50),
    Tipo varchar(50)
    )
    '''
    TablaEquipamiento_Personaje = '''
    CREATE TABLE equipamiento_personaje
    (id serial not null PRIMARY KEY,
    fk_id_equipamiento integer REFERENCES equipamiento(id),
    fk_id_personaje integer REFERENCES personaje(id)
    )
    '''
    
    TablaHabilidad_Personaje = f'''
    CREATE TABLE Habilidad_Personaje
    (id serial not null PRIMARY KEY,
    fk_id_habilidad integer REFERENCES Habilidad(id),
    fk_id_personaje integer REFERENCES personaje(id)
    )
    '''
    
    TablaPoder_Personaje = f'''
    CREATE TABLE Poder_Personaje
    (id serial not null PRIMARY KEY,
    fk_id_poder integer REFERENCES Poder(id),
    fk_id_personaje integer REFERENCES personaje(id)
    )
    '''
    cur.execute(TablaUsuario)
    cur.execute(TablaEstado)
    cur.execute(TablaRaza)
    cur.execute(TablaHabilidad)
    cur.execute(TablaPoder)
    cur.execute(TablaPersonaje)
    cur.execute(TablaPartida)
    cur.execute(TablaPersonaje_Partida)
    cur.execute(TablaEquipamiento)
    cur.execute(TablaEquipamiento_Personaje)
    cur.execute(TablaHabilidad_Personaje)
    cur.execute(TablaPoder_Personaje)
    cur.close()
    

def InsertarEstados():
    cur = conexion.cursor()
    InsertarEstado1 = f"""
    INSERT INTO estado (nombre, efecto) values
    ('Vivo', 'El personaje se encuentra vivo y puede realizar acciones')"""
    InsertarEstado2 = f"""
    INSERT INTO estado (nombre, efecto) values
    ('Muerto', 'El personaje se encuentra muerto por lo cual se encuentra inhabilitado de cualquier funcion')"""
    cur.execute(InsertarEstado1)
    cur.execute(InsertarEstado2)
    
try:
    CrearTablas()
    InsertarEstados()
except:
    print('Cargando...')

