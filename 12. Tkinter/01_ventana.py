# TKINTER

from tkinter import *
import pathlib
import os.path



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
        
        
    def texto(self):
        # Texto
        texto = Label(self.ventana, text="Bienvenidos al primer proyecto con python")
        texto.pack()
        
        
    def arrancar(self):     
        self.ventana.mainloop()
        
programa1 = Programa("Proyecto Python - Minsup UNCP", "800x800", "./imagenes/logo_minsup_uncp.ico", "./12. Tkinter/imagenes/logo_minsup_uncp.ico", True)

programa1.cargar()
programa1.texto()
programa1.arrancar()