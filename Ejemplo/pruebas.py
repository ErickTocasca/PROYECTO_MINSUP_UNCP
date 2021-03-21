
"""
import mysql.connector

database = mysql.connector.Connect(
    host = "Localhost",
    user = "root",
    passwd = "erick",
    database = "proyecto_minsup"
    )
    
cursor = database.cursor(buffered=True)


import datetime


fecha = datetime.datetime.now()

integrante = ("Gerardo", "Tocasca", "gerardo@gerardo.com", "erick", fecha)


sql = "INSERT INTO usuarios VALUES(null, %s, %s, %s, %s, %s)"

cursor.execute(sql, integrante)
database.commit()
"""
"""
from usuario.usuario import Usuario

usuario = Usuario("Jorch", "Fernandez", "jorch@jorch.com", "jorch")
registrar = usuario.registrar()

if registrar[0] >= 1:
    print(f"Perfecto {registrar[1].nombres} te has registrado con el email {registrar[1].email}")
    
else:
    print("Lo sentimos pero no te has registrado correctamente")
   
"""

from programas import programa
  
pro = programa.Programa("hola", "600x600", "./imagen/logo_minsup_uncp.ico", "./Ejemplo/imagen/logo_minsup_uncp.ico", False)
pro.cargar()
pro.arrancar()   
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    