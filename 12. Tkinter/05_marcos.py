from tkinter import *


ventana = Tk()

ventana.geometry("1080x720")
ventana.title("Proyecto Python")

marco = Frame(ventana, width=200, height=200)
marco.config(
    bg = "blue"
    )
marco.pack(side=TOP, anchor=NE)
marco.pack_propagate(False)

texto = Label(marco, text="Primer Marco")
texto.config(
    bg = "blue",
    fg = "white",
    font = ("Arial", 20)
    )
texto.pack()


ventana.mainloop()