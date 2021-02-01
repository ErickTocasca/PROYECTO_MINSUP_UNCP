# -*- coding: utf-8 -*-
"""
Created on Sun Jan 24 21:55:31 2021

@author: egt_d
"""

# FUNCIONES SIN ARGUMENTO
def sin_argumento():
    print("Esta es una función sin argumentos")
    
sin_argumento()

# FUNCIONES CON ARGUMENTO
def con_argumento(nombre):
    print("Hola mi nombre es ", nombre)
    
con_argumento("Erick")


# FUNCIONES CON RETURN
def suma(a, b):
    return a + b

print(suma(8, 9))