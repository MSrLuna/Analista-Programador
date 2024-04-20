from tkinter import *

from segunda_ventana import SegundaVentana

ventana = Tk()
ventana.title("Ventana UNO")
ventana.geometry("500x500")

def abrirNuevaVentana():
    # Toplevel() nos ayuda a crear una nueva ventana secundaria (independiente)
    ventanaActual = Toplevel(ventana)
    # Llamamos al constructor de nuestra SegundaVentana().. para que funcione, tenemos
    # que crear todo el contenido gráfico dentro de ese constructor
    SegundaVentana(ventanaActual)


boton = Button(ventana, text="Abrir Segunda Ventana", command=abrirNuevaVentana)
boton.pack()

ventana.mainloop()