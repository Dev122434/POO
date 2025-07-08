class Mamifero():
    def __init__(self, peso, estatura, temperatura_corporal, tipo_pelo):
        self.peso = peso
        self.estatura = estatura
        self.temperatura_corporal = temperatura_corporal
        self.tipo_pelo = tipo_pelo


    def __str__(self):
        return f'''
Peso: {self.peso}
Estatura: {self.estatura}
Temperatura Corporal: {self.temperatura_corporal}
Tipo De Pelo: {self.tipo_pelo}
'''