from tkinter import *
from ventanatxt import *

ventana = Tk()
ventana.title("Ventana Dos")
ventana.geometry("500x500")

def abrirNventana():
    ventanatxt = Toplevel(ventana)
    segungaVentana(ventanatxt)

boton = Button(ventana, text="Abrir segunda ventana", command=abrirNventana)
boton.pack()

ventana.mainloop()