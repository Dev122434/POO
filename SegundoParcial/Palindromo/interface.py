import flet as ft
from palindromo import Palindromo

palindromo: Palindromo

def main(page: ft.Page):
    page.title = "Palindromo"


    inputs = {
        "frase": ft.TextField(label="Frase"),
    }

    precio_cargado = ft.TextField(visible=False)


    output = ft.Text("")

    def agregar_cadena(e):
        global palindromo
        palindromo = Palindromo(inputs["frase"].value,)
        output.value = f'El objeto fue creado con la frase {palindromo}'
        page.update()

    def limpiar_campos(e):
        for v in inputs.values():
            v.value = ""
        output.value = ""
        page.update()

    def eliminar_espacios(e):
        output.value = f'Resultado de eliminar los espacios {palindromo.eliminar_espacios()}'
        page.update()

    def convertir_lista(e):
        output.value = f'La frase fue convertida a lista: {palindromo.convertir_lista()}'
        page.update()

    def is_palindromo(e):
        list_frase = palindromo.convertir_lista()
        copy_lista = palindromo.reverse_frase()
        if len(list_frase) == len(copy_lista):
            for i in range(len(list_frase)):
                if (list_frase[i] == copy_lista[i]):
                    output.value = f'lista1[{i}] = lista2[{i}]'
                else:
                    output.value = f'lista1[{i}] != lista2[{i}]'
                    break
            output.value = palindromo.is_palindromo()
            page.update()
        else:
            output.value = f'{palindromo.is_palindromo()}'
        page.update()

    btn_agregar = ft.ElevatedButton("Agregar Frase", on_click=agregar_cadena)
    btn_convertir_lista = ft.ElevatedButton("Convertir Frase A Una Lista", on_click=convertir_lista)
    btn_eliminar = ft.ElevatedButton("Eliminar Espacios", on_click=eliminar_espacios)
    btn_limpiar = ft.ElevatedButton("Limpiar Campos", on_click=limpiar_campos)
    btn_palindromo = ft.ElevatedButton('Es palindromo', on_click=is_palindromo)

    page.add(
        *inputs.values(),
        precio_cargado,
        btn_agregar,
        ft.Row([btn_convertir_lista, btn_eliminar, btn_limpiar, btn_palindromo], spacing=10),
        output
    )

ft.app(target=main)
