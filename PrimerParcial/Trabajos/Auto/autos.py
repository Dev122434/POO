class Auto:
    def __init__(self, marca, modelo, año, color, placa, estado, kilometraje, propietario):
        self.marca = marca
        self.modelo = modelo
        self.año = año
        self.color = color
        self.placa = placa
        self.estado = estado
        self.kilometraje = kilometraje
        self.propietario = propietario

    def __str__(self):
        return (
            f"Marca: {self.marca}\nModelo: {self.modelo}\nAño: {self.año}\n"
            f"Color: {self.color}\nPlaca: {self.placa}\nEstado: {self.estado}\n"
            f"Kilometraje: {self.kilometraje}\nPropietario: {self.propietario}"
        )