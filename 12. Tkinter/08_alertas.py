from tkinter import *
from tkinter import messagebox

ventana = Tk()

ventana.geometry("300x300")

def alerta():
    #messagebox.showinfo("Alerta", "Los datos son erroneos")
    #messagebox.showwarning("Peligro", "Los datos son erroneos")
    messagebox.showerror("Error", "Los datos son erroneos")
    


Button(ventana, text="Alerta", command=alerta).pack()


def salir():
    resultado = messagebox.askquestion("Salir", "¿Estas seguro que quieres salir?")
    
    if resultado != "no":
        ventana.destroy()

Button(ventana, text="Salir", command=salir).pack()

ventana.mainloop()