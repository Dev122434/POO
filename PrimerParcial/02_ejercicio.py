class Computadora():
    def __init__(self):
        self.marca = None
        self.procesador = 'I9'
        self.precio = 9500
        self.cantidad_memoria = 16
        self.velocidad = 2.8
        self.almacenamiento = 256

    def impresion(self) -> None:
        print('La computadora tiene estas caracteristicas')
        print(f'Marca {self.marca}, Procesador {self.procesador}, Precio {self.precio}, Cantidad de memoia RAM {self.cantidad_memoria}, Velocidad {self.velocidad} y tiene un almacenamiento de {self.almacenamiento}')



computadora1 = Computadora()
computadora1.marca = 'ACER'
computadora2 = Computadora()
computadora2.marca = 'Lenovo'

computadora1.impresion()
print()
computadora2.impresion()
