from tkinter import *
from PIL import Image, ImageTk
import os.path

ventana = Tk()

ventana.geometry("600x600")

Label(ventana, text="Bienvenido al proyecto con Python").pack()

ruta = os.path.abspath("./imagenes/minero.png")
if not os.path.isfile(ruta):
    ruta = os.path.abspath("./12. Tkinter/imagenes/minero.png")

imagen = Image.open(ruta)
render = ImageTk.PhotoImage(imagen)

Label(ventana, image = render).pack()


ventana.mainloop()