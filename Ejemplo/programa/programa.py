from tkinter import *
import pathlib
import os.path
from tkinter import messagebox

class Programa:
 
    
    def __init__(self, title, geometry, ruta, ruta_alt, resi):
        self.title = title
        self.geometry = geometry
        self.ruta = ruta
        self.ruta_alt = ruta_alt
        self.resi = resi
        
    def cargar(self):
        # ventana principal o ventana raiz
        ventana = Tk()
        self.ventana = ventana
        
        # Titulo
        ventana.title(self.title)
        
        # Dimensionarlo
        ventana.geometry(self.geometry)
        
        # ICONO
        #ruta = str(pathlib.Path().absolute()) + "/12. Tkinter/imagenes/logo_minsup_uncp.ico"
        ruta = os.path.abspath(self.ruta)
        
        if not os.path.isfile(self.ruta):
            ruta = os.path.abspath(self.ruta_alt)
        
        ventana.iconbitmap(ruta)
        
        # Estatico el dimensionamiento
        if self.resi:
            ventana.resizable(1,1)
        else:
            ventana.resizable(0,0)
        
        
    def texto(self, textos, color_fondo, color_letra, fila, columna, lapso, pegado):
        # Texto
        texto = Label(self.ventana, text=textos)
        texto.config(
            bg = color_fondo,
            fg = color_letra
            )
        texto.grid(row=fila, column=columna, columnspan=lapso, sticky=pegado)
    
    def formulario(self, fila, columna, pegado):
        formulario = Entry(self.ventana)
        formulario.grid(row=fila, column=columna, sticky=pegado)
        
    def boton(self, texto, comando, fila, columna):
        boton = Button(self.ventana, text=texto, command= comando)
        boton.grid(row=fila, column=columna)
        
    def salir(self):
        resultado = messagebox.askquestion("Salir", "¿Estas seguro que quieres salir?")
        
        if resultado != "no":
            self.ventana.destroy()
    
    def alerta_info(self, texto):
        messagebox.showinfo("Informacion", texto)
        
    def alerta_peligro(self):
        messagebox.showwarning("Peligro", texto)
    
    def alerta_error(self):
        messagebox.showerror("Error", texto)
        
    def menu(self):
        mi_menu = Menu(self.ventana)
        self.ventana.config(menu=mi_menu)
        archivo = Menu(mi_menu, tearoff=0)
        
        return [mi_menu, archivo]      
        
    def arrancar(self):     
        self.ventana.mainloop()


