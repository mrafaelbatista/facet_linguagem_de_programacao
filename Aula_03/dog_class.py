# Criando a classe cachorro

class Dog():

    def __init__(self, nome, idade, raca):
        self.nome = nome
        self.idade = idade
        self.raca = raca
    
    def andar(self):
        print(self.nome + ' está andando.')
    
    def correr(self):
        print(self.nome + ' está correndo.')
    
    def aumentar_idade(self):
        self.idade = self.idade + 1
    
    def verificar_idade(self):
        print(self.nome + ' tem ' + str(self.idade) + ' anos.' )