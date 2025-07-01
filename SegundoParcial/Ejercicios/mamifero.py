from animal import Animal

class Mamifero(Animal):
    def __init__(self, peso, estatura, temperatura_corporal, tipo_pelo):
        self.peso = peso
        self.estatura = estatura
        self.temperatura_corporal = temperatura_corporal
        self.tipo_pelo = tipo_pelo