class Animal:
    def __init__(self, nome, cor, peso):
        self.nome = nome      
        self.cor = cor        
        self.peso = peso      

    def andar(self):
        print(f"{self.nome} está a andar")

    def correr(self):
        print(f"{self.nome} está a correr")


class Cao(Animal):
    def latir(self):
        print(f"{self.nome} está a ladrar")


class Gato(Animal):
    def miar(self):
        print(f"{self.nome} está a miar")


animal = Animal("Bicho", "cinzento", 8)
cao = Cao("Duke", "castanho", 10)
gato = Gato("Miaurawr", "branca", 4)

print(f"O animal chama-se {animal.nome}, é {animal.cor} e pesa {animal.peso} kg")
animal.andar()
animal.correr()

print(f"O cão chama-se {cao.nome}, é {cao.cor} e pesa {cao.peso} kg")
cao.andar()
cao.latir()

print(f"O gato chama-se {gato.nome}, é {gato.cor} e pesa {gato.peso} kg")
gato.correr()
gato.miar()
