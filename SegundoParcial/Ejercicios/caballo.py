from mamifero import Mamifero
from animal import Animal

class Caballo(Mamifero):
    def __init__(self, edad, alimentacion, habitat, nombre, peso, estatura, temperatura_corporal, tipo_pelo, raza, color_pelo, personalidad):
        Mamifero.__init__(self, peso, estatura, temperatura_corporal, tipo_pelo)
        Animal.__init__(self, edad, alimentacion, habitat, nombre)
        self.raza = raza
        self.color_pelo = color_pelo
        self.personalidad = personalidad

    def hacer_sonido(self) -> None:
        print(f"{self.nombre} relincha: ¡Hiiiiiiii!")
    
    def beber_agua(self) -> None:
        print('Estoy bebiendo agua')