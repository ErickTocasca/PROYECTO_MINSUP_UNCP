import mysql.connector

database = mysql.connector.Connect(
    host = "localhost",
    user = "root",
    passwd = "erick",
    database = "proyecto_minsup"
)

cursor = database.cursor(buffered=True)

cursor.execute("CREATE DATABASE IF NOT EXISTS proyecto_minsup")

cursor.execute("""CREATE TABLE IF NOT EXISTS usuarios(
id          int(25) auto_increment not null,    
nombres     varchar(255) not null,
apellidos   varchar(255) not null,
email       varchar(255) not null,
password    varchar(255) not null,
fecha       date not null,
CONSTRAINT pk_usuarios PRIMARY KEY(id),
CONSTRAINT uq_email UNIQUE(email)
    )ENGINE=InnoDb;        
""")

cursor.execute("""CREATE TABLE IF NOT EXISTS inhalables(
id          int(25) auto_increment not null,
usuario_id  int(25) not null,
nombres     varchar(255) not null,
apellidos   varchar(255) not null,
edad        int(25) not null,
años        int(25) not null,
fecha       date not null,
mf1         int(25),
mo1         int(25),
mf2         int(25),
mo2         int(25),
mf3         int(25),
mo3         int(25),
mf4         int(25),
mo4         int(25),
mf5         int(25),
mo5         int(25),
mf6         int(25),
mo6         int(25),
CONSTRAINT pk_inhalables PRIMARY KEY(id),
CONSTRAINT fk_inhalables_usuario FOREIGN KEY(usuario_id) REFERENCES usuarios(id)
    )ENGINE=InnoDb           
""")


cursor.execute("""CREATE TABLE IF NOT EXISTS respirables(
id          int(25) auto_increment not null,
usuario_id  int(25) not null,
nombres     varchar(255) not null,
apellidos   varchar(255) not null,
edad        int(25) not null,
años        int(25) not null,
fecha       date not null,
mf1         int(25),
mo1         int(25),
mf2         int(25),
mo2         int(25),
mf3         int(25),
mo3         int(25),
mf4         int(25),
mo4         int(25),
mf5         int(25),
mo5         int(25),
mf6         int(25),
mo6         int(25),
CONSTRAINT pk_respirables PRIMARY KEY(id),
CONSTRAINT fk_respirables_usuario FOREIGN KEY(usuario_id) REFERENCES usuarios(id)
    )ENGINE=InnoDb            
""")



cursor.execute("""CREATE TABLE IF NOT EXISTS vibracion(
id          int(25) auto_increment not null,
usuario_id  int(25) not null,
nombres     varchar(255) not null,
apellidos   varchar(255) not null,
edad        int(25) not null,
años        int(25) not null,
fecha       date not null,
ax          int(25),
ay          int(25),
az          int(25),
CONSTRAINT pk_vibracion PRIMARY KEY(id),
CONSTRAINT fk_vibracion_usuario FOREIGN KEY(usuario_id) REFERENCES usuarios(id)
    )ENGINE=InnoDb            
""")































