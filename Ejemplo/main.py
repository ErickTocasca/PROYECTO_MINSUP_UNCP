"""
Proyecto:
1. Abrir aisstente 
2. Login o Registro
3. Si elegimos registro, creará un usuario en la bbdd
4. Si elegimos login, identifica al usuario y nos preguntará 
    4.1 Agentes inhalables 
    4.2 Agentes Respirables
    4.3 Vibración mano brazo

"""
from tkinter import *
import pathlib
import os.path
from tkinter import messagebox
from usuario import acciones
from programa import programa

hz = acciones.Acciones()

hz.accion()
hz.registro()
from databse import database
database = database.Database()[0]
cursor = database.Database()[1]

cursor.execute("INSERT INTO inhalables VALUES")