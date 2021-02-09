from io import open
import pathlib
import shutil
import os

try:
    ruta = str(pathlib.Path().absolute()) + "/texto_nuevo.txt"
    #ruta = r"D:\ERICK\DOCUMENTOS\ARCHIVOS UNIVERSIDAD\MINSUP UNCP\PROYECTO_PYTHON_MINSUP_UNCP\PROYECTO_MINSUP_UNCP\10. Manejo de Archivos\texto.txt"
    #print(ruta)
    
    archivo = open(ruta, "r")
    
    # a = append    a+
    # r = read      r+
    # w = write     w+
    
    # Agregar texto
    #archivo.write("\nEsto es un texto enviado desde python")
    
    # Leer
    #contenido = archivo.read()
    #print(contenido)
    
    # Lista
    lista = archivo.readlines()
    #print(lista)
    """
    for linea in lista:
        print(linea)
    
    # copiar - mover
    ruta_or = str(pathlib.Path().absolute()) + "/texto_nuevo.txt"
    ruta_new = str(pathlib.Path().absolute()) + "/texto_copiado.txt"
    
    shutil.copyfile(ruta_or, ruta_new)
    """
    
    # Elimnar
    ruta_new = str(pathlib.Path().absolute()) + "/texto_copiado.txt"
    os.remove(ruta_new)
    
    
except Exception as e:
    print(type(e).__name__)

finally:
    archivo.close()

