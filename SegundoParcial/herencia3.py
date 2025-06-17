import os

os.system('cls')

class Animal():
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def comunicarse(self):
        pass

    def moverse(self):
        pass

    def description(self) -> None:
        print(f"Soy un Animal y soy un tipo: {type(self).__name__}")
        print(f"Mi nombre es: {self.name}")
        print(f"Mi edad es: {self.age}")

class Perro(Animal):
    def __init__(self, name, age):
        super().__init__(name, age)
    
    # Sobrescribir un metodo de la clase Padre
    def comunicarse(self) -> None:
        print("¡Guau Guau!")
    
    def moverse(self) -> None:
        print("Caminado a 4 patas")

class Gato(Animal):
    def __init__(self, name, age):
        super().__init__(name, age)

    # Sobrescribir un metodo de la clase Padre
    def comunicarse(self) -> None:
        print("¡Miauu Miauu!")
    
    def moverse(self) -> None:
        print("Caminado con 4 patas")

class Abeja(Animal):
    def __init__(self, name, age):
        super().__init__(name, age)

    # Sobrescribir un metodo de la clase Padre
    def comunicarse(self) -> None:
        print("¡Bzzzzzzzzzz!")
    
    def moverse(self) -> None:
        print("Volando con mis pequeñas alas")

print('Clase Perro')
mi_perro = Perro("Toby", 5)
mi_perro.description()
mi_perro.comunicarse()
mi_perro.moverse()

print('\nClase Gato')
gato = Gato('Manchas', 8)
gato.description()
gato.comunicarse()
gato.moverse()

print('\nClase Abeja')
abeja = Abeja("Pegasus", 10)
abeja.description()
abeja.comunicarse()
abeja.moverse()