from mamifero import Mamifero
from animal import Animal

class Perro(Mamifero, Animal):
    def __init__(self, edad, alimentacion, habitat, nombre, peso, estatura, temperatura_corporal, tipo_pelo, raza, energia, nivel_estres):
        Animal.__init__(self, edad, alimentacion, habitat, nombre)
        Mamifero.__init__(self, peso, estatura, temperatura_corporal, tipo_pelo)
        self.raza: str = raza
        self.energia: float = energia
        self.nivel_estres: float = nivel_estres


    def jugar(self):
        print('Me gusta jugar en el aire libre')

    def hacer_sonido(self):
        print(f'{self.nombre} hace: GUAU GUAU')


    def __str__(self):
        return f'''{Animal.__str__(self)}
{Mamifero.__str__(self)}
Raza: {self.raza}
Energia: {self.energia}
Nivel De Estres: {self.nivel_estres}
'''