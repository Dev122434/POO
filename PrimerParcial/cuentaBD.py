class CuentaB():
    titular: str
    sucursal: str
    cantidad: float

    def __init__(self, titular = '', sucursal = '', cantidad = 0.0):
        self.titular = titular
        self.sucursal = sucursal
        self.cantidad = cantidad

    def ingresar_datos(self):
        self.titular = input('Ingrese el nombre del titular: ')
        self.sucursal = input('Ingrese el nombre de la sucursal: ')
        self.cantidad = float(input('Ingrese la cantidad: '))

    def mostrar(self) -> None:
        print('Datos de la cuenta')
        print(f'Titular: {self.titular} \nSucursal: {self.titular} \nCantidad: {self.cantidad}')

    def ingresar(self, cantidad):
        if cantidad <= 0:
            print('No se puede ingresar una cantidad negativa')
        else:
            self.cantidad += cantidad
            print('El ingreso fue relizado con exito')

    def retirar(self, retirar: float):
        if (retirar > self.cantidad):
            print('No se puede realizar ese retiro')
        else:
            self.cantidad -= retirar
            print('El retiro fue realizado con exito')

    def consultar(self):
        print('Estado de la cuenta')
        print(f'Cantidad: {self.cantidad}')

lista_objetos: list[CuentaB] = list()
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
        cuentaB = CuentaB()
        cuentaB.ingresar_datos()
        lista_objetos.append(cuentaB)
        while True:
            sub_menu = f'''
            1. Ingresar cantidad
            2. Retirar cantidad
            3. Ver perfil
            4. Regresar al menú principal
            '''
            print(sub_menu)
            sub_opcion = int(input('Ingrese la opcion del submenu: '))
            if sub_opcion == 1:
                ingresar = float(input('Ingrese la cantidad a ingresar: '))
                cuentaB.ingresar(ingresar)
            elif sub_opcion == 2:
                retirar = float(input('Ingrese la cantidad a retirar: '))
                cuentaB.retirar(retirar)
            elif sub_opcion == 3:
                cuentaB.mostrar()
            else:
                break
    elif opcion == 2:
        print(f'Usted tiene {len(lista_objetos)} objetos')
        index = int(input(f'Ingrese el número de indice del objeto que desea ver (0 - {len(lista_objetos) - 1}): '))
        aux: CuentaB = lista_objetos[index]
        aux.mostrar()
    else:
        break

print('Gracias por utilizar este pequeño programa')