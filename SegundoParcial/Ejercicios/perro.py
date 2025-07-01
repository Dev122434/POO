from mamifero import Mamifero
from animal import Animal

class Perro(Mamifero, Animal):
    def __init__(self, edad, alimentacion, habitat, nombre, peso, estatura, temperatura_corporal, tipo_pelo, raza, color, nivel_estres):
        Animal.__init__(self, edad, alimentacion, habitat, nombre)
        Mamifero.__init__(self, peso, estatura, temperatura_corporal, tipo_pelo)
        self.raza = raza
        self.color = color
        self.nivel_estres = nivel_estres


    def jugar(self):
        print('Me gusta jugar en el aire libre')

    def hacer_sonido(self):
        print(f'{self.nombre} hace: GUAU GUAU')