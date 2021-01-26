# -*- coding: utf-8 -*-
"""
Created on Sun Jan 24 21:55:10 2021

@author: egt_d
"""

mineria = {
    "DTH" : "Down The Hole",
    "blasthole" : "taladro",
    "cash flow" : "flujo de caja"
    }

print(mineria)

mineria["ANFO"] = "Nitrato de Amonio con Petroleo"
print(mineria)

print(mineria["DTH"])

for key in mineria:
    print(key)
    
for key in mineria:
    print(mineria[key])