class Palindromo():
    def __init__(self, frase: str):
        self.frase = frase

    def __str__(self):
        return f'{self.frase}'
    
    def convertir_lista(self) -> list[str]:
        self.list_text = self.frase.split().copy()
        return self.list_text
    
    def eliminar_espacios(self) -> list[str]:
        self.copy_text: list[str] = list()
        for item in self.list_text:
            if item != '':
                self.copy_text.append(item)
        return self.copy_text
     

    def is_palindromo(self) -> str:
        if (len(self.list_text) == len(self.copy_text)):
            for i in range(len(self.list_text)):
                if self.list_text[i] != self.copy_text[i]:
                    return 'No es palindromo'
            return 'Es palindromo'
        else:
            return 'No es palindromo'
    