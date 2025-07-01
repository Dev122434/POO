class Perros(object):
    # Se declaran los metodos de la clase
    # Pero no se implementa aqui
    def ladrar(self):
        pass

    def grunir(self):
        pass

class Chihuahua(Perros):
    # Se implementan los metodos de la clase Padre
    def ladrar(self) -> None:
        print('\tChihuahua ladra: guau guau')

    def grunir(self) -> None:
        print('\tChihuahua gruñe: GRR GRR')

class Pastor_Aleman(Perros):
    # Se implementan los metodos de la clase Padre
    def ladrar(self) -> None:
        print('\tPastor Aleman ladra: guau guau guau guau')

    def grunir(self) -> None:
        print('\tPastor Aleman gruñe: GRR GRR GRR GRR')

class Doberman(Chihuahua, Pastor_Aleman):
    def ladrar(self, veces):
        for i in range(veces):
            print('\tDoberman ladra: guau guau guau guau')

pastor = Pastor_Aleman()
print('\nPerror Pastor Aleman: ')
pastor.ladrar()
pastor.grunir()


chihuahua = Chihuahua()
print('\nPerro Chihuahua: ')
chihuahua.ladrar()
chihuahua.grunir()

obj = Doberman()
print('\nPerro Doberman: ')
obj.ladrar(5)