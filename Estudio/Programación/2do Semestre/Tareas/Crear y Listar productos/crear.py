from tkinter import *
from producto import Producto

class VentanaCrearProducto:
    def __init__(self, ventana):
        ventana.geometry("500x500")
        ventana.title("Crear Producto")
        estiloFuentes = ("Comic Sans MS", 18, "bold")

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
            p.insertar()

        btnInsertar = Button(ventana, text="Guardar", font=estiloFuentes,
                            bg="blue", fg="white", command=insertarProducto)
        btnInsertar.pack()