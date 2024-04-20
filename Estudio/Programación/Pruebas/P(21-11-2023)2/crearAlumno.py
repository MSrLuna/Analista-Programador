from tkinter import *
from alumno import Alumno

class VentanaCrearAlumno:

    def __init__(self, ventana):
        ventana.geometry("500x500")
        ventana.title("Ingresar Alumno")
        fuentes = ("Segoe UI", 18, "bold")

        lblNombre = Label(ventana, font=fuentes, text="NOMBRE")
        lblNombre.pack()
        txtNombre = Entry(ventana, font=fuentes)
        txtNombre.pack()

        lblApellido = Label(ventana, font=fuentes, text="APELLIDO")
        lblApellido.pack()
        txtApellido = Entry(ventana, font=fuentes)
        txtApellido.pack()

        lblPromedio = Label(ventana, font=fuentes, text="PROMEDIO")
        lblPromedio.pack()
        txtPromedio = Entry(ventana, font=fuentes)
        txtPromedio.pack()

        def insertar():
            a = Alumno()
            a.nombre = txtNombre.get()
            a.apellido=  txtApellido.get()
            a.promedio = txtPromedio.get()
            a.insertar()

        btnCrearA = Button(ventana, text="Crear Alumno", bg="green", fg="white", font=fuentes, command=insertar)
        btnCrearA.pack()