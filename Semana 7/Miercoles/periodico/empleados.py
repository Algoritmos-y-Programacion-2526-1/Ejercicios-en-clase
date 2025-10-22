class Empleado:
    def __init__(self, nombre, cedula):
        self.nombre = nombre
        self.cédula = cedula

class Jefe(Empleado):
    def __init__(self, nombre, cedula):
        super().__init__(nombre, cedula)

    def supervisar(self):
        pass

    def publicar(self, articulos):
        pass


class Escritor(Empleado):
    def __init__(self, nombre, cedula):
        super().__init__(nombre, cedula)

    def escribir_articulo(self):
        return None