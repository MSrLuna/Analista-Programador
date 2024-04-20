from tkinter import *
from producto import Producto
from datetime import *

class VentanaVenderProducto:
    def __init__(self, ventana):
        ventana.geometry("500x500")
        ventana.title("Crear Producto")
        estiloFuentes = ("Comic Sans MS", 18, "bold")

        labelIDventa = Label(ventana, text="ID", font=estiloFuentes)
        labelIDventa.pack()
        txtIDventa = Entry(ventana, font=estiloFuentes)
        txtIDventa.pack()

        labelCantidad = Label(ventana, text="Cantidad", font=estiloFuentes)
        labelCantidad.pack()
        txtCantidad = Entry(ventana, font=estiloFuentes)
        txtCantidad.pack()

        def VentaProducto():
            p = Producto()
            FV = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
            PID = txtIDventa.get()
            PSTOCK = txtCantidad.get()
            p.vender(PSTOCK, PID)
            ventana_historial_ventas.agregarVenta(PID, PSTOCK, FV)


        btnVender = Button(ventana, text="Vender", font=estiloFuentes,
                            bg="blue", fg="white", command=VentaProducto)
        btnVender.pack()
