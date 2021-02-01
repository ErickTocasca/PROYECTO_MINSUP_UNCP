# -*- coding: utf-8 -*-
"""
Created on Sun Jan 24 21:57:54 2021

@author: egt_d
"""

class Persona():
    
    def __init__(self, nombre, apellido):
        self.nombre = nombre
        self.apellido = apellido
        
    def __metodo_privado(self):
        print("Nombre: " + self.nombre + ", Apellido: " + self.apellido)
        
    def metodo_publico(self):
        return self.__metodo_privado()


persona1 = Persona("Valentina", "Perez")
#persona1.__metodo_privado()
persona1.metodo_publico()