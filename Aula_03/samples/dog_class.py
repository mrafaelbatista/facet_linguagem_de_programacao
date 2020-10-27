class Dog():

    def __init__(self, nome, idade, raca, cor_do_pelo):
        self.nome = nome
        self.idade = idade
        self.raca = raca
        self.cor_do_pelo = cor_do_pelo

    def sentar(self):
        print(self.nome.title() + " agora está sentado")
    
    def rolar(self):
        print(self.nome.title() + " rolou para próximo de você!")