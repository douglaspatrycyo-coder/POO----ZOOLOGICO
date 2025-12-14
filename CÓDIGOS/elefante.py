from animal import Animal


class Elefante(Animal):
def __init__(self, nome: str, idade: int, peso: float):
super().__init__(nome, idade)
self._peso = peso


def emitir_som(self):
return f"{self._nome} Prrrr!"


def tomar_banho(self):
return f"{self._nome} está tomando banho."
