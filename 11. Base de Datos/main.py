import mysql.connector

# conexion 

database = mysql.connector.Connect(
    host = "Localhost",
    user = "root",
    passwd = "erick",
    database = "proyecto_minsup"
    )

# print(database)

# CURSOR 
cursor = database.cursor(buffered=True)

# CREAR LA BASE DE DATOS
cursor.execute("CREATE DATABASE IF NOT EXISTS proyecto_minsup")

# CREAR UNA TABLA
cursor.execute("""
CREATE TABLE IF NOT EXISTS participantes(
id          int(10) auto_increment not null,
nombre      varchar(50) not null,
apellido    varchar(50) not null,
edad        int(10) not null,
CONSTRAINT pk_participantes PRIMARY KEY(id) 
    )
""")

# AGREGAR RAPIDA
participantes = [
    ("Gabriel", "Tom", 18),
    ("Fernando", "Fernanadez", 19),
    ("Raul", "Jimenez", 22),
    ("Maria", "Alvarez", 18),
    ]

cursor.executemany("INSERT INTO participantes VALUES (null, %s, %s, %s)", participantes)
database.commit()








