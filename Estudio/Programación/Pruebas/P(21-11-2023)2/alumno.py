from conexion import *

class Alumno:
    def __init__(self):
        self.id = None
        self.nombre = None
        self.apellido = None
        self.promedio = None

    def ObtenerTodos(self):
        sql = "SELECT * FROM alumno order by id"
        hoja.execute(sql)
        return hoja.fetchall()

    def ObtenerPorId(self, iid):
        sql = "SELECT id, nombre, apellido, promedio FROM alumno WHERE id = :idP"
        hoja.execute(sql, idP = iid)
        return hoja.fetchone()

    def insertar(self):
        sql = "INSERT INTO alumno (nombre, apellido, promedio) VALUES (:1, :2, :3)"
        hoja.execute(sql, (self.nombre, self.apellido, self.promedio))
        conexion.commit()

    def actualizar(self):
        sql = "UPDATE alumno SET nombre = :nom, apellido = :ape, promedio = :prom WHERE id = :idP"
        hoja.execute(sql, nom=self.nombre, ape=self.apellido, prom=self.promedio, idP=self.id)
        conexion.commit()

    def eliminar(self):
        sql = "DELETE FROM alumno WHERE id = :idP"
        hoja.execute(sql, idP=self.id)
        conexion.commit()