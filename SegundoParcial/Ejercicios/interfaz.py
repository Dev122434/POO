import flet as ft
from mamifero import Mamifero
from caballo import Caballo

def caballo():
    caballo = Caballo(edad, alimentacion, habitat, nombre, peso, estatura, temperatura_corporal, tipo_pelo, raza, color_pelo, personalidad)
    return caballo

def generar_boton(e):
    return ft.ElevatedButton('Generar Caballo',on_click=caballo)

def campos_texto(selected_animal: str):
    nombre = ft.TextField(label="Nombre del mamífero")
    edad = ft.TextField(label="Edad")
    alimentacion = ft.TextField(label="Alimentación")
    habitat = ft.TextField(label="Hábitat")
    peso = ft.TextField(label="Peso (kg)")
    estatura = ft.TextField(label="Estatura (cm)")
    temperatura = ft.TextField(label="Temperatura corporal")
    tipo_pelo = ft.TextField(label="Tipo de pelo")

    if selected_animal == 'Perro':
        raza = ft.TextField(label="Raza")
        color = ft.TextField(label="Color")
        nivel_estres = ft.TextField(label="Nivel de estres")
        return nombre, edad, alimentacion, habitat, peso, estatura, temperatura, tipo_pelo, raza, color, nivel_estres
    elif selected_animal == 'Gato':
        color = ft.TextField(label="Color")
        raza = ft.TextField(label="Raza")
        numero_vidas = ft.TextField(label="Numero De Vidas")
        return nombre, edad, alimentacion, habitat, peso, estatura, temperatura, tipo_pelo, raza, color, numero_vidas
    else:
        raza = ft.TextField(label="Raza")
        color = ft.TextField(label="Color")
        personalidad = ft.TextField(label="Personalidad", visible=True)
        boton = ft.ElevatedButton('Generar Caballo', on_click=generar_caballo)
        return nombre, edad, alimentacion, habitat, peso, estatura, temperatura, tipo_pelo, raza, color, personalidad

def main(page: ft.Page):

    animales = ['Perro', 'Gato', 'Caballo']

    value = False

    resultado_text = ft.Text("", size=18)
    
    def get_options():
        return [
            ft.DropdownOption(
                key=animal,
                content=ft.Text(animal)
            ) for animal in animales
        ]

    dd = ft.Dropdown(
        width=300,
        options=[
            ft.dropdown.Option("Perro"),
            ft.dropdown.Option("Gato"),
            ft.dropdown.Option("Caballo"),
        ],
    )

    resultado = ft.Text()

    page.add(dd)

    def generar_formulario(e):
        resultado.value = dd.value
        nombre, edad, alimentacion, habitat, peso, estatura, temperatura, tipo_pelo, raza, color, personalidad = campos_texto(resultado)
        page.add(nombre, edad, alimentacion, habitat, peso, estatura, temperatura, tipo_pelo, raza, color, personalidad)
        page.update()


ft.app(target=main)
