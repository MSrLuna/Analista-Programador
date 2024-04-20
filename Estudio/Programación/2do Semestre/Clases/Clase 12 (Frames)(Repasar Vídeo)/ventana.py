from tkinter import *

ventana = Tk()
ventana.geometry("1000x500")

frameIzq = Frame(ventana, width=250, height=500, bg="#13BFFF")
frameIzq.pack(side=LEFT)
frameIzq.pack_propagate(False)

def showInicio():
    frameContenido = Frame(ventana, width=750, height=500, bg="#E2B5FF")
    frameContenido.pack()
    frameContenido.pack_propagate(False)
    Label(frameContenido, text="Lista de Personas",  bg="#E2B5FF").pack()

def showFormularioPersona():
    hijos = ventana.winfo_children()
    hijos[1].destroy()
    formPersona = Frame(ventana, width=750, height=500)
    formPersona.pack()
    formPersona.pack_propagate(False)

btnP = Button(frameIzq, text="Personas", command=showFormularioPersona).pack(expand=True)
btnC = Button(frameIzq, text="Ciudades", command=showInicio).pack(expand=True)

ventana.mainloop()