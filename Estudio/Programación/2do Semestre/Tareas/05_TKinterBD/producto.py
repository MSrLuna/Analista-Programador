from conexion import conexion, hoja
# PASO 1: creo una clase con el mismo nonmbre de la tabla
class Producto:
    # PASO 2: creo el constructor
    def __init__(self):
        # PASO 3: creo tantos atributos como columnas hayan en la tabla de la BD
        self.id = None
        self.nombre = None
        self.precio = None
        self.stock = None
    
    def insertar(self):
        sql = "INSERT INTO producto (nombre, precio, stock) VALUES (:1, :2, :3)"
        # Para usar parámetros NUMERIC en una consulta a SQL, en el método execute()
        # vamos a poner justo después de nuestro SQL una coma y después una tupla
        # La tupla debe tener tantos valores como los números que pusiste en tu SQL
        # En este ejemplo, tenemos :1 :2 y :3.. por lo tanto, la tupla dentro de execute()
        # debe tener 3 valores.
        hoja.execute(sql, (self.nombre, self.precio, self.stock))
        conexion.commit()