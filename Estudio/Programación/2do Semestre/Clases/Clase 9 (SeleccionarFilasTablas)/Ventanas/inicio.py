from tkinter import *

ventana = Tk()
ventana.geometry("500x200")
ventana.title("Ventana de inicio")

def ventanaCP():
    VCP = Toplevel(ventana)
    pass

def ventanaLP():
    pass

fuentes = ("segoe UI", 20)
botonCrearP = Button(ventana, text="Crear Producto", font=fuentes, command=ventanaCP, bg="green", fg="white")
botonCrearP.pack()

botonListarP = Button(ventana, text="Lista de Productos", font=fuentes, command=ventanaLP, bg="blue", fg="white")
botonListarP.pack()

ventana.mainloop()