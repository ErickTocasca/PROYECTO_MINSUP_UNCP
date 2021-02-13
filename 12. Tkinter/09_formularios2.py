from tkinter import *


ventana = Tk()

ventana.geometry("800x800")

encabezado = Label(ventana, text="Formularios 2")
encabezado.config(
    bg = "green",
    padx = 10,
    pady = 10,
    font = ("Console", 20),
    )
encabezado.grid(row=0, column=0, columnspan=10)

# CHECKBUTTTON


Label(ventana, text="¿A que area perteneces?").grid(row=1, column=0)

def mostrar():
    texto = ""
    
    if planeamiento.get():
        texto += "Planeamiento"
        
    elif operaciones.get():
        texto += "Operaciones"
        
    elif seguridad.get():
        texto += "Seguridad"
        
    resultado.config(
        text = texto,
        bg ="green",
        fg = "white"
        )
        
    

planeamiento = IntVar()
operaciones = IntVar()
seguridad = IntVar()


Checkbutton(
    ventana, 
    text="Planeamiento",
    variable= planeamiento,
    onvalue=1,
    offvalue=0,
    command=mostrar
).grid(row=2, column=0)

Checkbutton(
    ventana, 
    text="Operaciones",
    variable=operaciones,
    onvalue=1,
    offvalue=0,
    command=mostrar
).grid(row=3, column=0)

Checkbutton(
    ventana, 
    text="Seguridad",
    variable=seguridad,
    onvalue=1,
    offvalue=0,
    command=mostrar
).grid(row=4, column=0)


resultado = Label(ventana)
resultado.grid(row=6, column=0)



# RADIOBUTTON
Label(ventana, text= "¿Cual es tu genero").grid(row=7, column=0)

opcion = StringVar()
opcion.set(None)
ver=StringVar()

def tu_genero():
    ver.set(opcion.get())


Radiobutton(
    ventana, 
    text="Masculino", 
    variable = opcion,
    value="Masculino",
    command = lambda: tu_genero()
).grid(row=8, column=0)

Radiobutton(
    ventana, 
    text="Femenino",
    variable=opcion,
    value="Femenino",
    command=tu_genero
).grid(row=9, column=0)

Label(ventana, text="Esta es tu opción").grid(row=10)
genero = Label(ventana, textvariable=ver)
genero.grid(row=11)

# OPTION MEN
kel=StringVar()
kel.set("Opcion 1")

OptionMenu(ventana, kel, "Opcion 1", "Opcion 2", "Opcion 3").grid(row=8, column=1)

Button(ventana, text="Mostrar").grid(row=9, column=1)

Label(ventana, textvariable=kel).grid(row=10, column=1)

ventana.mainloop()





















