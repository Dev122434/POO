class Palindromo():
    # Constructor
    def __init__(self, frase: str):
        self.frase = frase
        self.list_text: list[str] = list()
        self.copy_text: list[str] = list()

    # Metodo para imprimir el valor del objeto
    def __str__(self):
        return f'{self.frase}'
    
    # Metodo para convertir una lista
    def convertir_lista(self) -> list[str]:
        for item in self.frase:
            self.list_text.append(item)
        return self.list_text
    
    # Metodo para eliminar espacios y retornar el resultado en formato lista
    def eliminar_espacios(self) -> list[str]:
        for item in self.list_text:
            if not item == ' ':
                self.copy_text.append(item)
        return self.copy_text
    
    def is_palindromo(self) -> str:
        self.copy_text = self.frase[::-1]
        if len(self.list_text) == len(self.copy_text):
            for i in range(len(self.list_text)):
                if not (self.list_text[i] == self.el):
                    return 'No es palindromo'
        else:
            return 'No es palindromo'