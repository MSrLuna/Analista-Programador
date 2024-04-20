from tkinter import *
from crearAlumno import VentanaCrearAlumno
from listaAlumnos import VentanaListarAlumnos

from listaAlumnos import VentanaListarAlumnos

class VentanaMenu:

    def __init__(self, ventana):
        ventana.geometry("500x500")
        ventana.title("Menú de opciones")
        fuentes = ("Segoe UI", 18, "bold")

        def listarAlumnos():
            vListarAlumnos = Toplevel()
            VentanaListarAlumnos(vListarAlumnos)

        def crearAlumno():
            vCrearAlumno = Toplevel()
            VentanaCrearAlumno(vCrearAlumno)

        btnListar = Button(ventana, text="Listado Alumnos", bg="blue", fg="white", font=fuentes, command=listarAlumnos)
        btnListar.pack()
        btnCrear = Button(ventana, text="Crear Alumno", bg="green", fg="white", font=fuentes, command=crearAlumno)
        btnCrear.pack()