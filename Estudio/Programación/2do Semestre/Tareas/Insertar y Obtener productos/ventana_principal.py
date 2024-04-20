from tkinter import *

from ventanas import InsertarP
from ventanas import ObtenerP

ventana = Tk()
ventana.title("Menú Productos")
ventana.geometry("260x150")
fuentes = ("segoe UI", 15)

def VentanaIP():
    ventanaActual = Toplevel(ventana)
    InsertarP(ventanaActual)

def VentanaOP():
    ventanaActual = Toplevel(ventana)
    ObtenerP(ventanaActual)

def VentanaAP():
    ventanaActual = Toplevel(ventana)
    ActualizarP(ventana)

boton1 = Button(ventana, text="Insertar productos", font=fuentes, command=VentanaIP, bg="purple", fg="pink")
boton1.pack()

boton2 = Button(ventana, text="Obtener productos", font=fuentes, command=VentanaOP, bg="purple", fg="pink")
boton2.pack()

boton3 = Button(ventana, text="Actualizar productos", font=fuentes, command=VentanaAP, bg="purple", fg="pink")
boton3.pack()

ventana.mainloop()