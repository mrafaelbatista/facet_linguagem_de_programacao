class Dog():
    """""Modelando um Cachorro"""

    def __init__(self, nome, idade, altura, raca, cor_do_pelo):
        self.nome = nome
        self.idade = idade
        self.altura = altura
        self.raca = raca
        self.cor_do_pelo = cor_do_pelo

    def sentar(self):
        print(self.nome.title() + " agora está sentado")

    def rolar(self):
        print(self.nome.title() + " rolou para próximo de você!")

    def pular(self):
        print(self.nome.title() + " pulou mais alto que " + str(self.altura))

cachorro_de_oswaldo = Dog("Preguiça", 114, 1.44, "Pug", "preto")

cachorro_de_oswaldo.sentar()
cachorro_de_oswaldo.rolar()
cachorro_de_oswaldo.pular()