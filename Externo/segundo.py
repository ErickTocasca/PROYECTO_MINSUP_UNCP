from tkinter import ttk
from tkinter import *

import sqlite3

class DATOS:
    base="database.db"
            
    def __init__(self, ventana):
        self.wind = ventana
        self.wind.title("MENU")
        self.wind.geometry("850x600")
        
        #creando un frame container 
        
        frame1 = LabelFrame(self.wind, text = "Registrar Datos", font=("calibri", 14))
        frame1.pack()
        
        # NOMBRE INPUT
        Label(frame1, text = 'Nombres: ').grid(row = 1, column = 0)
        self.Nombre= Entry(frame1)
        self.Nombre.grid(row = 1, column = 1)
        
         # APELLIDO INPUT
        Label(frame1, text = 'Apellidos: ').grid(row = 2, column = 0)
        self.Apellido= Entry(frame1)
        self.Apellido.grid(row = 2, column = 1)
        
        # CORREO INPUT
        Label(frame1, text = 'Correo: ').grid(row = 3, column = 0)
        self.Correo= Entry(frame1)
        self.Correo.grid(row = 3, column = 1)
        
        # AREA INPUT
        Label(frame1, text = 'Área: ').grid(row = 4, column = 0)
        self.area= Entry(frame1)
        self.area.grid(row = 4, column = 1)
        
        # USUARIO INPUT
        Label(frame1, text = 'USUARIO: ').grid(row = 2, column = 5)
        self.usuario= Entry(frame1)
        self.usuario.grid(row = 2, column = 6)
        
        # CONTRASEÑA INPUT
        Label(frame1, text = 'CONTRASEÑA: ').grid(row = 3, column = 5)
        self.contra= Entry(frame1, show= "*")
        self.contra.grid(row = 3, column = 6)
        
        #BUTTON
        ttk.Button(frame1, text="REGISTRAR").grid(row = 6, columnspan = 3, sticky = W + E)
       
        #TABLA
        frame2 = LabelFrame(self.wind, text = "DATOS DEL USUARIO", font=("calibri", 14))
        frame2.pack()
       
        
        self.trv=ttk.Treeview(frame2, columns=(1,2,3,4,5,6), show="headings", height="5")
        self.trv.pack()
        
        self.trv.heading(1, text="NOMBRE")
        self.trv.heading(2, text="APELLIDO") 
        self.trv.heading(3, text="CORREO")
        self.trv.heading(4, text="AREA")
        self.trv.heading(5, text="USUARIO")
        self.trv.heading(6, text="CONTRASEÑA")
        
        self.get_supervisores()
        
   
        
        #OTRO FRAME
        
        frame3 = LabelFrame(self.wind, text = "DATOS DEL TRABAJADOR", font=("calibri", 14))
        frame3.pack()
        
        Label(frame3, text = 'NOMBRES COMPLETO: ').grid(row = 8, column = 0)
        self.trabajador= Entry(frame3)
        self.trabajador.grid(row = 8, column = 1)
        
        Label(frame3, text = 'EDAD: ').grid(row = 9, column = 0)
        self.edad= Entry(frame3)
        self.edad.grid(row = 9, column = 1)
         
        Label(frame3, text = 'CARGO: ').grid(row = 10, column = 0)
        self.cargo= Entry(frame3)
        self.cargo.grid(row = 10, column = 1)
        
        #BUTTON
        ttk.Button(frame3, text="REGISTRAR").grid(row = 12, columnspan = 3, sticky = W + E)
        
        # OPTIONS
        
        kel=StringVar()
        kel.set("PARTICULAS RESPIRABLES")
        
        OptionMenu(ventana, kel, "PARTICULAS RESPIRABLES", "PARTICULAS IHNALABLES", "VIBRACION MANO BRAZO").pack()
        
        Label(ventana, textvariable=kel).pack()
        
        
        #TABLA 2
        frame4 = LabelFrame(self.wind, text = "DATOS DEL TRABAJADOR", font=("calibri", 14))
        frame4.pack()
       
        
        self.trv=ttk.Treeview(frame4, columns=(1,2,3), show="headings", height="5")
        self.trv.pack()
        
        self.trv.heading(1, text="NOMBRES COMPLETOS")
        self.trv.heading(2, text="EDAD") 
        self.trv.heading(3, text="CARGO")
       
    def run_query(self, query, parameters =()):
        with sqlite3.connect(self.base) as conn:
            cursor=conn.cursor()
            result=cursor.execute(query, parameters)
            conn.commit()
        return result
    def get_supervisores(self):
        #clining table
        record= self.trv.get_children()
        for elemet in record:
            self.trv.delete(element)
            
         #query data   
        query='SELECT nombre, apellido, area, correo, usuario, contraseña FROM supervisores'
        
        db_rows=self.run_query(query)
        
        
        for row in db_rows:
            self.trv.insert('', 0, text= row[1], values= row)
            
            
            
        
if __name__ == '__main__':
    ventana=Tk()
    aplicacion=DATOS(ventana)
    ventana.mainloop()
  
        
        
