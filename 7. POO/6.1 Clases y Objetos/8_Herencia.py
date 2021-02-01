# -*- coding: utf-8 -*-
"""
Created on Sun Jan 24 21:58:06 2021

@author: egt_d
"""

class Persona():
    
    def __init__(self, nombre, edad):
        self.nombre = nombre
        self.edad = edad
    
    def __str__(self):
         return "Nombre: " + self.nombre + ", edad: " + str(self.edad)

class Obrero(Persona):
    
    def __init__(self, nombre, edad, sueldo):
        super().__init__(nombre, edad)
        self.sueldo = sueldo
    
    def __str__(self):
        return super().__str__() + ", Sueldo: " + str(self.sueldo)
        

persona1 = Persona("Erick", 24)
print(persona1)

obrero1 = Obrero("Erick", 25, 2000.00)
print(obrero1)
