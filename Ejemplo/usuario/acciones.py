from usuario.programa import Programa
"""
from usuario import Usuario

usuario = Usuario("Vale", "Fernandez", "vale@vale.com", "vale")
registrar = usuario.registrar()

if registrar[0] >= 1:
    print(f"Perfecto {registrar[1].nombres} te has registrado con el email {registrar[1].email}")
    
else:
    print("Lo sentimos pero no te has registrado correctamente")
"""
pro = Programa("hola", "600x600", "./imagen/logo_minsup_uncp.ico", "./Ejemplo/imagen/logo_minsup_uncp.ico", False)
pro.cargar()
pro.arrancar()      

"""
class Acciones():
    def accion(self):
        hazel = Programa(
                "Proyecto Python - Minsup UNCP", 
                "1080x720", 
                "./imagen/logo_minsup_uncp.ico", 
                "./Ejemplo/imagen/logo_minsup_uncp.ico", 
                True
                )
        hazel.cargar()
        hazel.texto("Opcines Disponibles", None, "black", 0, 0, None, None)
        hazel.boton("REGISTRO", self.registro, 1, 0)
        hazel.boton("LOGIN", self.login, 2, 0)
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
            
        
            
        
 """            
        
        
        
        
        
        
        
        
        
        
        
        