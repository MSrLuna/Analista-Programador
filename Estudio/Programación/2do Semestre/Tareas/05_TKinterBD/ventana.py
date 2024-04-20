from tkinter import *
from producto import Producto

ventana = Tk()
ventana.geometry("500x500")
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
    # como el método para insertar en la tabla producto está en la CLASE Producto..
    # Lo primero que tengo que hacer es CREAR un OBJETO de la clase Producto
    p = Producto()
    p.nombre = txtNombre.get()
    p.precio=  txtPrecio.get()
    p.stock = txtStock.get()
    p.insertar()

btnInsertar = Button(ventana, text="Guardar", font=estiloFuentes,
                     bg="blue", fg="white", command=insertarProducto)
btnInsertar.pack()

ventana.mainloop()