# modulo_usuarios.py

class Usuario:
    def __init__(self, nombre, email):
        self.nombre = nombre
        self.email = email

    def mostrar_usuario(self):
        print(f"Nombre: {self.nombre}")
        print(f"Email: {self.email}")
