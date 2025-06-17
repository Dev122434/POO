class Empleado():
    def __init__(self, rfc, name, paterno, materno, ingreso):
        self.rfc = rfc
        self.name = name
        self.paterno = paterno
        self.materno = materno
        self.ingreso = ingreso

    def calcular_sueldo(self):
        pass
    def __str__(self):
        return f'''Nombre: {self.name}
Apellido Paterno: {self.paterno}
Apellido Materno: {self.materno}
Fecha De Ingreso: {self.ingreso}
'''
    


class Contratado(Empleado):
    def __init__(self, rfc, name, paterno, materno, ingreso, sueldo, anios_laborando):
        super().__init__(rfc, name, paterno, materno, ingreso)
        self.sueldo = sueldo
        self.porcentaje = 0
        self.sueldo_final = 0.0
        self.anios_laborando = anios_laborando

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
    def __init__(self, rfc, name, paterno, materno, ingreso, num_clientes):
        super().__init__(rfc, name, paterno, materno, ingreso)
        self.num_clientes = num_clientes
        self.monto = 150
        self.sueldo_final = 0

    def calcular_sueldo(self):
        self.sueldo_final = self.monto * self.num_clientes

    
    def __str__(self):
        return f'''{super().__str__()}Numero De Clientes: {self.num_clientes}
Sueldo: {self.sueldo_final}
'''
    

#contratado = Contratado()
destajo = Destajo("asasas", 'SCSCSC', 'SAQDADAD', 'ADADAD', '02/12/2025', 5)
print(destajo)