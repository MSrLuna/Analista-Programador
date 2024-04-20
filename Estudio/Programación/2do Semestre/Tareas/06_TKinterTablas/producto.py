from conexion import hoja, conexion

class Producto:

    def __init__(self):
        self.id = None
        self.nombre = None
        self.precio = None
        self.stock = None
    
    def obtenerDatos(self):
        sql = "SELECT * FROM producto"
        hoja.execute(sql)
        # Devolvemos la lista de tuplas de la BD
        return hoja.fetchall()