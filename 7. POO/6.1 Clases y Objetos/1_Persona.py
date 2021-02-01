# -*- coding: utf-8 -*-
"""
Created on Sun Jan 24 21:56:24 2021

@author: egt_d
"""

class Persona():
    
    def __init__(self, n, edad):
        self.nombre = n
        self.edad = edad
        
persona1 = Persona("Erick", 24)

print(persona1.edad)
print(persona1.nombre)