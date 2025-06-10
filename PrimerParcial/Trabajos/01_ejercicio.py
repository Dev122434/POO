class Computadora():
    def __init__(self, cantidad_memoria: int, marca: str, procesador: str, velocidad: float, precio: float, almacenamiento: int):
        self.marca = marca
        self.procesador = procesador
        self.precio = precio
        self.cantidad_memoria = cantidad_memoria
        self.velocidad = velocidad
        self.almacenamiento = almacenamiento

    def impresion(self) -> None:
        print('La computadora tiene estas caracteristicas')
        print(f'Marca {self.marca}, Procesador {self.procesador}, Precio {self.precio}, Cantidad de memoia RAM {self.cantidad_memoria}, Velocidad {self.velocidad} y tiene un almacenamiento de {self.almacenamiento}')



computadora1 = Computadora(16, 'HP', 'I9', 2.8, 8500, 256)
computadora2 = Computadora(8, 'ACER', 'I7', 2.9, 9850, 512)

computadora1.impresion()
print()
computadora2.impresion()
