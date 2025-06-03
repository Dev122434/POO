import flet as ft


def main(page: ft.Page):

    text_opciones = ft.Text(value='Escoja una opcion')
    opciones = ft.Dropdown(
        width=200,
        options=[
            ft.DropdownOption("Todos los atributos"),
            ft.DropdownOption("Algunos atributos")
        ],
    )
    page.add(text_opciones, opciones)

    page.add(ft.Text('Ingrese la marca del auto: '))
    text_marca = ft.TextField(label="Marca", value='Marca')
    page.add(ft.Text('Ingrese el modelo del auto: '))
    text_modelo = ft.TextField(label="Modelo", value='Modelo')
    page.add(ft.Text('Ingrese el año del auto: '))
    text_anio = ft.TextField(label="Año", value='Año')
    page.add(ft.Text('Ingrese el color del auto: '))
    text_color = ft.TextField(label="Color", value='Color')
    page.add(ft.Text('Ingrese las placas del auto: '))
    text_placas = ft.TextField(label="Placas", value='Placas')
    page.add(ft.Text('Ingrese el estado del auto: '))
    text_estado = ft.TextField(label="Estado", value='Estado')
    page.add(ft.Text('Ingrese el kilometraje del auto: '))
    text_kilometraje = ft.TextField(label="Kilometraje", value='Kilometraje')
    page.add(ft.Text('Ingrese el propietario del auto: '))
    text_propietario = ft.TextField(label="Propietario", value='Propietario')
    page.add(text_marca, text_modelo, text_anio, text_color, text_placas, text_estado, text_kilometraje, text_propietario)


ft.app(main)