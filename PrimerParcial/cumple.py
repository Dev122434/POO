import os

os.system('cls')

class Persona():

    def __init__(self, nombre, direccion, edad):
        self.nombre = nombre
        self.direccion = direccion
        self.edad = edad

    def cumpleanios(self):
        self.edad += 1

    def __str__(self):
        return f'Atributos De La Clase:\nNombre: {self.nombre}\nDireccion: {self.direccion}\nEdad: {self.edad}'
    

persona = Persona('Marcos', 'Torres Landa', 18)
persona.cumpleanios()
print(persona)