from tkinter import *

ventana = Tk()
ventana.geometry("600x600")

mi_menu = Menu(ventana)
ventana.config(menu=mi_menu)


def cerrar():
    ventana.destroy()


archivo = Menu(mi_menu)
archivo.add_command(label="Nuevo Archivo")
archivo.add_command(label="Abrir")
archivo.add_command(label="Abrir el ultimo cerrado")
archivo.add_separator()
archivo.add_command(label="Guardar")
archivo.add_separator()
archivo.add_command(label="Cerrar", command=cerrar)


mi_menu.add_cascade(label="Archivos", menu=archivo)
mi_menu.add_command(label="Editar")
mi_menu.add_command(label="Buscar")
mi_menu.add_command(label="Ayuda")


ventana.mainloop()