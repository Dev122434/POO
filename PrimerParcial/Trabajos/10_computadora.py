import os

class Computadora():
    marca: str
    procesador: str
    memoria: str
    velocidad: str

    estado = False

    def __init__(self, marca = '', procesador = '', memoria = '', velocidad = ''):
        self.marca = marca
        self.procesador = procesador
        self.memoria = memoria
        self.velocidad = velocidad
    
    def verificar(self):
        if self.estado:
            return True
        return False
    
    def capturar(self):
        print('\nCapture los datos de la computadora: \n')
        self.marca = input('Marca de la computadora: ')
        self.procesador = input('Procesador: ')
        self.memoria = input('Capacidad de memoria: ')
        self.velocidad = input('Velocidad en Ghz')

    def encender(self):
        if self.estado:
            print('Imposible encender ... ya que ya esta encendida!!')
        else:
            print('Enseguida se encendera, espere un momento!!')
            self.estado = True
            print('La computadora se acaba de encender, ya puede trabajar en ella!')

    def apagar(self):
        print('\nLa computadora se apagara en unos segundos...')
        self.estado = False
        print('La computadora se ha apagado')

    def __str__(self):
        return f'\nMarca: {self.marca} \nProcesador: {self.procesador} \nMemoria: {self.memoria} \nVelocidad: {self.velocidad}'
    
    def imprimir(self):
        print(f'Las caracteristicas de la computadora son las siguientes: {self.__str__()}')

if __name__ == '__main__':
    computadora = Computadora()
    estado = computadora.verificar()

    if estado:
        print('\nLa computadora esta encendida')
    else:
        print('\nLa computadora esta apagada')


    computadora.encender()
    computadora.capturar()
    computadora.imprimir()
    computadora.apagar()
    computadora.encender()