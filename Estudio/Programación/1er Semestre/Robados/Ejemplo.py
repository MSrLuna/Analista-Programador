from tkinter import *
from tkinter import messagebox

ventana = Tk()
ventana.geometry("1024x768")

ciudades = ["Santiago", "Valdivia", "Osorno", "Puerto Montt"] #LISTA CON LAS OPCIONES
options = StringVar() #ES LA VARIABLE DONDE SE GUARDAN LAS OPCIONES

#FUNCION QUE TOMA LO QUE SE SELECCIONE
def optionSelected(ciudad):
    if ciudad == "Santiago":
        messagebox.showwarning("Eleccion", "Ciudad peligrosa: {}".format(ciudad))
    elif ciudad == "Osorno":
        messagebox.showinfo("Eleccion", "Ciudad aceptable pero penca: {}".format(ciudad))
    else:
        messagebox.showinfo("Eleccion", "Ciudad Aceptable: ".format(ciudad))

#PARAM1 DONDE SE MUESTRA LA OPCION
#PARAM2 DONDE SE GUARDA LA OPCION SELECCIONADA 
#PARAM3 LISTA DE DATOS CON LA QUE SE CARGA EL OPTION_MENU
    #ANTES DE COLOCAR EL NOMBRE DE LA LISTA SE COLOCA UN *
#PARAM4 TIENE QUE SER LA REFERENCIA A UNA FUNCION QUE VA DEFINIR UN CODIGO QUE SE EJECUTARA
    #AL ELEGIR UNA OPCION DISTINTA
selecMenu = OptionMenu(ventana, options, *ciudades, command=optionSelected) 
selecMenu.pack()

ventana.mainloop()