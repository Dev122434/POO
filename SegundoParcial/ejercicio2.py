import os

os.system('cls')

class Empleado():
    def __init__(self, rfc, name, paterno, materno, fecha_ingreso):
        self.rfc = rfc
        self.name = name
        self.paterno = paterno
        self.materno = materno
        self.fecha_ingreso = fecha_ingreso

    def __str__(self):
        return f'''RFC: {self.rfc}
Nombre: {self.name}
Apellido Paterno: {self.paterno}
Apellido Materno: {self.materno}
Fecha De Ingreso: {self.fecha_ingreso}
'''
    


class Contratado(Empleado):
    def __init__(self, rfc, name, paterno, materno, fecha_ingreso, sueldo, anios_laborando):
        super().__init__(rfc, name, paterno, materno, fecha_ingreso)
        self.sueldo = sueldo
        self.anios_laborando = anios_laborando
        self.porcentaje = 0.0
        self.sueldo_final = 0.0

    def calcular_sueldo(self):
        if (self.anios_laborando < 4):
            self.porcentaje = 0.05
        elif (self.anios_laborando < 8):
            self.porcentaje = 0.10
        elif (self.anios_laborando < 16):
            self.porcentaje = 0.15
        else:
            self.porcentaje = 0.20

        self.sueldo_final = self.sueldo + (self.sueldo * self.porcentaje)

    def __str__(self):
        return f'''{super().__str__()}Sueldo Base: {self.sueldo}
Años De Experiencia: {self.anios_laborando}
Porcentaje Adicional: {self.porcentaje}
Sueldo Final: {self.sueldo_final}
'''


class Destajo(Empleado):
    def __init__(self, rfc, name, paterno, materno, fecha_ingreso, num_clientes):
        super().__init__(rfc, name, paterno, materno, fecha_ingreso)
        self.num_clientes = num_clientes
        self.sueldo_final = self.num_clientes * 150

    
    def __str__(self):
        return f'''{super().__str__()}Numero De Clientes: {self.num_clientes}
Sueldo: {self.sueldo_final}
'''
    

print('\n----------------')
print('Objeto Contratado')
rfc = input('Ingrese su RFC: ')
nombre = input('Ingrese su nombre: ')
paterno = input('Ingrese su apellido paterno: ')
materno = input('Ingrese su apellido materno: ')
fecha_ingreso = input('Ingrese su fecha de ingreso: ')
sueldo = float(input('Ingrese su sueldo: '))
anios = int(input('Ingrese sus años de experiencia: '))
contratado = Contratado(rfc, nombre, paterno, materno, fecha_ingreso, sueldo, anios)
contratado.calcular_sueldo()
print(f'\n{contratado}')
print('\n----------------')
print('Objeto Destajo')
rfc_destajo = input('Ingrese su RFC: ')
nombre_destajo = input('Ingrese su nombre: ')
paterno_destajo = input('Ingrese su apellido paterno: ')
materno_destajo = input('Ingrese su apellido materno: ')
fecha_ingreso_destajo = input('Ingrese su fecha de ingreso: ')
num_clientes_destajo = int(input('Ingrese su número de clientes: '))
destajo = Destajo(rfc_destajo, nombre_destajo, paterno_destajo, materno_destajo, fecha_ingreso_destajo, num_clientes_destajo)
print(f'\n{destajo}')