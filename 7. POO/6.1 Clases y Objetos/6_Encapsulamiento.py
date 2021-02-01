# -*- coding: utf-8 -*-
"""
Created on Sun Jan 24 21:57:35 2021

@author: egt_d
"""

class Persona():
    
    def __init__(self, nombre, edad):
        self.__nombre = nombre
        self.__edad = edad
        
    def get_nombre(self):
        return self.__nombre
    
    def set_nombre(self, nombre):
        self.__nombre = nombre
    
        

persona1 = Persona("Erick", 24)
# print(persona1.__nombre) ERRROR
print(persona1.get_nombre())

persona1.set_nombre("Karla")
print(persona1.get_nombre())