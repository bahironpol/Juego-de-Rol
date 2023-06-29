from Usuario import Usuario

class Jugador(Usuario):
    def __init__(self, id, nombre, rol):
        super().__init__(nombre=nombre, rol=rol)
        self.id = id
        
    def CrearPersonaje(self):
        print("Bienvenido a la pantalla de creación de personaje")
        Nombre = input("Ingrese el nombre de su personaje: ")
        ListadoRaza = self.ListarRazas()
        SeleccionRaza = int(input("Seleccione la raza (numero) que desea darle a su personaje: ")) -1
        EleccionRaza = ListadoRaza[SeleccionRaza]
        CrearPersonaje = f"""INSERT INTO personaje (nombre, nivel, fk_id_raza, fk_id_usuario, fk_id_estado)
        values ('{Nombre}', 1, {EleccionRaza[1]}, {self.id}, 1) RETURNING id"""
        self.cursor.execute(CrearPersonaje)
        id_pj_creado = self.cursor.fetchone()[0]
        self.AsignarEquipamiento(id_pj_creado)
        self.AsignarPoder(id_pj_creado, EleccionRaza) 
        self.AsignarHabilidad(id_pj_creado, EleccionRaza)
        self.AsignarHabilidad(id_pj_creado, EleccionRaza)
        print("Se ha creado su personaje exitosamente")
    
    def VerPersonajes(self):
        query = f"""select personaje.nombre, raza.nombre, personaje.nivel, estado.nombre, personaje.id
        from personaje
        left join raza on personaje.fk_id_raza = raza.id
        left join estado on personaje.fk_id_estado = estado.id
        WHERE fk_id_usuario = {self.id}
        ORDER BY id
        """
        self.cursor.execute(query)
        listaPersonaje = self.cursor.fetchall()
        HayPersonajes = bool(listaPersonaje)
        if HayPersonajes:
            print("Estos son sus personajes")
            for indice, i in enumerate(listaPersonaje):
                print(f"{indice+1}.- {i[0]} -  Nivel: {i[1]} - {i[2]} - {i[3]}")
            return listaPersonaje
        else:
            print("Usted no posee personajes")
            return HayPersonajes
        
    def AsignarEquipamiento(self, id):
        ListadoEquipamiento = self.ListarEquipamiento()
        Eleccion = int(input("Seleccione el equipamiento (numero) que desea equiparle a su personaje: ")) -1  
        EleccionEquipamiento = ListadoEquipamiento[Eleccion]
        EquiparPersonaje = f"""INSERT INTO equipamiento_personaje (fk_id_equipamiento, fk_id_personaje)
        VALUES ({EleccionEquipamiento[1]}, {id})"""
        self.cursor.execute(EquiparPersonaje)
    
    def AsignarPoder(self, id, raza):
        ListadoPoder = self.ListarPoderes(raza[1])
        Eleccion = int(input("Seleccione el poder (numero) que desea asignarle a su personaje: ")) -1
        EleccionPoder = ListadoPoder[Eleccion]
        AsociarPoder = f"""INSERT INTO poder_personaje (fk_id_poder, fk_id_personaje)
        VALUES ({EleccionPoder[3]}, {id})
        """
        self.cursor.execute(AsociarPoder)
    
    def AsignarHabilidad(self,id, raza):
        ListadoHabilidad = self.ListarHabilidades(raza[1])
        Eleccion = int(input("Seleccione la habilidad (numero) que desea asignarle a su personaje: ")) -1
        EleccionPoder = ListadoHabilidad[Eleccion]
        AsociarHabilidad = f"""INSERT INTO habilidad_personaje (fk_id_habilidad, fk_id_personaje)
        VALUES ({EleccionPoder[3]}, {id})
        """
        self.cursor.execute(AsociarHabilidad)
    
    def ModificarEquipamiento(self):
        ListadoPersonajes = self.VerPersonajes()
        HayPersonaje = bool(ListadoPersonajes)
        if HayPersonaje == False:
            print("Usted no posee personajes a los cuales modificar su equipamiento")
            return
        EleccionPersonaje = int(input("Seleccione el personaje (Numero) que desea equipar: ")) -1
        SeleccionPersonaje = ListadoPersonajes[EleccionPersonaje]
        if SeleccionPersonaje[3] == 'Muerto':
            print("No se pueden equipar personajes muertos")
            return
        EquipamientosEquipados = f"""SELECT equipamiento.nombre, equipamiento.id
        FROM equipamiento_personaje
        INNER JOIN equipamiento on equipamiento_personaje.fk_id_equipamiento = equipamiento.id
        WHERE equipamiento_personaje.fk_id_personaje = {SeleccionPersonaje[4]}
        ORDER BY id
        """
        self.cursor.execute(EquipamientosEquipados)
        ListadoEquipados = self.cursor.fetchall()
        print("Estos son los equipamientos asociados a su personaje: ")
        for indice, i in enumerate(ListadoEquipados):
            print(f"{indice+1}.- {i[0]}")
        EleccionEquipados = int(input("Seleccione (Numero) que equipamiento desea Modificar")) -1
        EquipadoSeleccionado = ListadoEquipados[EleccionEquipados]
        ListadoEquipamientos = self.ListarEquipamiento()
        EleccionEquipamiento = int(input("Seleccione el equipamiento (Numero) nuevo por el cual reemplazara el anterior: ")) -1
        EquipamientoSeleccionado = ListadoEquipamientos[EleccionEquipamiento]
        Reemplazo = f""" equipamiento_personaje
        SET fk_id_equipamiento = {EquipamientoSeleccionado[1]}
        WHERE personaje_equipamiento.id = {EquipadoSeleccionado[1]}
        """
        self.cursor.execute(Reemplazo)
        
    def asociarPJaPartida(self):
        ListadoPersonajes = self.VerPersonajes()
        if ListadoPersonajes == False:
            print("Parece que no tiene personajes para asociar a partidas")
            return
        EleccionPersonaje = int(input("¿A que personaje desea asociar a una partida?"))
        SeleccionPersonaje = ListadoPersonajes[EleccionPersonaje-1]
        ListadoPartidas = self.ListarPartidas()
        EleccionPartida = int(input("¿A que partida quiere asociar a su personaje?"))
        SeleccionPartida = ListadoPartidas[EleccionPartida-1]
        Asociar = f""" INSERT INTO personaje_partida (fk_id_personaje, fk_id_partida) 
        VALUES ({SeleccionPersonaje[4]}, {SeleccionPartida[1]})"""
        self.cursor.execute(Asociar)
        print("Asociado Correctamente")
        
    def MenuOpciones(self, Opcion):
        if Opcion == 1:
            self.CrearPersonaje()
        elif Opcion == 2:
            self.VerPersonajes()
        elif Opcion == 3:
            self.asociarPJaPartida()
        elif Opcion == 4:
            self.ModificarEquipamiento()
            
