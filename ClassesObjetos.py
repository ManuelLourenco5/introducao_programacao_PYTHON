class Pessoa:
    def __init__(self, nome, idade):
        self.nome = nome
        self.idade = idade
    def cumprimentar(self):
        print(f"ola, o meu nome e {self.nome} e tenho {self.idade} anos")