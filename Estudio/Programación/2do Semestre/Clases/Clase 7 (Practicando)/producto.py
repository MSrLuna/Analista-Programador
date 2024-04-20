from conexion import conexion, hoja

class Producto:
    def __init__(self):
        self.id = None
        self.nombre =None
        self.precio = None
        self.stock = None
    
    def insertar(self):
        sql = "insert into producto(nombre, precio, stock) values (:1, :2, :3)"

        hoja.execute(sql, (self.nombre, self.precio, self.stock))
        conexion.commit()
