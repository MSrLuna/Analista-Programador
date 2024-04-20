from tkinter import *
from tkinter import messagebox

ventana = Tk()
ventana.geometry("500x500")

# Necesitamos una lista de datos para que podamos cargar con esta información nuestro OptionMenu..
listaCiudades = ["Santiago", "Valdivia", "Osorno", "Puerto Montt"]
# Para capturar el valor seleccionado, tenemos que crear una variable de tipo StringVar()
ciudadSeleccionada = StringVar()

# Este método se ejecutará cada vez que se seleccione un ítem en el OptionMenu
def onOptionSelected(ciudad):
    print(ciudad)
    messagebox.showinfo(title="Ciudad Seleccionada", message=ciudad)

# PARAM 1: la ventana dónde se "pintará" el OptionMenu
# PARAM 2: la variable de tipo StringVar() que va a almacenar el valor seleccionado
# PARAM 3: la lista de datos con que vamos a cargar el OptionMenu. OJO: vamos a agregarle
# a nuestra variable de tipo lista, justo antes, un símbolo *
# PARAM 4: tiene que ser la referencia a una función que va a definir un código que
# se ejecutará cada vez que seleccionemos un ítem diferente
seleccionable = OptionMenu(ventana, ciudadSeleccionada, *listaCiudades, command=onOptionSelected)
seleccionable.pack()

ventana.mainloop()