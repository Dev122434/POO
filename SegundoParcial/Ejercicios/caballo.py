from mamifero import Mamifero
from animal import Animal

class Caballo(Animal, Mamifero):
    def __init__(self, edad, alimentacion, habitat, nombre, peso, estatura, temperatura_corporal, tipo_pelo, linaje, color_pelo, personalidad):
        Mamifero.__init__(self, peso, estatura, temperatura_corporal, tipo_pelo)
        Animal.__init__(self, edad, alimentacion, habitat, nombre)
        self.linaje = linaje
        self.color_pelo = color_pelo
        self.personalidad = personalidad

    def hacer_sonido(self) -> None:
        print(f"{self.nombre} relincha: ¡Hiiiiiiii!")
    
    def beber_agua(self) -> None:
        print('Estoy bebiendo agua')


    def __str__(self):
        return f'''{Animal.__str__(self)}
{Mamifero.__str__(self)}
Linaje: {self.linaje}
Color De Pelo: {self.color_pelo}
Personalidad: {self.personalidad}
'''