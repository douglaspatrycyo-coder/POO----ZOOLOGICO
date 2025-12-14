class Animal:
def __init__(self, nome: str, idade: int):
self._nome = nome
self._idade = idade


def get_nome(self):
return self._nome


def get_idade(self):
return self._idade


def dormir(self):
return f"{self._nome} está dormindo."


def emitir_som(self):
return "Som indefinido"
