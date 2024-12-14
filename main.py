# main.py
from modulo_usuarios import Usuario
from modulo_mascotas import Mascota
from modulo_citas import Cita

# Crear un usuario
usuario1 = Usuario("Juan Pérez", "juan@correo.com")

# Crear una mascota para el usuario
mascota1 = Mascota("Firulais", "Perro", 3, usuario1)

# Crear una cita para la mascota
cita1 = Cita(mascota1, "2024-12-15", "10:00 AM", "Dr. García")

# Mostrar información
usuario1.mostrar_usuario()
mascota1.mostrar_mascota()
cita1.mostrar_cita()
