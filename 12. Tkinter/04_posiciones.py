from tkinter import *

ventana = Tk()

ventana.geometry("600x600")

ventana.title("Proyecto Python")


texto = Label(ventana, text="Bienvenido")
texto.config(
    bg = "red",
    fg = "white",
    font = ("Arial",20),
    padx = 5,
    pady = 5
    )
texto.pack(side = RIGHT, fill=X, expand=YES)


ventana.mainloop()