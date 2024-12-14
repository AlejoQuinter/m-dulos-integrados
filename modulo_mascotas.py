# modulo_mascotas.py

class Mascota:
    def __init__(self, nombre, especie, edad, propietario):
        self.nombre = nombre
        self.especie = especie
        self.edad = edad
        self.propietario = propietario  # Referencia al objeto Usuario

    def mostrar_mascota(self):
        print(f"Mascota: {self.nombre}")
        print(f"Especie: {self.especie}")
        print(f"Edad: {self.edad}")
        print(f"Propietario: {self.propietario.nombre}")
