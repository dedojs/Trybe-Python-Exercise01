from personagem import Personagem
from jedi_sith import Jedi, Sith


personagem_1 = Personagem("Padmé", 'Humana', 50, 165, 40)

personagem_2 = Jedi("Luke", "Humano", 60, 170, 200)
personagem_3 = Sith("Vader", "Humano", 100, 200, 200)

print("Batalha Inicia")
print('-------------')

while personagem_3.get_hp() > 0:
    print(f" -> {personagem_2.nome} e {personagem_2.get_hp()}")
    print(f" -> {personagem_3.nome} e {personagem_3.get_hp()}")
    print('-------------')
    personagem_3.atacar(personagem_2)

    if personagem_2.get_hp() > 0:
        personagem_2.contra_atacar(personagem_3)
    else:
        print('Sith venceu')
        break

else:
    print("Jedi Wins")
  