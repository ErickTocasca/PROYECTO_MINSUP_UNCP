# -*- coding: utf-8 -*-
"""
Created on Sun Jan 24 21:57:21 2021

@author: egt_d
"""

class Persona():
    
    def __init__(this, n, e, *t, **d):
        this.nombre = n
        this.edad = e
        this.tupla = t
        this.diccionario = d
    
    def sumar(self):
        return self.edad + self.edad
    
        
     
persona1 = Persona("Erick", 24)
print(persona1.edad)
print(persona1.nombre)
print(persona1.tupla)

print("\n")

persona2 = Persona("Juan", 25, 1,5,6,8)
print(persona2.edad)
print(persona2.nombre)
print(persona2.tupla)

persona3 = Persona("Alberto", 26, 1,4,7,8, m="manzana",d="durazno")
print(persona3.edad)
print(persona3.nombre)
print(persona3.tupla)
print(persona3.diccionario)

print(persona1.sumar())