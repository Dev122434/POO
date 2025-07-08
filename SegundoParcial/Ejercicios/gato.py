from mamifero import Mamifero
from animal import Animal

class Gato(Animal, Mamifero):
    def __init__(self, edad, alimentacion, habitat, nombre, peso, estatura, temperatura_corporal, tipo_pelo, flexibilidad, genero, numero_vidas):
        Animal.__init__(self, edad, alimentacion, habitat, nombre)
        Mamifero.__init__(self, peso, estatura, temperatura_corporal, tipo_pelo)
        self.flexibilidad = flexibilidad
        self.genero = genero
        self.numero_vidas = numero_vidas

    def cant_vidas(self) -> None:
        print(f'Soy un gato y tengo {self.numero_vidas} vidas')

    def hacer_sonido(self) -> None:
        print(f'{self.nombre} hace: MIAU MIAU')

    def __str__(self):
        return f'''{Animal.__str__(self)}
{Mamifero.__str__(self)}
Genero: {self.genero}
flexibilidad: {self.flexibilidad}
Numero De Vidas: {self.numero_vidas}
'''