# -*- coding: utf-8 -*-
"""
Created on Sun Jan 24 21:56:40 2021

@author: egt_d
"""

class Aritmetica:
    
    def __init__(self, n1, n2):
        self.numero_uno = n1
        self.numero_dos = n2
        
    def suma(self):
        print(self.numero_dos + self.numero_uno)
        

aritmetica = Aritmetica(15, 26)

aritmetica.suma()