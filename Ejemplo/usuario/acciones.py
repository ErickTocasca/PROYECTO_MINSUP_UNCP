from programa import programa
from tkinter import *
import pathlib
import os.path
from tkinter import messagebox

hazel = programa.Programa("Proyecto Python - Minsup UNCP", "1080x720", "./imagen/logo_minsup_uncp.ico", "./Ejemplo/imagen/logo_minsup_uncp.ico", False)
reg = programa.Programa("REGISTRO", "600x600", "./imagen/logo_minsup_uncp.ico", "./Ejemplo/imagen/logo_minsup_uncp.ico", False)
log = programa.Programa("LOGIN", "600x600", "./imagen/logo_minsup_uncp.ico", "./Ejemplo/imagen/logo_minsup_uncp.ico", False)

class Acciones():
    
    def accion(self):
        hazel.cargar()
        hazel.texto("ACCIONES DISPONIBLES", "black", "white", 1, 6, 11, N)
        hazel.boton("REGISTRO", self.registro, 2, 6)
        hazel.boton("LOGIN", self.login, 3, 6)
        hazel.arrancar()
    
    def registro(self):
        reg.cargar()
        reg.texto("OKEY! VAMOS A REGISTRARTE", "white", "black", 0, 0, 10, W)
        reg.texto("NOMBRES: ", "white", "black", 1, 0, 10, W)
        nombre = reg.formulario(1, 10, W)
        reg.texto("APELLIDOS: ", "white", "black", 2, 0, 10, W)
        apellido = reg.formulario(2, 10, W)
        reg.texto("EMAIL: ", "white", "black", 3, 0, 10, W)
        email = reg.formulario(3, 10, W)
        reg.texto("PASSWORD: ", "white", "black", 4, 0, 10, W)
        password = reg.formulario(4, 10, W)
        
    def login(self):
        log.cargar()
        log.texto("OK! INGRESA TUS DATOS: ", "white", "black", 1, 0, 10, W)
        log.texto("EMAIL", "white", "black", 1, 0, 10, W)
        em = log.formulario(1, 10, W)
        log.texto("CONTRASEÑA", "white", "black", 2, 0, 10, W)
        cn = log.formulario(2, 10, W)