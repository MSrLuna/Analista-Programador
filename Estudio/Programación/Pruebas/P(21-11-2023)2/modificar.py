#Decidí poner el borrar alumno por aquí junto con actualizar ya que se me hacía más fácil y también porque ya lo había hecho así en casa.

from tkinter import *
from alumno import Alumno

class VentanaModificarAlumno:
    def __init__(self, ventana, iid):
        ventana.geometry("500x500")
        ventana.title("Modificación")
        fuentes = ("Segoe UI", 18, "bold")

        a = Alumno()
        tuplaResultado = a.ObtenerPorId(iid)
        a.id = iid
        a.nombre = tuplaResultado[1]
        a.apellido = tuplaResultado[2]
        a.promedio = tuplaResultado[3]
        
        lblNombre = Label(ventana, text="Nombre",font=fuentes)
        lblNombre.pack()
        txtNombre = Entry(ventana, font=fuentes)
        txtNombre.insert(0, a.nombre)
        txtNombre.pack()

        lblApellido = Label(ventana, text="Apellido",font=fuentes)
        lblApellido.pack()
        txtApellido = Entry(ventana, font=fuentes)
        txtApellido.insert(0, a.apellido)
        txtApellido.pack()

        lblPromedio = Label(ventana, text="Promedio", font=fuentes)
        lblPromedio.pack()
        txtPromedio = Entry(ventana, font=fuentes)
        txtPromedio.insert(0, a.promedio)
        txtPromedio.pack()

        def actualizar():
            a = Alumno()
            a.id = iid
            a.nombre = txtNombre.get()
            a.apellido =  txtApellido.get()
            a.promedio = txtPromedio.get()
            a.actualizar()

        btnActualizar = Button(ventana, text="Actualizar", bg="green", fg="white", command=actualizar)
        btnActualizar.pack()

        def eliminarProducto():
            a = Alumno()
            a.id = iid
            a.eliminar()
        
        btnEliminar = Button(ventana, text="Eliminar",
                            bg="red", fg="white", command=eliminarProducto)
        btnEliminar.pack()