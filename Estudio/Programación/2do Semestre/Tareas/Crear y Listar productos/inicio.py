from tkinter import *
from crear import VentanaCrearProducto
from listar import VentanaListarProductos
from venta import VentanaVenderProducto

ventana = Tk()
ventana.title("Inicio")
ventana.geometry("400x400")

def openCrearProducto():
    ventanaCrear = Toplevel(ventana)
    VentanaCrearProducto(ventanaCrear)

def openListarProductos():
    ventanaListar = Toplevel(ventana)
    VentanaListarProductos(ventanaListar)

def openGenerarVenta():
    ventanaVender = Toplevel(ventana)
    VentanaVenderProducto(ventanaVender)

fuentes = ("Segoe UI", 20, "bold ")
botonCrearP = Button(ventana, text="Crear Producto", font=fuentes, command=openCrearProducto, bg="purple", fg="pink")
botonCrearP.pack()
botonListarP = Button(ventana, text="Lista de Productos", font=fuentes, command=openListarProductos, bg="purple", fg="pink")
botonListarP.pack()
botonGenerarVenta = Button(ventana, text="Generar Venta", font=fuentes, command=openGenerarVenta, bg="purple", fg="pink")
botonGenerarVenta.pack()

ventana.mainloop()