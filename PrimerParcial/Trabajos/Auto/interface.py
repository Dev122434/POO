import flet as ft
from autos import Auto

def main(page: ft.Page):
    page.title = "Gestión de Autos"
    autos = []

    inputs = {
        "marca": ft.TextField(label="Marca"),
        "modelo": ft.TextField(label="Modelo"),
        "año": ft.TextField(label="Año"),
        "color": ft.TextField(label="Color"),
        "placa": ft.TextField(label="Placa"),
        "estado": ft.TextField(label="Estado"),
        "kilometraje": ft.TextField(label="Kilometraje"),
        "propietario": ft.TextField(label="Propietario"),
    }

    indice_modificar = ft.TextField(label="Índice del Auto a Modificar (0-n)")

    output = ft.Text("")

    def agregar_auto(e):
        auto = Auto(
            inputs["marca"].value,
            inputs["modelo"].value,
            inputs["año"].value,
            inputs["color"].value,
            inputs["placa"].value,
            inputs["estado"].value,
            inputs["kilometraje"].value,
            inputs["propietario"].value,
        )
        autos.append(auto)
        output.value = f"Auto agregado en el índice {len(autos)-1}:\n{str(auto)}"
        page.update()

    def modificar_auto(e):
        try:
            index = int(indice_modificar.value)
            if 0 <= index < len(autos):
                auto = autos[index]
                for k, v in inputs.items():
                    if v.value:
                        setattr(auto, k, v.value)
                output.value = f"Auto modificado en el índice {index}:\n{str(auto)}"
            else:
                output.value = "Índice fuera de rango."
        except ValueError:
            output.value = "Índice no válido. Introduzca un número entero."
        page.update()

    def cargar_auto(e):
        try:
            index = int(indice_modificar.value)
            if 0 <= index < len(autos):
                auto = autos[index]
                # Cargar los atributos en los TextField
                inputs["marca"].value = auto.marca
                inputs["modelo"].value = auto.modelo
                inputs["año"].value = auto.año
                inputs["color"].value = auto.color
                inputs["placa"].value = auto.placa
                inputs["estado"].value = auto.estado
                inputs["kilometraje"].value = auto.kilometraje
                inputs["propietario"].value = auto.propietario
                output.value = f"Auto cargado del índice {index}."
            else:
                output.value = "Índice fuera de rango."
        except ValueError:
            output.value = "Índice no válido. Introduzca un número entero."
        page.update()

    def limpiar_campos(e):
        for v in inputs.values():
            v.value = ""
        indice_modificar.value = ""
        output.value = ""
        page.update()

    def mostrar_todos(e):
        if autos:
            resultado = "\n\n".join([f"Índice {i}:\n{str(auto)}" for i, auto in enumerate(autos)])
        else:
            resultado = "No hay autos registrados."
        output.value = resultado
        page.update()

    btn_agregar = ft.ElevatedButton("Agregar Auto", on_click=agregar_auto)
    btn_modificar = ft.ElevatedButton("Modificar Auto", on_click=modificar_auto)
    btn_cargar = ft.ElevatedButton("Cargar Auto", on_click=cargar_auto)
    btn_limpiar = ft.ElevatedButton("Limpiar Campos", on_click=limpiar_campos)
    btn_mostrar_todos = ft.ElevatedButton("Mostrar Todos los Autos", on_click=mostrar_todos)

    page.add(
        *inputs.values(),
        btn_agregar,
        ft.Row([indice_modificar, btn_cargar, btn_modificar, btn_limpiar, btn_mostrar_todos], spacing=10),
        output
    )

ft.app(target=main)
