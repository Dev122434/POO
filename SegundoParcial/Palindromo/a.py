import os
os.system("cls")
import flet as ft

class Palindromo:
    def _init_(self, cadena):
        self.cadena = cadena

    def convertir_a_lista(self):
        return list(self.cadena)

    def eliminar_espacios_de_cadena(self):
        return [c for c in self.cadena if c != " "]

    def eliminar_espacios_y_voltear_lista(self, lista):
        lista3 = [c for c in lista if c != " "]
        lista3.reverse()
        return lista3

    def es_palindromo(self, lista_reversa):
        lista_original = [c for c in self.cadena if c != " "]
        if lista_original == lista_reversa:
            return "Sí es un palíndromo"
        else:
            return "No es un palíndromo"