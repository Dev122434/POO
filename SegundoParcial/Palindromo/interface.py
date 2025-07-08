import flet as ft
from palindromo import Palindromo

def main(page: ft.Page):
    page.title = "Verificador de Palíndromos"
    resultado = ft.Text("")
    lista1_text = ft.Text("")
    lista2_text = ft.Text("")
    lista3_text = ft.Text("")
    tabla = ft.DataTable(
        columns=[
            ft.DataColumn(ft.Text("Indice")),
            ft.DataColumn(ft.Text("Lista 2")),
            ft.DataColumn(ft.Text("Lista 3")),
            ft.DataColumn(ft.Text("¿Iguales?")),
        ],
        rows=[]
    )

    def verificar_palindromo(e):
        cadena = input_box.value
        obj = Palindromo(cadena)
        lista1 = obj.convertir_a_lista()
        lista2 = obj.eliminar_espacios_de_cadena()
        lista3 = obj.eliminar_espacios_y_voltear_lista(lista1)
        res = obj.es_palindromo(lista3)
        
        lista1_text.value = f"Lista 1: {lista1}"
        lista2_text.value = f"Lista 2: {[(i, c) for i, c in enumerate(lista2)]}"
        lista3_text.value = f"Lista 3: {[(i, c) for i, c in enumerate(lista3)]}"
        resultado.value = f"Resultado: {res}"

        # Construir la tabla de comparación
        tabla.rows.clear()
        max_len = max(len(lista2), len(lista3))
        for i in range(max_len):
            letra2 = lista2[i] if i < len(lista2) else ""
            letra3 = lista3[i] if i < len(lista3) else ""
            iguales = "✅" if letra2 == letra3 else "❌"
            tabla.rows.append(
                ft.DataRow(
                    cells=[
                        ft.DataCell(ft.Text(str(i))),
                        ft.DataCell(ft.Text(letra2)),
                        ft.DataCell(ft.Text(letra3)),
                        ft.DataCell(ft.Text(iguales)),
                    ]
                )
            )
        page.update()

    input_box = ft.TextField(label="Ingresa una palabra o frase", width=400)
    btn = ft.ElevatedButton("Verificar", on_click=verificar_palindromo)

    page.add(
        input_box,
        btn,
        lista1_text,
        lista2_text,
        lista3_text,
        resultado,
        tabla
    )

ft.app(target=main)