import datetime
import mysql.connector
# import hashlib

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
