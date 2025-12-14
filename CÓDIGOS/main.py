from zoologico import Zoologico
from leao import Leao
from elefante import Elefante
from ave import Ave


zoo = Zoologico("Zoo Central")


leao = Leao("Simba", 5, 0.8)
elefante = Elefante("Dumbo", 10, 5400)
ave = Ave("Loro José", 2, 1.2)


zoo.adicionar_animal(leao)
zoo.adicionar_animal(elefante)
zoo.adicionar_animal(nave)


zoo.listar_animais()
print("\nRotina diária:\n")
zoo.rotina_diaria()
