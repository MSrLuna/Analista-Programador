from conexion import hoja, conexion

class Producto:

    def __init__(self):
        self.id = None
        self.nombre = None
        self.precio = None
        self.stock = None
    
    def obtenerDatos(self):
        sql = "SELECT * FROM producto order by id"
        hoja.execute(sql)
        return hoja.fetchall()
   
    def insertar(self):
        sql = "INSERT INTO producto (nombre, precio, stock) VALUES (:1, :2, :3)"
        hoja.execute(sql, (self.nombre, self.precio, self.stock))
        conexion.commit()
    
    def ObtnerPorId(self, iid):
        sql = "SELECT id, nombre, precio, stock FROM producto WHERE id = :idP"
        hoja.execute(sql, idP = iid)
        return hoja.fetchone()
    
    def actualizar(self):
        sql = "UPDATE producto SET nombre = :nom, precio = :pre, stock = :sto WHERE id = :idP"
        hoja.execute(sql, nom=self.nombre, pre=self.precio, sto=self.stock, idP=self.id)
        conexion.commit()

    def eliminar(self):
        sql = "DELETE FROM producto WHERE id = :idP"
        hoja.execute(sql, idP=self.id)
        conexion.commit()
    
    def vender(self, CantidadVendida, ProductoVendido):
        sql = "UPDATE producto SET stock = stock - :cant WHERE id = :idP"
        hoja.execute(sql, cant=CantidadVendida, idp=ProductoVendido)
        conexion.commit()