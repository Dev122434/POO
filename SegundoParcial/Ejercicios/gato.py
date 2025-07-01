from mamifero import Mamifero
from animal import Animal

class Gato(Animal, Mamifero):
    def __init__(self, edad, alimentacion, habitat, nombre, peso, estatura, temperatura_corporal, tipo_pelo, color, raza, numero_vidas):
        Animal().__init__(edad, alimentacion, habitat, nombre)
        Mamifero.__init__(self, peso, estatura, temperatura_corporal, tipo_pelo)
        self.color = color
        self.raza = raza
        self.numero_vidas = numero_vidas

    def cant_vidas(self) -> None:
        print(f'Soy un gato y tengo {self.numero_vidas} vidas')

    def hacer_sonido(self) -> None:
        print(f'{self.nombre} hace: MIAU MIAU')