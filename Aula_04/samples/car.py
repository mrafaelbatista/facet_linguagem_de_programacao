class Carro():

    def __init__(self, fabricante, modelo, ano):
        self.fabricante = fabricante
        self.modelo = modelo
        self.ano = ano
    
    def descrever_nome(self):
        mensagem = "{} - {}, {}".format(self.ano, self.fabricante, self.modelo)
        print(mensagem)

class CarroEletrico(Carro):

    def __init__(self, fabricante, modelo, ano):
        super().__init__(fabricante, modelo, ano)
        self.bateria = Bateria()