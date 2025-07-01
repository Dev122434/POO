import os 

os.system('cls')

class Padre():
    def __init__(self, ojos, cejas):
        self.ojos = ojos
        self.cejas = cejas
    
class Hijo(Padre):
    def __init__(self, ojos, cejas, cara):
        Padre.__init__(self, ojos, cejas)
        self.cara = cara

tomas = Hijo('Ojos Marrones', 'Cejas Negras', 'Cara Larga')
print(f'Las caracteristicas de Tomas son: {tomas.ojos} {tomas.cejas} {tomas.cara}')