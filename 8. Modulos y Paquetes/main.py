import mi_modulo
from mi_paquete.persona import Persona, Obrero

print(mi_modulo.HolaMundo().hola_mundo())

p1 = Persona()
print(p1.caminar())

o1 = Obrero()
print(o1.apellido)
print(o1.nombre)
print(o1.sueldo)
print(o1.caminar())