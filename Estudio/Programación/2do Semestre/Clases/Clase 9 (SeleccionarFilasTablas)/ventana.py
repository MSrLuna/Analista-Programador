from tkinter import *
from tkinter.ttk import *
from ventana2 import *

ventana = Tk()
ventana.geometry("500x500")
ventana.title("Seleccionar una fila de la tabla")

tabla = Treeview(ventana, columns=("COL1", "COL2"))
tabla.column(column="#0", width=50)

fila1 = ("Valor celda 1", "Valor celda 2")
fila2 = ("Valor celda 1", "Valor celda 2")

tabla.insert("", END, values=fila1, iid="Fila 1")
tabla.insert("", END, values=fila2, iid="Fila 2")

def onClick(event):
    filaseleccionada = tabla.selection()[0]
    print(f"Fila IID: {filaseleccionada}")
    ventana2 = Toplevel(ventana)
    Ventana2(ventana2, filaseleccionada)
tabla.bind("<ButtonRelease-1>", onClick)

tabla.pack()

ventana.mainloop()