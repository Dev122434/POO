import flet as ft
from ferretera import Factura

def main(page: ft.Page):
    page.title = "Gestión de Ferreteria"
    facturas = []

    inputs = {
        "clave": ft.TextField(label="Clave"),
        "descripcion": ft.TextField(label="Descripcion"),
        "marca": ft.TextField(label="Marca"),
        "cantidad": ft.TextField(label="Cantidad"),
        "precio": ft.TextField(label="Precio"),         
    }

    precio_cargado = ft.TextField(visible=False)

    indice_modificar = ft.TextField(label="Índice de la Factura a Modificar (0-n)")

    output = ft.Text("")

    def agregar_factura(e):
        factura = Factura(
            inputs["clave"].value,
            inputs["descripcion"].value,
            inputs["marca"].value,
            int(inputs["cantidad"].value),
            float(inputs["precio"].value),
        )
        facturas.append(factura)
        output.value = f"Factura agregada en el índice {len(facturas)-1}:\n{str(factura)}"
        page.update()

    def modificar_factura(e):
        try:
            index = int(indice_modificar.value)
            if 0 <= index < len(facturas):
                factura = facturas[index]
                for k, v in inputs.items():
                    if v.value:
                        if k == 'cantidad':
                            setattr(factura, k, int(v.value))
                        elif k == 'precio':
                            setattr(factura, k, float(v.value))
                        else:
                            setattr(factura, k, v.value)
            
                precio_cargado.value = str(factura.calcular_factura())
                output.value = f"Factura modificada"
            else:
                output.value = "Índice fuera de rango."
        except ValueError:
            output.value = "Índice no válido. Introduzca un número entero."
        page.update()



    def cargar_factura(e):
        try:
            index = int(indice_modificar.value)
            if 0 <= index < len(facturas):
                factura = facturas[index]
                inputs["clave"].value = factura.clave
                inputs["descripcion"].value = factura.descripcion
                inputs["marca"].value = factura.marca
                inputs["cantidad"].value = factura.cantidad
                inputs["precio"].value = factura.precio
                precio_cargado.visible = True
                precio_cargado.value = str(factura.calcular_factura())
                output.value = f"Factura cargado del índice {index}."
            else:
                output.value = "Índice fuera de rango."
        except ValueError:
            output.value = "Índice no válido. Introduzca un número entero."
        page.update()

    def limpiar_campos(e):
        for v in inputs.values():
            v.value = ""
        indice_modificar.value = ""
        precio_cargado.visible = False
        output.value = ""
        page.update()

    def mostrar_todos(e):
        if facturas:
            resultado = "\n\n".join([f"Índice {i}:\n{str(factura)}" for i, factura in enumerate(facturas)])
        else:
            resultado = "No hay facturas registradas."
        output.value = resultado
        page.update()

    btn_agregar = ft.ElevatedButton("Agregar Factura", on_click=agregar_factura)
    btn_modificar = ft.ElevatedButton("Modificar Factura", on_click=modificar_factura)
    btn_cargar = ft.ElevatedButton("Cargar Factura", on_click=cargar_factura)
    btn_limpiar = ft.ElevatedButton("Limpiar Campos", on_click=limpiar_campos)
    btn_mostrar_todos = ft.ElevatedButton("Mostrar Todos las Facturas", on_click=mostrar_todos)

    page.add(
        *inputs.values(),
        precio_cargado,
        btn_agregar,
        ft.Row([indice_modificar, btn_cargar, btn_modificar, btn_limpiar, btn_mostrar_todos], spacing=10),
        output
    )

ft.app(target=main)
