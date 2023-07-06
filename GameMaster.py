from Usuario import Usuario

class GameMaster(Usuario):
    def __init__(self, nombre, rol):
        super().__init__(nombre=nombre, rol=rol)
    
    def AgregarEstado(self):
        Nombre = input("Ingrese el nombre de su nuevo estado: ")
        Efecto = input("Ingrese el efecto que tiene el estado: ")
        NuevoEstado = f"""INSERT INTO estado(nombre, efecto)
        values('{Nombre}','{Efecto}')
        """
        self.cursor.execute(NuevoEstado)
    
    def EditarEstado(self):
        ListadoEstados = self.ListarEstado()
        Eleccion = int(input("Seleccione el estado (numero) que desea modificar: ")) -1
        EstadoElegido = int(ListadoEstados[Eleccion][0])
        print(EstadoElegido)
        if EstadoElegido == 1 or EstadoElegido == 2:
            print("Los estados de vivo y muerto no pueden ser modificados")
            return
        Modificar = int(input("""¿Qué desea modificar del estado en cuestion
              1.- Su nombre
              2.- Su Efecto
              3.- Ambas
              """))
        if Modificar == 1:
            NuevoNombre = input("Ingrese el nuevo nombre de su estado: ")
            Modificacion = f"""UPDATE estado 
            set nombre = '{NuevoNombre}' 
            WHERE  id = {EstadoElegido}"""
            self.cursor.execute(Modificacion)
            print("Se ha cambiado el Nombre Exitosamente")
        elif Modificar == 2:
            NuevoEfecto = input("Ingrese el nuevo efecto de su estado: ")
            Modificacion = f"""UPDATE estado 
            set efecto = '{NuevoEfecto}' 
            WHERE  id = {EstadoElegido}"""
            self.cursor.execute(Modificacion)
            print("Se ha cambiado el efecto Exitosamente")
        elif Modificar == 3:
            NuevoNombre = input("Ingrese el nuevo nombre de su estado: ")
            NuevoEfecto = input("Ingrese el nuevo efecto de su estado: ")
            Modificacion = f"""UPDATE estado
            set nombre = '{NuevoNombre}', efecto = '{NuevoEfecto}' 
            WHERE  id = {EstadoElegido}"""
            self.cursor.execute(Modificacion)
            print("Se han cambiado los valores Exitosamente")
    

    def EliminarEstado(self):
        ListadoEstados = self.ListarEstado()
        Eleccion = int(input("Seleccione el estado (numero) que desea eliminar: ")) -1
        Estado = int(ListadoEstados[Eleccion][0])
        if Estado == 1 or Estado == 2:
            print("Los estados de vivo y muerto no pueden ser eliminados")
            return
        estadoenuso = f"""SELECT personaje.fk_id_estado 
        FROM personaje 
        WHERE fk_id_estado = {Estado}
        """
        self.cursor.execute(estadoenuso)
        Seusa = self.cursor.fetchone()
        if (bool(Seusa)):
            print("El estado que desea eliminar se encuentra en uso")
            return
        else:
            BorrarEstado= f"""DELETE FROM estado WHERE id = {Estado}"""
            self.cursor.execute(BorrarEstado)
            print("Se ha eliminado el estado exitosamente")

    def crearPartida(self):
        NombrePartida = input("Inserte el nombre de la nueva partida que desea crear: ")
        while NombrePartida == '':
            NombrePartida = input("El nombre de la partida no es valido Por favor ingreselo nuevamente")    
        QueryCrearPartida= f"""INSERT INTO partida (nombre)
        VALUES ('{NombrePartida}')"""
        self.cursor.execute(QueryCrearPartida)
        print("La partida ha sido creada exitosamente")

    def AgregarEquipamiento(self):
        Nombre = input("Ingrese el nombre de su nueva arma: ")
        Tipo = ''
        Eleccion = int(input("""¿Qué tipo de equipamiento es?
                            1.-Arma
                            2.-Armadura
                            """))
        if Eleccion == 1:
            Tipo = "Arma"
        elif Eleccion == 2:
            Tipo = "Armadura"
        
        NuevoEquipamiento = f"""INSERT INTO equipamiento(nombre, tipo)
        values('{Nombre}','{Tipo}')
        """
        self.cursor.execute(NuevoEquipamiento)
        
    def EditarEquipamiento(self):
        ListadoEquipamientos = self.ListarEquipamiento()
        if bool(ListadoEquipamientos):
            Eleccion = int(input("Seleccione el equipamiento (numero) que desea modificar: ")) -1
            EquipamientoElegido = ListadoEquipamientos[Eleccion]
            print(f"Se cambiara el nombre del equipamiento {EquipamientoElegido[0]}")
            NuevoNombre = input("Ingrese el nuevo nombre del equipamiento: ")
            Modificacion = f"""UPDATE equipamiento 
                set nombre = '{NuevoNombre}' 
                WHERE  id = {EquipamientoElegido[1]}"""
            self.cursor.execute(Modificacion)
            print("Se ha cambiado el Nombre Exitosamente")
        else:
            return
        
    def EliminarEquipamiento(self):
        ListadoEquipamiento = self.ListarEquipamiento()
        if bool(ListadoEquipamiento):           
            Eleccion = int(input("Seleccione el equipamiento (numero) que desea eliminar: ")) -1
            equipamiento = int(ListadoEquipamiento[Eleccion][1])
            equipamientoeuso = f"""SELECT equipamiento_personaje.fk_id_equipamiento 
            FROM equipamiento_personaje 
            WHERE fk_id_equipamiento = {equipamiento}
            """
            self.cursor.execute(equipamientoeuso)
            Seusa = self.cursor.fetchone()
            if (bool(Seusa)):
                print("El equipamiento que desea eliminar se encuentra en uso")
            else:
                BorrarEquipamiento= f"""DELETE FROM equipamiento WHERE id = {equipamiento}"""
                self.cursor.execute(BorrarEquipamiento)
                print("Se ha eliminado el equipamiento exitosamente")
        else:
            return
    
    def AgregarPoder(self):
        Nombre = input("Ingrese el nombre del nuevo poder ")
        Descripción = input("Ingrese el detalle del poder ")
        razas = self.ListarRazas()
        Eleccion = int(input("Seleccione la raza (numero) a la que pertenecera el nuevo poder: "))
        Raza = razas[Eleccion][0]
        NuevoPoder = f"""INSERT INTO poder (nombre, descripcion, fk_id_raza) 
        values('{Nombre}', '{Descripción}', {Raza})"""
        self.cursor.execute(NuevoPoder)
    
    def EditarPoder(self):
        ListadoPoder = self.ListarPoderes()
        if bool(ListadoPoder):
            Elección = int(input("Seleccione (Numero) que poder desea modificar: ")) - 1
            PoderElegido = ListadoPoder[Elección]
            print(f"""Se ha seleccionado el {PoderElegido[1]} de la Raza {PoderElegido[3]} \nla cual posee la siguiente descripción:\n{PoderElegido[2]}""")
            Modificar = int(input("""¿Qué desea modificar del poder en cuestion
                1.- Su nombre
                2.- Su Descripción
                3.- Ambas
                """))
            
            if Modificar == 1:
                NuevoNombre = input("Ingrese el nuevo nombre de su poder: ")
                Modificacion = f"""UPDATE poder 
                set nombre = '{NuevoNombre}' 
                WHERE  id = {PoderElegido[0]}"""
                self.cursor.execute(Modificacion)
                print("Se ha cambiado el Nombre Exitosamente")
                
            elif Modificar == 2:
                NuevaDescripcion = input("Ingrese la nueva descripcion de su poder: ")
                Modificacion = f"""UPDATE poder 
                set descripcion = '{NuevaDescripcion}' 
                WHERE  id = {PoderElegido[0]}"""
                self.cursor.execute(Modificacion)
                print("Se ha cambiado la descripcion Exitosamente")
                
            elif Modificar == 3:
                NuevoNombre = input("Ingrese el nuevo nombre de su poder: ")
                NuevaDescripcion = input("Ingrese la nueva descripcion de su poder: ")
                Modificacion = f"""UPDATE poder
                set nombre = '{NuevoNombre}', descripcion = '{NuevaDescripcion}' 
                WHERE  id = {PoderElegido[0]}"""
                self.cursor.execute(Modificacion)
                print("Se han cambiado los valores Exitosamente")
        else:
            return
        
    def EliminarPoder(self):
        ListadoPoder = self.ListarPoderes()
        if bool(ListadoPoder):
            Elección = int(input("Seleccione (Numero) que poder desea eliminar: ")) - 1
            PoderElegido = ListadoPoder[Elección]
            PoderEnuso = f"""Select poder_personaje.fk_id_poder 
            FROM poder_personaje
            WHERE poder_personaje.fk_id_poder = {PoderElegido[0]}
            """
            self.cursor.execute(PoderEnuso)
            datos = self.cursor.fetchone()
            if bool(datos):
                print("El poder que desea eliminar se esta utilizando")
                return
            else:
                BorrarPoder= f"""DELETE FROM poder 
                WHERE poder.id = {PoderElegido[0]}"""
                self.cursor.execute(BorrarPoder)
                print("Se ha eliminado el poder exitosamente")
        else:
            return
        
    def AgregarHabilidad(self):
        Nombre = input("Ingrese el nombre de la nueva habilidad ")
        Descripción = input("Ingrese el detalle de la raza ")
        razas =  self.ListarRazas()
        Eleccion = int(input("Seleccione la raza (numero) a la que pertenecera el nuevo poder: "))
        Raza = razas[Eleccion][0]
        print(Raza)
        NuevaHabilidad = f"""INSERT INTO habilidad (nombre, descripcion, fk_id_raza) 
        values('{Nombre}', '{Descripción}', {Raza})"""
        self.cursor.execute(NuevaHabilidad)
    
    def EditarHabilidad(self):
        ListadoHabilidades = self.ListarHabilidades()
        if bool(ListadoHabilidades):
            Elección = int(input("Seleccione (Numero) que habilidad desea modificar: ")) - 1
            HabilidadElegida = ListadoHabilidades[Elección]
            print(f"""Se ha seleccionado la habilidad {HabilidadElegida[1]} de la Raza {HabilidadElegida[3]} \nla cual posee la siguiente descripción:\n{HabilidadElegida[2]}""")
            Modificar = int(input("""¿Qué desea modificar de la habilidad en cuestion
                1.- Su nombre
                2.- Su Descripción
                3.- Ambas
                """))
            if Modificar == 1:
                NuevoNombre = input("Ingrese el nuevo nombre de su habilidad: ")
                Modificacion = f"""UPDATE habilidad 
                set nombre = '{NuevoNombre}' 
                WHERE  id = {HabilidadElegida[0]}"""
                self.cursor.execute(Modificacion)
            elif Modificar == 2:
                NuevaDescripcion = input("Ingrese la nueva descripcion de su habilidad: ")
                Modificacion = f"""UPDATE habilidad 
                set descripcion = '{NuevaDescripcion}' 
                WHERE  id = {HabilidadElegida[0]}"""
                self.cursor.execute(Modificacion)
            elif Modificar == 3:
                NuevoNombre = input("Ingrese el nuevo nombre de su habilidad: ")
                NuevaDescripcion = input("Ingrese la nueva descripcion de su habilidad: ")
                Modificacion = f"""UPDATE habilidad
                set nombre = '{NuevoNombre}', descripcion = '{NuevaDescripcion}' 
                WHERE  id = {HabilidadElegida[0]}"""
                self.cursor.execute(Modificacion)
            print("Se han modificado la habilidad exitosamente")
        else:
            return
        
    def EliminarHabilidad(self):
        ListadoHabilidad = self.ListarHabilidades()
        if bool(ListadoHabilidad): 
            Elección = int(input("Seleccione (Numero) que habilidad desea eliminar: ")) - 1
            HabilidadElegida = ListadoHabilidad[Elección]
            HabilidadenUso = f"""Select habilidad_personaje.fk_id_habilidad 
            FROM habilidad_personaje
            WHERE habilidad_personaje.fk_id_habilidad = {HabilidadElegida[0]}
            """
            self.cursor.execute(HabilidadenUso)
            datos = self.cursor.fetchone()
            if bool(datos):
                print("La habilidad que desea eliminar se esta utilizando")
                return
            else:
                BorrarHabilidad= f"""DELETE FROM habilidad 
                WHERE habilidad.id = {HabilidadElegida[0]}"""
                self.cursor.execute(BorrarHabilidad)
                print("Se ha eliminado la habilidad exitosamente")
        else:
            return
    
    def AgregarRaza(self):
        Nombre = input("Ingrese el nombre de su nueva Raza: ")
        InsertarRaza= f"""INSERT INTO raza(nombre)
        values('{Nombre}')"""
        self.cursor.execute(InsertarRaza)
        print("Se ha creado la raza correctamente")
    
    def EliminarRaza(self):
        ListadoRaza = self.ListarRazas()
        if ListadoRaza == False:
            return
        Elección = int(input("Seleccione (Numero) que raza desea eliminar: ")) - 1
        RazaElegida = ListadoRaza[Elección]
        RazaenUso = f"""Select personaje.fk_id_raza 
        FROM personaje
        WHERE personaje.fk_id_raza = {RazaElegida[1]}
        """
        self.cursor.execute(RazaenUso)
        datos = self.cursor.fetchone()
        if bool(datos):
            print("La raza que desea eliminar se encuentra en uso")
        else:
            BorrarRaza= f"""DELETE FROM raza 
            WHERE raza.id = {RazaElegida[1]}"""
            self.cursor.execute(BorrarRaza)
            print("Se ha eliminado la raza exitosamente")
        
    def VerPersonajesPartida(self):
        PartidasExistentes = self.ListarPartidas()
        Eleccion = int(input("Seleccione de que partida (Numero) Desea ver los personajes: ")) -1
        PartidaSeleccionada = int(PartidasExistentes[Eleccion][0])
        Personajes = f"""select personaje.id, personaje.nombre, personaje.nivel, raza.nombre, raza.id, estado.nombre
        from personaje
        inner join personaje_partida ON personaje_partida.fk_id_personaje = personaje.id
        inner join raza ON personaje.fk_id_raza = raza.id
        inner join estado ON personaje.fk_id_estado = estado.id
        where personaje_partida.fk_id_partida = {PartidaSeleccionada}
        ORDER BY personaje.id      
        """
        self.cursor.execute(Personajes)
        PersonajesEnPartida = self.cursor.fetchall()
        if bool(PersonajesEnPartida):
            print("Los personajes asociados esta partida son: ")
            for indice, i in enumerate(PersonajesEnPartida):
                print(f"{indice+1}.- {i[1]}  Nivel: {i[2]} - {i[3]}")
            return PersonajesEnPartida
        else:
            print("No hay personajes asociados a esta partida")
            return False
         
    def ListarPoderesPersonaje(self):
        PersonajesEnPartida = self.VerPersonajesPartida()
        if PersonajesEnPartida == False:
            return
        EleccionPersonaje = int(input("¿De que personaje desea ver los poderes?")) -1
        SeleccionPersonaje = int(PersonajesEnPartida[EleccionPersonaje][0])
        QueryPoderes = f"""select poder_personaje.id, poder.id, poder.nombre
        from poder_personaje
        inner join poder on poder.id = poder_personaje.fk_id_poder
        where poder_personaje.fk_id_personaje = {SeleccionPersonaje}
        order by poder_personaje.id
        """
        self.cursor.execute(QueryPoderes)
        ListaPoderesPersonaje = self.cursor.fetchall() 
        if bool(ListaPoderesPersonaje):
            print("Estos son los poderes asociados al personaje: ")
            for indice,i in enumerate(ListaPoderesPersonaje):
                print(f'{indice+1}.-  {i[2]}')
            return ListaPoderesPersonaje, SeleccionPersonaje
        else:
            print("Este personaje no tiene poderes asociados")
            return bool(PersonajesEnPartida), SeleccionPersonaje
           
    def ListarHabilidadesPersonaje(self):
        PersonajesEnPartida = self.VerPersonajesPartida()
        if PersonajesEnPartida == False:
            return
        EleccionPersonaje = int(input("¿De que personaje desea ver las habilidades?")) - 1
        SeleccionPersonaje = int(PersonajesEnPartida[EleccionPersonaje][0])
        QueryHabilidades = f"""select habilidad_personaje.id, habilidad.id, habilidad.nombre
        from habilidad_personaje
        inner join habilidad on habilidad.id = habilidad_personaje.fk_id_habilidad
        where habilidad_personaje.fk_id_personaje = {SeleccionPersonaje}
        ORDER BY habilidad_personaje.id
        """
        self.cursor.execute(QueryHabilidades)
        ListaHabilidadesPersonaje = self.cursor.fetchall() 
        if bool(ListaHabilidadesPersonaje):
            print("Estos son las habilidades asociadas al personaje: ")
            for indice,i in enumerate(ListaHabilidadesPersonaje):
                print(f'{indice+1}.-  {i[2]}')
            return ListaHabilidadesPersonaje, SeleccionPersonaje
        else:
            print("Este personaje no tiene habilidades asociadas")
            return bool(PersonajesEnPartida), SeleccionPersonaje
    
    def ListarEquipamientosPersonaje(self):
        PersonajesEnPartida = self.VerPersonajesPartida()
        if PersonajesEnPartida == False:
            return 
        EleccionPersonaje = int(input("¿De que personaje desea ver el equipamiento? ")) -1
        SeleccionPersonaje = int(PersonajesEnPartida[EleccionPersonaje][0])
        QueryEquipamientoPersonaje = f"""select equipamiento_personaje.id, equipamiento.id, equipamiento.nombre
        from equipamiento_personaje
        inner join equipamiento on equipamiento.id = equipamiento_personaje.fk_id_equipamiento
        where equipamiento_personaje.fk_id_personaje = {SeleccionPersonaje}
        order by equipamiento_personaje.id
        """
        self.cursor.execute(QueryEquipamientoPersonaje)
        ListaEquipamientosPersonaje = self.cursor.fetchall()
        HayEquipamientosAsociados = bool(ListaEquipamientosPersonaje) 
        if HayEquipamientosAsociados:
            print("Estos son los equipamientos asociados al personaje: ")
            for indice,i in enumerate(ListaEquipamientosPersonaje):
                print(f'{indice+1}.-  {i[2]}')
            return ListaEquipamientosPersonaje
        else:
            print("Este personaje no tiene equipamientos asociados")

    def AgregarHabilidadApersonaje(self):
        Personajes = self.VerPersonajesPartida()
        EleccionPersonaje = int(input("Elija (Numero) a que personaje desea agregarle un equipamiento: ")) -1
        SeleccionPersonaje = Personajes[EleccionPersonaje]
        IdSeleccion = Personajes[EleccionPersonaje][0]
        Raza = SeleccionPersonaje[4]
        QueryCantidadHabilidades = f"""SELECT * 
        FROM habilidad_personaje
        WHERE habilidad_personaje.fk_id_personaje = {IdSeleccion}
        """
        self.cursor.execute(QueryCantidadHabilidades)
        Cantidad = len(self.cursor.fetchall())
        print(Cantidad)
        if Cantidad >= 8:
            print("El personaje seleccionado ha alcanzado su capacidad maxima de habilidades permitidas (8)")
            return
        print("Estas son las habilidades disponibles para equipar: ")
        Habilidades = self.ListarHabilidades(Raza)
        EleccionHabilidad = int(input("Elija (Numero) de habilidad que desea darle al personaje : ")) -1
        SeleccionHabilidad = Habilidades[EleccionHabilidad][0]
        AgregarHabilidadAPjQuery = f"""INSERT INTO habilidad_personaje (fk_id_habilidad, fk_id_personaje)
        VALUES ({SeleccionHabilidad}, {IdSeleccion})
        """
        self.cursor.execute(AgregarHabilidadAPjQuery)
        print("Se ha asignado la habilidad al personaje exitosamente")
    
    def CambiarHabilidadPersonaje(self):
        pass
 
    def eliminarhabilidadPersonaje(self):
        pass
    
    def AgregarPoderApersonaje(self):
        Personajes = self.VerPersonajesPartida()
        EleccionPersonaje = int(input("Elija (Numero) a que personaje desea agregarle un equipamiento: ")) -1
        SeleccionPersonaje = Personajes[EleccionPersonaje]
        idSeleccion = SeleccionPersonaje[0]
        Raza = SeleccionPersonaje[4]
        QueryCantidadPoderes = f"""SELECT * 
        FROM poder_personaje
        WHERE poder_personaje.fk_id_personaje = {idSeleccion}
        """
        self.cursor.execute(QueryCantidadPoderes)
        Cantidad = len(self.cursor.fetchall())
        print(Cantidad)
        if Cantidad >= 4:
            print("El personaje seleccionado ha alcanzado su capacidad maxima de poderes permitidos (4)")
            return
        print("Estos son los poderes disponibles para equipar: ")
        Poderes = self.ListarPoderes(Raza)
        EleccionPoder = int(input("Elija (Numero) de habilidad que desea darle al personaje : ")) -1
        SeleccionPoder = Poderes[EleccionPoder][0]
        AgregarHabilidadAPjQuery = f"""INSERT INTO habilidad_personaje (fk_id_habilidad, fk_id_personaje)
        VALUES ({SeleccionPoder}, {idSeleccion})
        """
        self.cursor.execute(AgregarHabilidadAPjQuery)
        print("Se ha asignado el poder al personaje exitosamente")
    
    def CambiarPoderPersonaje(self):
        pass
    
    def eliminarPoderPersonaje(self):
        pass
    
    def AgregarEquipamientoPersonaje(self):
        Personajes = self.VerPersonajesPartida()
        EleccionPersonaje = int(input("Elija (Numero) a que personaje desea agregarle un equipamiento: ")) -1
        SeleccionPersonaje = Personajes[EleccionPersonaje][0]
        QueryCantidadEquipamientos = f"""SELECT * 
        FROM equipamiento_personaje
        WHERE equipamiento_personaje.fk_id_personaje = {SeleccionPersonaje}
        """
        self.cursor.execute(QueryCantidadEquipamientos)
        Cantidad = len(self.cursor.fetchall())
        print(Cantidad)
        if Cantidad >= 8:
            print("El personaje seleccionado ha alcanzado su capacidad maxima de equipamientos permitidos (8)")
            return
        print("Estos son los equipamientos disponibles para equipar: ")
        Equipamientos = self.ListarEquipamiento()
        EleccionEquipamiento = int(input("Elija (Numero) de equipamiento que desea ponerle al personaje : ")) -1
        SeleccionEquipamiento = Equipamientos[EleccionEquipamiento][0]
        AgregarEquipamientoaPJQuery = f"""INSERT INTO equipamiento_personaje (fk_id_equipamiento, fk_id_personaje)
        VALUES ({SeleccionEquipamiento}, {SeleccionPersonaje})
        """
        self.cursor.execute(AgregarEquipamientoaPJQuery)
        print("Se ha equipado al personaje exitosamente")
        
    def EliminarEquipamientoPersonaje(self):
        Equipamientos = self.ListarEquipamientosPersonaje()
        if not bool(Equipamientos):
            return
        EleccionEquipamiento = int(input("Elija (Numero) cual de los equipamientos desea eliminar : ")) - 1
        SeleccionEquipamiento = Equipamientos[EleccionEquipamiento]
        while EleccionEquipamiento == 1:
            EleccionEquipamiento = int(input("No se puede eliminar el equipamiento puesto por el jugador por favor seleccione otro: ")) -1
        EliminacionEquipamientoQuery = f"""DELETE 
        FROM equipamiento_personaje
        WHERE id = {SeleccionEquipamiento[0]}
        """
        self.cursor.execute(EliminacionEquipamientoQuery)
        print("Se ha eliminado el equipamiento correctamente")
            
    def cambiarEstadoPersonaje(self):
        Personajes = self.VerPersonajesPartida()
        EleccionPersonaje = int(input("Elija (Numero) A que personaje desea de cambiarle el estado: ")) -1
        PersonajeSeleccionado = Personajes[EleccionPersonaje]
        print(f"Estado actual del personaje seleccionado: {PersonajeSeleccionado[5]}")
        Estados = self.ListarEstado()
        EleccionEstado = int(input("Elija (Numero) el nuevo estado que quiere darle al personaje : ")) -1
        EstadoSeleccionado = Estados[EleccionEstado][0]
        CambiarEstadoPJQuery = f"""UPDATE personaje
        set fk_id_estado = {EstadoSeleccionado}
        where id = {PersonajeSeleccionado[0]}
        """
        self.cursor.execute(CambiarEstadoPJQuery)
        print("Estado Cambiado exitosamente")
    
    def SubirNiveldePersonaje(self):
        Personajes = self.VerPersonajesPartida()
        EleccionPersonaje = int(input("Elija (Numero) A que personaje desea de incrementarle el nivel: ")) -1
        PersonajeSeleccionado = Personajes[EleccionPersonaje]
        Nivel = int(input("¿Cuantos niveles desea incrementarle al personaje?"))
        while Nivel < 0:
            Nivel = int(input("No se pueden disminuir niveles por favor ingrese un valor valido: "))
        NuevoNivel = PersonajeSeleccionado[2] + Nivel
        IncrementoDeNivelQuery = f"""UPDATE personaje
            set nivel = '{NuevoNivel}' 
            WHERE  id = {PersonajeSeleccionado[0]}"""
        self.cursor.execute(IncrementoDeNivelQuery)
        print("Se ha aumentado el nivel correctamente")

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