import psycopg2

conexion = psycopg2.connect(
    database="Juego_Rol",
    user="postgres",
    password ="postgres",
    host = "localhost",
    port="5432"
)

conexion.autocommit = True

def creartablas():
    cur = conexion.cursor()
    TablaUsuario = '''
    CREATE TABLE usuario 
    (id serial not null PRIMARY KEY, 
    nombre varchar(25),
    correo varchar(50),
    contraseña varchar(50),
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
    

def insetarvalor():
    cur = conexion.cursor()
    InsertarJugador = f"""
    INSERT INTO usuario (nombre, correo, contraseña, rol) values
    ('Ejemplo', 'correoejemplo@hotmail.com','password123', 'jugador')"""
    InsertarEstado1 = f"""
    INSERT INTO estado (nombre, efecto) values
    ('Vivo', 'El personaje se encuentra vivo y puede realizar acciones')"""
    InsertarEstado2 = f"""
    INSERT INTO estado (nombre, efecto) values
    ('Muerto', 'El personaje se encuentra muerto por lo cual se encuentra inhabilitado de cualquier funcion')"""
    InsertarRaza1 = f"""
    INSERT INTO raza (nombre) values
    ('elfo')
    """
    InsertarRaza2 = f"""
    INSERT INTO raza (nombre) values
    ('orco')
    """
    InsertarHabilidadElfo1 = f"""
    INSERT INTO habilidad (nombre, descripcion, fk_id_raza) 
    values ('Sigilo', 'Le permite no ser detectado por los enemigos cuando esta cerca', 1)
    """
    InsertarHabilidadElfo2 = f"""
    INSERT INTO habilidad (nombre, descripcion, fk_id_raza) 
    values ('Cabalgar', 'Le permite cabalgar bestias domesticadas', 1)
    """
    InsertarHabilidadOrco1 = f"""
    INSERT INTO habilidad (nombre, descripcion, fk_id_raza) 
    values ('Furia', 'Cuando su vida se encuentra por debajo del 50% aumenta su ataque', 2)
    """
    InsertarHabilidadOrco2 = f"""
    INSERT INTO habilidad (nombre, descripcion, fk_id_raza) 
    values ('Robustez', 'Es inmune a los efectos de empuje', 2)
    """
    InsertarPoderElfo1 =f"""
    INSERT INTO Poder (nombre, descripcion, fk_id_raza) 
    values ('Tiro cargado', 'Ataque el cual inflinge 25% mas de daño que un ataque basico', 1)
    """
    InsertarPoderElfo2 =f"""
    INSERT INTO Poder (nombre, descripcion, fk_id_raza) 
    values ('Detección', 'Realiza un rastreo del area rastreando todos los seres vivos cercanos al area', 1)
    """
    InsertarPoderOrco1 =f"""
    INSERT INTO Poder (nombre, descripcion, fk_id_raza) 
    values ('Embestida', 'Realiza un ataque en carga con todo su cuerpo el cual recorre 3 casillas hacia adelante', 2)
    """
    InsertarPoderOrco2 =f"""
    INSERT INTO Poder (nombre, descripcion, fk_id_raza) 
    values ('Empuje', 'Permite empujar a un objetivo cierto numero de casillas dependiendo de la fuerza del usuario', 2)
    """
    InsertarPersonaje1 = f"""
    INSERT INTO personaje (nombre, nivel, fk_id_raza, fk_id_usuario, fk_id_estado) 
    values ('klin', 1, 1, 1, 2)
    """
    InsertarPersonaje2 = f"""
    INSERT INTO personaje (nombre, nivel, fk_id_raza, fk_id_usuario, fk_id_estado) 
    values ('Thurm',1, 2, 1, 1)
    """
    InsertarPartida1 = f"""
    INSERT INTO partida (nombre) 
    values ('Aguas profundas')
    """
    InsertarPartida2 = f"""
    INSERT INTO partida (nombre) 
    values ('La ultima ascua ')
    """
    
    InsertarPersonajePartida1 = f"""
    INSERT INTO personaje_partida (fk_id_personaje, fk_id_partida)
    values (1,1)
    """
    InsertarPersonajePartida2 = f"""
    INSERT INTO personaje_partida (fk_id_personaje, fk_id_partida)
    values (2,1)
    """
    InsertarEquipamiento1 = f"""
    INSERT INTO equipamiento (Nombre, Tipo)
    values ('Arco', 'Arma')
    """
    InsertarEquipamiento2 = f"""
    INSERT INTO equipamiento (Nombre, Tipo)
    values ('Hombreras', 'Armadura')
    """
    InsertarEquipamiento3 = f"""
    INSERT INTO equipamiento (Nombre, Tipo)
    values ('Hacha', 'Arma')
    """
    InsertarEquipamientoPersonaje1 = f"""
    INSERT INTO equipamiento_personaje (fk_id_equipamiento, fk_id_personaje)
    values (2,2)
    """
    InsertarEquipamientoPersonaje2 = f"""
    INSERT INTO equipamiento_personaje (fk_id_equipamiento, fk_id_personaje)
    values (3,2)
    """
    InsertarEquipamientoPersonaje3 = f"""
    INSERT INTO equipamiento_personaje (fk_id_equipamiento, fk_id_personaje)
    values (1,1)
    """
    InsertarHabilidad_Personaje1 = f"""
    INSERT INTO habilidad_personaje (fk_id_habilidad, fk_id_personaje)
    values (1,1)
    """
    InsertarPoder_Personaje1 = f"""
    INSERT INTO poder_personaje (fk_id_poder, fk_id_personaje)
    values (1,2)
    """
    
    cur.execute(InsertarJugador)
    cur.execute(InsertarEstado1)
    cur.execute(InsertarEstado2)
    cur.execute(InsertarRaza1)
    cur.execute(InsertarRaza2)
    cur.execute(InsertarHabilidadElfo1)
    cur.execute(InsertarHabilidadElfo2)
    cur.execute(InsertarHabilidadOrco1)
    cur.execute(InsertarHabilidadOrco2)
    cur.execute(InsertarPoderElfo1)
    cur.execute(InsertarPoderElfo2)
    cur.execute(InsertarPoderOrco1)
    cur.execute(InsertarPoderOrco2)
    cur.execute(InsertarPersonaje1)
    cur.execute(InsertarPersonaje2)
    cur.execute(InsertarPartida1)
    cur.execute(InsertarPartida2)
    cur.execute(InsertarPersonajePartida1)
    cur.execute(InsertarPersonajePartida2)
    cur.execute(InsertarEquipamiento1)
    cur.execute(InsertarEquipamiento2)
    cur.execute(InsertarEquipamiento3)
    cur.execute(InsertarEquipamientoPersonaje1)
    cur.execute(InsertarEquipamientoPersonaje2)
    cur.execute(InsertarEquipamientoPersonaje3)
    cur.close()


# creartablas()
# insetarvalor()
# conexion.close()