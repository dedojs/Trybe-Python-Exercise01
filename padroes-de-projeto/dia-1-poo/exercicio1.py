class Eletrodomestico:
    def __init__(self, tipo, cor, potencia, voltagem, preco):
        self.tipo = tipo
        self.preco = preco
        self.__cor = cor
        self.potencia = potencia
        self.voltagem = voltagem
        self.__ligado = False
        
    def ligar(self):
        self.ligado = True

    def desligar(self):
        self.ligado = False

    @property
    def cor(self):
        return self.__cor

    @cor.setter
    def cor(self, nova_cor):
        self.cor = nova_cor

    def __str__(self):
      return f"Eletrodomestico: {self.tipo}, Cor: {self.cor}, Preço: {self.preco}"
     


class Pessoa:
    def __init__(self, nome, saldo):
        self.nome = nome
        self.saldo = saldo
        self.eletrodomestico = []

    def comprar_eletrodomestico(self, eletrodomestico: Eletrodomestico):
        if eletrodomestico.preco <= self.saldo:
            self.saldo -= eletrodomestico.preco
            self.eletrodomestico.append(eletrodomestico.tipo)

    def __str__(self):
        if (self.eletrodomestico):
            return f"{self.nome} - Eletrodomésticos: {self.eletrodomestico}"
        return f"{self.nome} - não possui um eletrodomestico"


class Geladeira(Eletrodomestico):
    def __init__(self, tipo, cor, potencia, voltagem, preco, portas):
        super().__init__(tipo, cor, potencia, voltagem, preco)
        self.portas = portas
    
    def __str__(self):
        return f"Geladeira, {self.cor}, R$ {self.preco},00"


class Microondas(Eletrodomestico):
    def __init__(self, tipo, cor, potencia, voltagem, preco, marca):
        super().__init__(tipo, cor, potencia, voltagem, preco)
        self.marca = marca

    def __str__(self):
        return f"Microondas, {self.cor}, R$ {self.preco},00, marca: {self.marca}"


class Fogao(Eletrodomestico):
    def __init__(self, tipo, cor, potencia, voltagem, preco, bocas):
        super().__init__(tipo, cor, potencia, voltagem, preco)
        self.bocas = bocas
    
    def __str__(self):
        return f"Fogão, {self.cor}, R$ {self.preco},00, quantidade de bocas: {self.bocas}"


class Batedeira(Eletrodomestico):
    def __init__(self, tipo, cor, potencia, voltagem, preco, velocidade):
        super().__init__(tipo, cor, potencia, voltagem, preco)
        self.velocidade = velocidade
    
    def __str__(self):
        return f"Batedeira, {self.cor}, R$ {self.preco},00, velocidade: {self.velocidade}"

geladeira_azul = Geladeira('Geladeira', 'Branca', 1000, 220, 500, 2)
microondas_vermelho = Microondas('Microondas', 'Vermelho', 1000, 220, 600, 'Panasonic')
fogao_azul = Fogao('Fogao', 'Azul', 200, 220, 700, 6)
batedeira_amarela = Batedeira('Batedeira', 'Amarela', 500, 220, 300, 12)

pessoa_cozinheira = Pessoa('Juvenal', 2000)
pessoa_cozinheira.comprar_eletrodomestico(geladeira_azul)
pessoa_cozinheira.comprar_eletrodomestico(batedeira_amarela)
pessoa_cozinheira.comprar_eletrodomestico(microondas_vermelho)
pessoa_cozinheira.comprar_eletrodomestico(fogao_azul)

print(geladeira_azul)
print(microondas_vermelho)
print(fogao_azul)
print(batedeira_amarela)

print(pessoa_cozinheira)





