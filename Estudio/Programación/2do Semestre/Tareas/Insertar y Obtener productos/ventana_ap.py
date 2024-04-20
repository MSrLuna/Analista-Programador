 from tkinter import *
from tkinter.ttk import *
from producto import Producto

class ActualizarP:
    def __init__(self, VentanaPadre):
        ventana = VentanaPadre
        ventana.geometry("360x300")
        ventana.title("Actualizar datos en la tabla 'Producto'")
        estiloFuentes = ("Tahoma", 18, "bold")

        labelNombre = Label(ventana, text="Nombre", font=estiloFuentes)
        labelNombre.pack()
        txtNombre = Entry(ventana, font=estiloFuentes)
        txtNombre.pack()

        labelPrecio = Label(ventana, text="Precio", font=estiloFuentes)
        labelPrecio.pack()
        txtPrecio = Entry(ventana, font=estiloFuentes)
        txtPrecio.pack()

        labelStock = Label(ventana, text="Stock", font=estiloFuentes)
        labelStock.pack()
        txtStock = Entry(ventana, font=estiloFuentes)
        txtStock.pack()

        def insertarProducto():

            p = Producto()
            p.nombre = txtNombre.get()
            p.precio=  txtPrecio.get()
            p.stock = txtStock.get()

        btnActualizar = Button(ventana, text="Actualizar", font=estiloFuentes,
                            bg="blue", fg="white", command=insertarProducto)
        btnActualizar.pack()