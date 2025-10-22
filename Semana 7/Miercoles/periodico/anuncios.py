class AnuncioComercial:
    def __init__(self, nombre, cedula, seccion, titulo, cuerpo):
        self.nombre = nombre
        self.cedula = cedula
        self.seccion = seccion
        self.titulo = titulo
        self.cuerpo = cuerpo

class AnuncioClasificado:
    def __init__(self, precio, fecha, cantidad, tipo):
        self.precio = precio
        self.fecha_de_publicación = fecha
        self.cantidad_de_dias = cantidad
        self.tipo_de_articulo = tipo

class AnuncioClasicadoVehiculo(AnuncioClasificado):
    def __init__(self, precio, fecha, cantidad, marca, modelo, año, color, km):
        super().__init__(precio, fecha, cantidad, "Vehiculo")
        self.marca = marca
        self.modelo = modelo
        self.año = año
        self.color = color
        self.km = km

class AnuncioClasicadoVivienda(AnuncioClasificado):
    def __init__(self, precio, fecha, cantidad, m2, cuartos, baños, puestos, acepta):
        super().__init__(precio, fecha, cantidad, "Vivienda")
        self.m2 = m2
        self.cuartos = cuartos
        self.baños = baños
        self.puestos_de_estacionamientos = puestos
        self.acepta_política_habitacional = acepta