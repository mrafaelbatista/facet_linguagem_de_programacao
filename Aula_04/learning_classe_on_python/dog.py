class Dog():
    """""Modelando um Cachorro"""


    def __init__(self, nome, idade):
        self.nome = nome
        self.idade = idade

    def sentar(self):
        print(self.nome.title() + " agora está sentado")

    def rolar(self):
        print(self.nome.title() + " rolou para próximo de você!")