class Animal():
    def __init__(self, edad, alimentacion, habitat, nombre):
        self.edad = edad
        self.alimentacion = alimentacion
        self.habitat = habitat
        self.nombre = nombre


    def __str__(self):
        return f'''
Edad: {self.edad}
Alimentacion {self.alimentacion}
Habitat {self.habitat}
Nombre: {self.nombre}
'''