class Animal:   

    def __init__(self, nome, idade):

        self.nome = nome 
        self.idade = idade

    def barulho(self):
        print(f"O {self.nome} esta fazendo barulho")

class Bicho(Animal):

    def __init__(self, nome, idade, especie, som):

        #posso colocar super(). para os atributos iguas de outra classe
        super().__init__(nome, idade)

        self.especie = especie
        self.som_bicho = som

    def fazer_som(self):
         print(f"O {self.nome} está fazendo {self.som_bicho}")


meu_animal = Bicho("patonildo", 3, "ganso", "quack")

print(meu_animal.nome)
print(meu_animal.idade)
print(meu_animal.especie)
meu_animal.barulho()
meu_animal.fazer_som()