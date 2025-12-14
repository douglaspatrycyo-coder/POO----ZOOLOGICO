from animal import Animal


class Ave(Animal):
def __init__(self, nome: str, idade: int, envergadura: float):
super().__init__(nome, idade)
self._envergadura = envergadura


def emitir_som(self):
return f"{self._nome} canta: Piu piu!"


def voar(self):
return f"{self._nome} está voando."
