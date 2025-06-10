import os

os.system('cls')

class Coordenadas():

    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __str__(self) -> str:
        return f'El valor de la coordenada x es: {self.x}\nEl valor de la coordenada y es: {self.y}'
    

punto = Coordenadas(6, 9)
print(punto)