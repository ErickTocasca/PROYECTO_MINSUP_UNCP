import datetime
import mysql.connector
import hashlib
from tkinter import *
import pathlib
import os.path
from tkinter import messagebox

database = mysql.connector.Connect(
    host = "Localhost",
    user = "root",
    passwd = "erick",
    database = "proyecto_minsup"
    )
    
cursor = database.cursor(buffered=True)


class Usuario:
    
    def __init__(self, nombres, apellidos, email, password):
        self.nombres = nombres
        self.apellidos = apellidos
        self.email = email
        self.password = password
        
    def registrar(self):
        fecha = datetime.datetime.now()
        self.fecha = fecha
        
        
        sql = "INSERT INTO usuarios VALUES(null, %s, %s, %s, %s, %s)"
        usuario = (
            self.nombres, 
            self.apellidos, 
            self.email, 
            self.password,
            fecha)
        
        try:
            cursor.execute(sql, usuario)
            database.commit()
            result = [cursor.rowcount, self]
            
            return result
        
        except:
            result = [0, self]
            
        return result
    
    def identificar(self):
        None
        """
        sql = "SELECT * FROM usuarios WHERE email = %s AND password = %s"
        
        
        # Cifrar contraseña
        cifrado = hashlib.sha256()
        cifrado.update(self.password.encode("utf8"))
        
        usuario = (self.email, cifrado.hexadigest())
        
        cursor.execute(sql, usuario)
        result = cursor.fetchone()
        
        return result
        """




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
        
        
    def texto(self,frame, textos, color_fondo, color_letra, fila, columna, lapso, pegado):
        # Texto
        texto = Label(frame, text=textos)
        texto.config(
            bg = color_fondo,
            fg = color_letra
            )
        texto.grid(row=fila, column=columna, columnspan=lapso, sticky=pegado)
    
    def formulario(self, frame, fila, columna, pegado):
        formulario = Entry(frame)
        formulario.grid(row=fila, column=columna, sticky=pegado)
        
    def boton(self, frame, texto, comando, fila, columna):
        boton = Button(frame, text= texto, command= comando)
        boton.grid(row=fila, column=columna)
        
    def salir(self):
        resultado = messagebox.askquestion("Salir", "¿Estas seguro que quieres salir?")
        
        if resultado != "no":
            self.ventana.destroy()
    
    def alerta_info(self, texto):
        messagebox.showinfo("Informacion", texto)
        
    def alerta_peligro(self, texto):
        messagebox.showwarning("Peligro", texto)
    
    def alerta_error(self, texto):
        messagebox.showerror("Error", texto)
        
    def menu(self):
        mi_menu = Menu(self.ventana)
        self.ventana.config(menu=mi_menu)
        archivo = Menu(mi_menu, tearoff=0)
        
        return [mi_menu, archivo]      
        
    def arrancar(self):     
        self.ventana.mainloop()



class Acciones(Programa, Usuario):
    """
    def __init__(self):
        Programa.__init__(self, title, geometry, ruta, ruta_alt, resi)
        Usuario.__init__(self, nombres, apellidos, email, password)
    """
    def accion(self):
        hazel = Programa(
                "Proyecto Python - Minsup UNCP", 
                "1080x720", 
                "./imagen/logo_minsup_uncp.ico", 
                "./Ejemplo/imagen/logo_minsup_uncp.ico", 
                True
                )
        hazel.cargar()
        hazel.texto(self.ventana, "Opcines Disponibles", None, "black", 0, 0, None, None)
        hazel.boton(self.ventana, "REGISTRO", None, 1, 0)
        hazel.boton("LOGIN", None, 2, 0)
        hazel.arrancar()
    
    def registro(self):
        reg = Programa(
            "REGISTRO", 
            None, 
            "./imagen/logo_minsup_uncp.ico", 
            "./Ejemplo/imagen/logo_minsup_uncp.ico", 
            True
            )
        reg.cargar()
        
        reg.texto("OKEY! VAMOS A REGISTRARTE", "white", "black", 0, 0, None, None)
        reg.texto("NOMBRES: ", None, "black", 1, 0, None, None)
        nombres = str(reg.formulario(1, 2, None))
        reg.texto("APELLIDOS: ", None, "black", 2, 0, None, None)
        apellidos = str(reg.formulario(2, 2, None))
        reg.texto("EMAIL: ", None, "black", 3, 0, None, None)
        email = str(reg.formulario(3, 2, None))
        reg.texto("PASSWORD: ", None, "black", 4, 0, None, None)
        password = str(reg.formulario(4, 2, None))
        
        
        usuario = Usuario(nombres, apellidos, email, password)
        
        reg.boton("REGISTRAR", usuario.registrar(), 5, 0)
        
        
        
        if registrarlo[0] >= 1:
            reg.alerta_info(f"Perfecto {registrarlo[1].nombre} te has registrado con el email {registrarlo[1].email}")
            
            
        else:
            reg.alerta_error("Lo sentimos pero no te has registrado correctamente")
        
        
        reg.arrancar()
             
        
    def login(self):
        None
        
        log = Programa(
            "LOGIN", 
            "600x600", 
            "./imagen/logo_minsup_uncp.ico", 
            "./Ejemplo/imagen/logo_minsup_uncp.ico", 
            True
            )
        log.cargar()
        log.texto("OK! INGRESA TUS DATOS: ", "white", "black", 1, 0, 10, W)
        log.texto("EMAIL", "white", "black", 1, 0, 10, W)
        em = log.formulario(1, 10, W)
        log.texto("CONTRASEÑA", "white", "black", 2, 0, 10, W)
        cn = log.formulario(2, 10, W)
        
        usuario = Usuario("","",em,cn)
        login = usuario.identificar()
        
        log.boton("ENTRAR", login, 3, 10)
        
        if email == login[3]:
            log.alerta_info(f"Bienvenido {login[1]}")
            
        log.arrancar()







