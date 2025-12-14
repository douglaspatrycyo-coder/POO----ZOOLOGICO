from animal import Animal


class Leao(Animal):
def __init__(self, nome: str, idade: int, tamanho_juba: float):
super().__init__(nome, idade)
self._tamanho_juba = tamanho_juba


def emitir_som(self):
return f"{self._nome} Rooooar!"


def cacar(self):
return f"{self._nome} está caçando."
