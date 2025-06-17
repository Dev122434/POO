class Persona():
    def __init__(self, name, last_name, age, estado_civil, genero):
        self.name = name
        self.last_name = last_name
        self.age = age
        self.estado_civil = estado_civil
        self.genero = genero

    def __str__(self):
        return f'''Nombre: {self.name}
Apellidos: {self.last_name}
Edad: {self.age}
Estado Civil: {self.estado_civil}
Genero: {self.genero}
'''


class Doctor(Persona):
    def __init__(self, name, last_name, age, estado_civil, genero,
                 especialidad, area_estudio, grado, anios_experiencia
                 ):
        super().__init__(name, last_name, age, estado_civil, genero)
        self.especialidad = especialidad
        self.area_estudio = area_estudio
        self.grado = grado
        self.anios_experiencia = anios_experiencia

    def __str__(self):
        return f'''{super().__str__()}Especialidad: {self.especialidad}
Area De Estudio: {self.area_estudio}
Grado: {self.grado}
Años De Experiencia: {self.anios_experiencia}
'''

class Ingeniero(Persona):
    def __init__(self, name, last_name, age, estado_civil, genero,
                 area, herramientas, especialidad, proyectos):
        super().__init__(name, last_name, age, estado_civil, genero)
        self.area = area
        self.herramientas = herramientas
        self.especialidad = especialidad
        self.proyectos = proyectos

    def __str__(self):
        return f'''{super().__str__()}Area: {self.area}
Herramientas: {self.herramientas}
Especialidad: {self.especialidad}
Proyectos: {self.proyectos}
'''

class Licenciado(Persona):
    def __init__(self, name, last_name, age, estado_civil, genero,
                 despacho, especialidad, area, num_registro):
        super().__init__(name, last_name, age, estado_civil, genero)
        self.despacho = despacho
        self.especialidad = especialidad
        self.area = area
        self.num_registro = num_registro

    def __str__(self):
        return f'''{super().__str__()}Area: {self.area}
Despacho: {self.despacho}
Especialidad: {self.especialidad}
Numero De Registro: {self.num_registro}
'''
    

persona = Persona("Joel", 'Garcia', 35, 'Soltero', 'Masculino')
doctor = Doctor("Emiliano", 'Hernandez', 40, 'Soltero', 'Masculino', 'Cardiología', 'Medicina Interna', 'Doctorado', 12)
ingeniero = Ingeniero("Marcos", 'Cardenas', 22, 'Soltero', 'Masculino', 'Desarrollo de Software', 'Java, Spring Boot y Git', 'Desarrollo Backend', 'Sistema de inventario')
licenciado = Licenciado("Alejandra", 'Aguilera', 28, 'Casada', 'Femenino', 'Despacho Jurídico López & Asociados', 'Derecho Penal', 'Defensa', 78956)

print(persona)
print(doctor)
print(ingeniero)
print(licenciado)