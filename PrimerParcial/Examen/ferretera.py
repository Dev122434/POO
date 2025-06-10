class Factura():
    def __init__(self, nombre, descripcion, marca, cantidad, precio):
        self.nombre: str = nombre
        self.descripcion: str = descripcion 
        self.marca: str = marca
        self.cantidad: int = cantidad
        self.precio: float = precio

    def calcular_factura(self):
        if (int(self.cantidad) > 0 and float(self.precio > 0)):
            return f"Pago por la factura: {self.cantidad * self.precio}"
        return f"Pago por la factura: {0}"
    
    def __str__(self):
        return f'''Informacion De La Factura
            Nombre: {self.nombre}
            Descripcion: {self.descripcion}
            Marca: {self.marca}
            Cantidad: {self.cantidad}
            Precio: {self.precio}
            {self.calcular_factura()}
            '''
    
    

    
    