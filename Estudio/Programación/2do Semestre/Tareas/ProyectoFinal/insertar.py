from tkinter import *
from tkinter.ttk import *
from libro import Libro
from socio import Socio


class InsetarVentana():
    def __init__(self, ventana2):
        ventana = ventana2
        ventana.geometry("1000x500")
        titulo = Label(ventana, text="Ingresar Libro")
        titulo.pack()
        space2 = Label(ventana, text="")
        space2.pack()

        tituloLabel = Label(ventana,text="Titulo")
        tituloEntry = Entry(ventana, )
        tituloLabel.pack()
        tituloEntry.pack()

        disponibleLabel = Label(ventana, text="Disponible")
        disponibleEntry = Entry(ventana, )
        disponibleLabel.pack()
        disponibleEntry.pack()

        space4= Label(ventana,text="")
        space4.pack()

        def ingresarLibro():
            libro = Libro()
            libro.titulo = tituloEntry.get()
            libro.disponible = disponibleEntry.get()

            libro.insertar()

        buttonEnterLibro = Button(ventana, text="Ingresar Libro",command=ingresarLibro)
        buttonEnterLibro.pack()
 
        space59= Label(ventana,text="")
        space59.pack()

        titulo = Label(ventana, text="Ingresar Socio")
        titulo.pack()
        space2 = Label(ventana, text="")
        space2.pack()

        nombreLabel = Label(ventana,text="Nombre")
        nombreEntry = Entry(ventana, )
        nombreLabel.pack()
        nombreEntry.pack()

        apellidoLabel = Label(ventana, text="Apellido")
        apellidoEntry = Entry(ventana, )
        apellidoLabel.pack()
        apellidoEntry.pack()

        space4= Label(ventana,text="")
        space4.pack()

        def ingresarSocio():
            socio = Socio()
            socio.nombre = nombreEntry.get()
            socio.apellido = apellidoEntry.get()

            socio.insertar()

        buttonEnterSocio = Button(ventana, text="Ingresar Socio",command=ingresarSocio)
        buttonEnterSocio.pack()

