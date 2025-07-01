import flet as ft
from mamifero import Mamifero

def main(page: ft.Page):
    # Crear los controles para la interfaz
    nombre = ft.TextField(label="Nombre del mamífero")
    edad = ft.TextField(label="Edad")
    alimentacion = ft.TextField(label="Alimentación")
    habitat = ft.TextField(label="Hábitat")
    peso = ft.TextField(label="Peso (kg)")
    estatura = ft.TextField(label="Estatura (cm)")
    temperatura = ft.TextField(label="Temperatura corporal")
    tipo_pelo = ft.TextField(label="Tipo de pelo")

    # Opciones del dropdown
    animales = ['Perro', 'Gato', 'Caballo']

    # Etiqueta para mostrar el resultado
    resultado_text = ft.Text("", size=18)
    
    # Crear un control de dropdown para seleccionar el animal
    def get_options():
        return [
            ft.DropdownOption(
                key=animal,  # Asignamos el 'key' que es el nombre del animal
                content=ft.Text(animal)  # El contenido será el texto que muestra la opción
            ) for animal in animales
        ]

    # Función para actualizar la interfaz según el valor seleccionado en el dropdown
    def dropdown_changed(e):
        selected_animal = e.control.selected_value  # Obtener el valor seleccionado
        
        # Mostrar diferentes campos según el animal seleccionado
        if selected_animal == 'Perro':
            resultado_text.value = "Seleccionaste un Perro. Ingrese sus datos."
        elif selected_animal == 'Gato':
            resultado_text.value = "Seleccionaste un Gato. Ingrese sus datos."
        elif selected_animal == 'Caballo':
            resultado_text.value = "Seleccionaste un Caballo. Ingrese sus datos."
        else:
            resultado_text.value = "Selecciona un animal."

        page.update()

    # Crear un Dropdown para elegir un animal
    dd = ft.Dropdown(
        label="Selecciona un animal",
        options=get_options(),
        on_change=dropdown_changed,
    )

    # Función para crear el mamífero basado en los datos ingresados
    def crear_mamifero(e):
        # Obtener el valor seleccionado del dropdown
        selected_animal = dd.selected_value
        
        if not selected_animal:
            resultado_text.value = "Por favor selecciona un animal primero."
            page.update()
            return
        
        # Crear una instancia de la clase Mamifero con los valores ingresados
        mamifero = Mamifero(
            edad.value, 
            alimentacion.value, 
            habitat.value, 
            nombre.value, 
            peso.value, 
            estatura.value, 
            temperatura.value, 
            tipo_pelo.value
        )

        # Mostrar el resultado del objeto Mamífero creado
        resultado_text.value = f"{selected_animal} {mamifero.nombre} creado con éxito.\n"
        resultado_text.value += f"Edad: {mamifero.edad}\n"
        resultado_text.value += f"Alimentación: {mamifero.alimentacion}\n"
        resultado_text.value += f"Hábitat: {mamifero.habitat}\n"
        resultado_text.value += f"Peso: {mamifero.peso} kg\n"
        resultado_text.value += f"Estatura: {mamifero.estatura} cm\n"
        resultado_text.value += f"Temperatura corporal: {mamifero.temperatura_corporal}°C\n"
        resultado_text.value += f"Tipo de pelo: {mamifero.tipo_pelo}"

        # Actualizar la interfaz
        page.update()

    # Agregar los controles a la página
    page.add(
        dd, nombre, edad, alimentacion, habitat, peso, estatura, temperatura, tipo_pelo,
        ft.ElevatedButton("Crear Mamífero", on_click=crear_mamifero),
        resultado_text
    )

# Iniciar la aplicación Flet
ft.app(target=main)
