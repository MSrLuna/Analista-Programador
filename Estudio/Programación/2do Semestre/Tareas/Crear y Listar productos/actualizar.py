from tkinter import *
from producto import Producto

class VentanaActualizarProducto:
    def __init__(self, ventana, iid):
        ventana.geometry("500x500")
        ventana.title("Actualizar Producto")
        estiloFuentes = ("Comic Sans MS", 18, "bold")

        p = Producto()
        tuplaResultado = p.ObtnerPorId(iid)
        p.id = iid
        p.nombre = tuplaResultado[1]
        p.precio = tuplaResultado[2]
        p.stock = tuplaResultado[3]

        labelNombre = Label(ventana, text="Nombre", font=estiloFuentes)
        labelNombre.pack()
        txtNombre = Entry(ventana, font=estiloFuentes)
        txtNombre.insert(0, p.nombre)
        txtNombre.pack()

        labelPrecio = Label(ventana, text="Precio", font=estiloFuentes)
        labelPrecio.pack()
        txtPrecio = Entry(ventana, font=estiloFuentes)
        txtPrecio.insert(0, p.precio)
        txtPrecio.pack()

        labelStock = Label(ventana, text="Stock", font=estiloFuentes)
        labelStock.pack()
        txtStock = Entry(ventana, font=estiloFuentes)
        txtStock.insert(0, p.stock)
        txtStock.pack()

        def actualizarProducto():
            p = Producto()
            p.id = iid
            p.nombre = txtNombre.get()
            p.precio=  txtPrecio.get()
            p.stock = txtStock.get()
            p.actualizar()

        btnActualizar = Button(ventana, text="Actualizar Producto", font=estiloFuentes,
                            bg="purple", fg="pink", command=actualizarProducto)
        btnActualizar.pack()

        def eliminarProducto():
            p = Producto()
            p.id = iid
            p.eliminar()
        
        btnEliminar = Button(ventana, text="Eliminar Producto", font=estiloFuentes,
                            bg="red", fg="white", command=eliminarProducto)
        btnEliminar.pack()