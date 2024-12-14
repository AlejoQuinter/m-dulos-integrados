# modulo_citas.py

class Cita:
    def __init__(self, mascota, fecha, hora, veterinario):
        self.mascota = mascota  # Objeto de la clase Mascota
        self.fecha = fecha
        self.hora = hora
        self.veterinario = veterinario

    def mostrar_cita(self):
        print(f"Cita para {self.mascota.nombre} el {self.fecha} a las {self.hora}")
        print(f"Veterinario: {self.veterinario}")
