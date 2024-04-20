from conexion import conexion, hoja

class Producto:
    def __init__(self):
        self.id = None
        self.nombre = None
        self.precio = None
        self.stock = None
    
    def obtenerDatos(self):
        sql = "select * from producto"
        hoja.execute(sql)
        return hoja.fetchall()