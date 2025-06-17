class Animal():
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def describeme(self) -> None:
        print(f"Soy un Animal y soy un: {type(self).__name__}")
        print(f"Mi nombre es: {self.name}")
        print(f"Mi edad es: {self.age}")

class Perro(Animal):
    pass


mi_perro = Perro("Toby", 5)
mi_perro.describeme()