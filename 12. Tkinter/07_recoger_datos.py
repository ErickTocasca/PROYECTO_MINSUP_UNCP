from tkinter import *


ventana = Tk()

ventana.geometry("600x600")

def mostrar():
    resultado.set(dato.get())

dato = StringVar()
resultado = StringVar()

Label(ventana, text="Digite un dato: ").pack(side=TOP, anchor=NW)
Entry(ventana, textvariable=dato).pack(side=TOP, anchor=NW)

Label(ventana, text="Aqui esta tu dato: ").pack(side=TOP, anchor=NW)

mostrado = Label(ventana, textvariable=resultado)
mostrado.pack(side=TOP, anchor=NW)
Button(ventana, text="Mostrar", command=mostrar).pack(side=TOP, anchor=NW)

ventana.mainloop()