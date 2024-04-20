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
        return hoja.fetchall()
   
    def insertar(self):
        sql = "INSERT INTO producto (nombre, precio, stock) VALUES (:1, :2, :3)"
        hoja.execute(sql, (self.nombre, self.precio, self.stock))
        conexion.commit()