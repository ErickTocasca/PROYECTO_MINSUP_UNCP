from tkinter import *

ventana = Tk()

ventana.geometry("800x800")

# ENCABEZADO
encabezado = Label(ventana, text="Formulario: ")
encabezado.config(
    bg = "gray",
    fg = "white",
    font = ("Arial", 30)
    )
encabezado.grid(row=0, column=0, columnspan=10)

# texto Nombre
texto = Label(ventana, text="Nombre: ")
texto.grid(row=1, column=0)

# formulario
formulario = Entry(ventana)
formulario.grid(row=1, column=1, sticky=W)

# texto Nombre
texto = Label(ventana, text="Apellido: ")
texto.grid(row=2, column=0)

# formulario
formulario = Entry(ventana)
formulario.grid(row=2, column=1, sticky=W)

# texto descripción
texto = Label(ventana, text="Descripción: ")
texto.grid(row=3, column=0)

# formulario
formulario = Text(ventana, width=30, height=30)
formulario.grid(row=3, column=1)

# Boton
boton = Button(ventana, text="Enviar")
boton.grid(row=4, column=1)

ventana.mainloop()