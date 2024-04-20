from conexion import conexion, hoja

class Socio:
    def __init__(self):
        self.id = None
        self.nombre = None
        self.apellido = None
    
    def insertar(self):
        sql = "INSERT INTO socio (nombre, apellido) VALUES (:nom, :ape)"
        hoja.execute (sql, nom=self.nombre, ape=self.apellido)
        conexion.commit()