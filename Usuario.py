from Database import conexion
class Usuario:
    cursor = conexion.cursor()
    def __init__(self, nombre, rol):
        self.nombre = nombre
        self.rol = rol
        
    def ListarHabilidades(self, id=False):
        if bool(id):
            query = f"""SELECT habilidad.nombre, habilidad.descripcion, raza.nombre, habilidad.id 
            from habilidad 
            LEFT JOIN raza ON habilidad.fk_id_raza=raza.id 
            WHERE fk_id_raza = {id}
            ORDER BY id"""
        else:
            query = f"""SELECT habilidad.nombre, habilidad.descripcion, raza.nombre, habilidad.id 
            from habilidad 
            LEFT JOIN raza ON habilidad.fk_id_raza=raza.id 
            ORDER BY id"""
        self.cursor.execute(query)
        listaHabilidades = self.cursor.fetchall()
        if bool(listaHabilidades):
            print("    Habilidad - Descripcion - Raza")
            for indice, i in enumerate(listaHabilidades):
                print(f"{indice+1}.- {i[0]} - {i[1]} - {i[2]}")
            return listaHabilidades
        else:
            print("No hay habilidades en el sistema")
            return False

    def ListarPoderes(self, id=False):
        if bool(id):
            query = f"""SELECT poder.nombre, poder.descripcion, raza.nombre, poder.id 
            from poder 
            LEFT JOIN raza ON poder.fk_id_raza=raza.id
            WHERE fk_id_raza = {id}
            ORDER BY id
            """
        else:
            query = f"""SELECT poder.nombre, poder.descripcion, raza.nombre, poder.id 
            from poder 
            LEFT JOIN raza ON poder.fk_id_raza=raza.id
            ORDER BY id
            """
        self.cursor.execute(query)
        listaPoderes = self.cursor.fetchall()
        if bool(listaPoderes):
            print("    Poder - Descripcion - Raza")
            for indice, i in enumerate(listaPoderes):
                print(f"{indice+1}.- {i[0]} - {i[1]} - {i[2]}")
            return listaPoderes
        else:
            print("No hay poderes en el sistema")
            return False

    def ListarEquipamiento(self):
        query = f"""SELECT equipamiento.nombre, equipamiento.id 
        from equipamiento 
        ORDER BY id"""
        self.cursor.execute(query)
        listaEquipamiento = self.cursor.fetchall()
        if bool(listaEquipamiento):       
            for indice, i in enumerate(listaEquipamiento) :
                print(f"{indice+1}.- {i[0]} ")
            return listaEquipamiento
        else: 
            print("No hay equipamientos en el sistema")
            return False

    def ListarEstado(self):
        estados = f"""SELECT estado.nombre, estado.id, estado.efecto 
        from estado 
        ORDER BY id"""
        self.cursor.execute(estados)
        listaEstados = self.cursor.fetchall()
        for indice, i in enumerate(listaEstados):
            print(f"{indice+1}.- {i[0]}")
        return listaEstados

    def ListarRazas(self):
        query = f"""SELECT raza.nombre, raza.id 
        from raza 
        ORDER BY id"""
        self.cursor.execute(query)
        listaRazas = self.cursor.fetchall()
        if bool(listaRazas):
            for indice, i in enumerate(listaRazas):
                print(f"{indice+1}.- {i[0]} ")
            return listaRazas
        else:
            print("No hay razas disponibles")
            return False

    def ListarPartidas(self):
        query = f"""SELECT partida.nombre, partida.id 
        from partida 
        ORDER BY id"""
        self.cursor.execute(query)
        listaPartidas = self.cursor.fetchall()
        if bool(listaPartidas):
            for indice, i in enumerate(listaPartidas):
                print(f"{indice+1}.- {i[0]} ")
            return listaPartidas
        else:
            print("No hay habilidades en el sistema")
            return
