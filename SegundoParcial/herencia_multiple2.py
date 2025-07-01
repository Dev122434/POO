import os 

os.system('cls')

# Clase padre 1
class Estudiante():
    def __init__(self, nombre: str, edad: int):
        self.edad = edad
        self.nombre = nombre

# Clase padre 2
class Escuela():
    def __init__(self, escuela):
        self.escuela = escuela

    def nombre_escuela(self):
        print(f'Estudio en la Facultad de derecho {self.escuela}')

class Derecho(Estudiante, Escuela):
    def __init__(self, nombre, edad, escuela):
        Estudiante.__init__(self, nombre, edad)
        Escuela.__init__(self, escuela)
    
    def presentarse(self):
        print(f'Soy {self.nombre} tengo {self.edad} años y estudio Derecho')

obj = Derecho('James', 26, 'UNAM')

obj.presentarse()
obj.nombre_escuela()