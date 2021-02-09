import os 

# CREAR CARPETA

if not os.path.isdir("./Ejemplo"):
    os.mkdir("./Ejemplo")
else:
    print("El directorio ya existe")