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
        self.velocidad = input('Velocidad en Ghz: ')

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

lista_objetos: list[Computadora] = list()
while True:
    menu = f'''
    Menu de opciones:
    1. Capturar
    2. Ver datos
    3. Salir
    '''
    print(menu)
    opcion = int(input('Ingrese una opcion del menu: '))
    if (opcion == 1):
        computadora = Computadora()
        computadora.capturar()
        lista_objetos.append(computadora)
        print('Acciones de la computadora')
        sub_menu = f'''
        1. Encender
        2. Estado
        3. Apagar
        '''
        print(sub_menu)
        text = 'Ingrese la opcion para la computadora: '
        sub_opcion = int(input(text))
        while True:
            if sub_opcion == 1:
                computadora.encender()
                print('Para poder regresar al menu de opciones, debe apagar la computadora')
            elif sub_opcion == 2:
                result = 'La computadora esta encendida' if computadora.estado else 'La computadora esta apagada'
                print(result)
            else:
                computadora.apagar()
                break
            print(sub_menu)
            sub_opcion = int(input(text))
            
    elif opcion == 2:
        print(f'Usted tiene {len(lista_objetos)} objetos')
        index = int(input(f'Ingrese el número de indice del objeto que desea ver (0 - {len(lista_objetos) - 1}): '))
        aux: Computadora = lista_objetos[index]
        aux.imprimir()
    else:
        break

print('Gracias por utilizar este pequeño programa')