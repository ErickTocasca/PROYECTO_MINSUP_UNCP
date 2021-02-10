from tkinter import *
import os.path

ventana = Tk()

ventana.geometry("600x600")

ventana.title("Proyecto Python")

ruta = os.path.abspath("./imagenes/logo_minsup_uncp.ico")

if not os.path.isfile(ruta):
    ruta = os.path.abspath("./12. Tkinter/imagenes/logo_minsup_uncp.ico")

ventana.iconbitmap(ruta)

texto = Label(ventana, text="Será un proyecto de seguridad y salud en mineria")
texto.config(
    bg = "red",
    fg = "white",
    font = ("Arial", 20),
    padx = 5,
    pady = 5
    )
texto.pack(side=TOP, anchor=SE)

texto = Label(ventana, text="MINSUP UNCP")
texto.config(
    bg = "lightblue",
    fg = "white",
    font = ("Arial", 20),
    padx = 5,
    pady = 5
    )
texto.pack(side=TOP, anchor=SE)

texto = Label(ventana, text="Hecho por alumnos de la UNCP")
texto.config(
    bg = "green",
    fg = "white",
    font = ("Arial", 20),
    padx = 5,
    pady = 5
    )
texto.pack(side=TOP, anchor=SE)

ventana.mainloop()