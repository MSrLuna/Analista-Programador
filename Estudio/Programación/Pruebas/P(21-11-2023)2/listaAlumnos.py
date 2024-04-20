#Le informo que la lista no se ve debido a que hay algún error con la conexión con sqldeveloper que no me da permisos ni desde el mismo programa siquiera, pero el código en teoría está correcto.

from conexion import *
from tkinter import *
from tkinter.ttk import *
from alumno import Alumno
from modificar import VentanaModificarAlumno

class VentanaListarAlumnos:

    def __init__(self, ventana):
        ventana.geometry("500x500")
        ventana.title("Lista de alumnos")

        tabla = Treeview(ventana)
        tabla["columns"]=("ID", "NOMBRE", "APELLIDO", "PROMEDIO")

        tabla.column(column="#0", width=0)
        tabla.column(column="ID", width=50)
        tabla.column(column="NOMBRE", width=50)
        tabla.column(column="APELLIDO", width=50)
        tabla.column(column="PROMEDIO", width=50)

        tabla.heading(column="ID", text="ID")
        tabla.heading(column="NOMBRE", text="NOMBRE")
        tabla.heading(column="APELLIDO", text="APELLIDO")
        tabla.heading(column="PROMEDIO", text="PROMEDIO")

        a = Alumno()
        filas = a.ObtenerTodos()
        for tupla in filas:
            tabla.insert(parent="", index=END, values=tupla, iid=tupla[0])
        
        def onClick(event):
            iid = tabla.selection()[0]
            ventanaActualizar = Toplevel(ventana)
            VentanaModificarAlumno(ventanaActualizar, iid)
        tabla.bind("<ButtonRelease-1>", onClick)
        tabla.pack()