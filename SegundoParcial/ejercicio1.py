class Persona():
    def __init__(self, name, last_name, age, estado_civil, tipo):
        self.name = name
        self.last_name = last_name
        self.age = age
        self.estado_civil = estado_civil
        self.tipo = tipo



class Doctor(Persona):
    def __init__(self, name, last_name, age, email, tipo, especialidad,
                 area_estudio, grado
                 ):
        super().__init__(name, last_name, age, email, tipo)
        self.especialidad = especialidad
        self.area_estudio = area_estudio
        self.grado = grado

class Ingeniero(Persona):
    def __init__(self, name, last_name, age, estado_civil, tipo,
                 area, herramientas, especialidad, proyectos
                 ):
        super().__init__(name, last_name, age, estado_civil, tipo)
        self.
    pass

class Licenciado(Persona):
    pass