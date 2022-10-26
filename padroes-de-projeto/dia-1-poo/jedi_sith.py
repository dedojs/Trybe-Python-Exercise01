from personagem import Personagem;
from light_saber import SabreDeLuz;
from random import choice


class Jedi(Personagem):
    def __init__(self, nome, especie, peso, altura, hp):
        super().__init__(nome, especie, peso, altura, hp)
        self.sabre = SabreDeLuz('Verde', 20)

    def defender(self):
        defesa = choice([True, False])
        if defesa:
            print(f"{self.nome} defendeu com sucesso!")
            return defesa

    def contra_atacar(self, personagem):
        print(f"{self.nome} contra atacou com sucesso!")
        personagem.damage_hp(self.sabre.forca)

    def falar(self):
        return "Que a força esteja com você!"



class Sith(Personagem):
    def __init__(self, nome, especie, peso, altura, hp):
        super().__init__(nome, especie, peso, altura, hp)
        self.sabre = SabreDeLuz('Vermelho', 40)

    def atacar(self, personagem):
      if not personagem.defender():
          print(f"{self.nome} atacou com sucesso!")
          personagem.damage_hp(self.sabre.forca)

    def falar(self):
        return "Venha para o ladro Negro da força!"