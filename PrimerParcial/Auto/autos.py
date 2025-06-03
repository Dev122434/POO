class Auto():

    def __init__(self, marca: str, modelo: str, anio: int, color: str,
                 placas: str, estado, kilometraje: int, propietario: str):
        self.marca = marca
        self.modelo = modelo
        self.anio = anio
        self.color = color
        self.placas = placas
        self.estado = estado
        self.kilometraje = kilometraje
        self.propietario = propietario

    def __str__(self):
        return f'Marca: {self.marca}\n \
        Modelo: {self.modelo}\n \
        Marca: {self.marca}\n \
        Año: {self.anio}\n \
        Color: {self.color}\n \
        Placas: {self.placas}\n \
        Estado: {self.estado}\n \
        Kilometraje: {self.kilometraje}\n \
        Propietario: {self.propietario}'