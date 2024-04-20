from tkinter import *
from tkinter.ttk import *

ventana = Tk()
ventana.geometry("1240x768")
ventana.title = ("Ejercicio")
tabla = Treeview(ventana)
tabla["columns"] = ("ID", "ltGénero", "ltJuegos", "ltCalificación")

tabla.column(column="#0", width=50)
tabla.column(column="ID", width=50)
tabla.column(column="ltGénero", width=100)
tabla.column(column="ltJuegos", width=150)
tabla.column(column="ltCalificación", width=100)

tabla.heading(column="ID", text="#")
tabla.heading(column="ltGénero", text="Género")
tabla.heading(column="ltJuegos", text="Juegos")
tabla.heading(column="ltCalificación", text="Calificación")

aimt = 1
filas = [(aimt, "Estrategia", "Starcraft", "10/10"), ("2", "Estrategia", "Age Of Empires III", "10/10"), ("3", "Estrategia", "Age Of Empires II", "10/10"), ("4", "Estrategia", "Plantas contra Zombies", "10/10"), ("5", "Estrategia", "Worms", "10/10")]

for i in filas:
    tabla.insert(parent="", index=END, values=i, iid=i[0])
    aimt =+ 1

tabla.pack()
ventana.mainloop()