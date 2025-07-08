import flet as ft
from gato import Gato
from caballo import Caballo
from perro import Perro

def main(page: ft.Page):

    dd = ft.Dropdown(
        width=300,
        options=[
            ft.dropdown.Option("Perro"),
            ft.dropdown.Option("Gato"),
            ft.dropdown.Option("Caballo"),
        ],
    )
    text = ft.Text('')

    def control(e):
        resultado = dd.value

        if resultado == 'Perro':
            perro = Perro(5, 'croquetas', 'hogar', 'Toby', 25, 30, 35, 'Pelo corto', 'Labrador', 100, 0)
            text.value = perro
        elif resultado == 'Gato':
            gato = Gato(4, 'croquetas', 'hogar', 'michi', 30, 30, 38, 'corto', True, 'Macho', 10)
            text.value = gato
        elif resultado == 'Caballo':
            caballo = Caballo(10, 'Forraje', 'Corrales', 'Tiro al blanco', 60, 50, 38, 'corto', 'Arabe', 'negro', 'activo')
            text.value = caballo
        
        page.update()


    def limpiar(e):
        text.value = ''
        page.update()

    column = ft.Column(
        controls=[
            dd,
            text,
            ft.ElevatedButton('Generar Objeto', on_click=control),
        ],
        scroll=ft.ScrollMode.AUTO,
        width=400,
        height=500,
    )

    # Agregar la columna con scroll a la página
    page.add(column)

ft.app(target=main)
