import os

os.system('cls')

class Humano():

    def __init__(self, edad: int, nombre: str, ocupacion: str):
        self.edad = edad
        self.nombre = nombre
        self.ocupacion = ocupacion
        
    def __str__(self) -> str:
        return f'Hola soy {self.nombre}, mi edad es {self.edad} y mi ocupacion es {self.ocupacion}'
    
    def contratar(self, puesto: str):
        self.puesto = puesto
        print(f'{self.nombre} ha sido contratado como {self.puesto}')
        self.ocupacion = puesto

personal = Humano(18, 'Pedro', 'Desocupado')
print(personal)
personal.contratar('Obrero')
print(personal)