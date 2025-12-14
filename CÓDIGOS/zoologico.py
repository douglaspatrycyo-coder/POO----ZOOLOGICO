from animal import Animal


class Zoologico:
def __init__(self, nome: str):
self._nome = nome
self._animais = [] 


def adicionar_animal(self, animal: Animal):
self._animais.append(animal)


def listar_animais(self):
for animal in self._animais:
print(f"- {animal.get_nome()} ({animal.__class__.__name__})")


def rotina_diaria(self):
for animal in self._animais:
print(animal.emitir_som())
print(animal.dormir())
