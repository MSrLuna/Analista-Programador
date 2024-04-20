from tkinter import *
from producto import *

ventana = Tk()
fuente = ("Tahoma", 18, "bold")

labelNombre = Label(ventana, text="Nombre", font=fuente)
labelNombre.pack()

txtNombre = Entry(ventana, font=fuente)
txtNombre.pack()

labelPrecio = Label(ventana, text="Precio", font=fuente)
labelPrecio.pack()

txtPrecio = Entry(ventana, font=fuente)
txtPrecio.pack()

labelStock = Label(ventana, text="Stock", font=fuente)
labelStock.pack()

txtStock = Entry(ventana, font=fuente)
txtStock.pack()

def insertarproducto():
    p = Producto()
    p.nombre = txtNombre.get()
    p.precio = txtPrecio.get()
    p.stock = txtStock.get()
    p.insertar()
boton = Button(ventana, text="Guardar", font=fuente, bg="blue", fg="White", command=insertarproducto)
boton.pack()

ventana.mainloop()