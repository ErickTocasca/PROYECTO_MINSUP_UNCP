import os 

# CREAR CARPETA

if not os.path.isdir("./Cristhian"):
    os.mkdir("./Cristhian")
else:
    print("El directorio ya existe")