class Restaurante():

    def __init__(self, nome_restaurante, tipo_cozinha):
        self.nome_restaurante = nome_restaurante
        self.tipo_cozinha = tipo_cozinha

    def descrever_restaurante(self):
        print("O restaurante " + self.nome_restaurante
              + " trabalha com o tipo de cozinha "
              + self.tipo_cozinha)

    def abrir_restaurante(self):
        print("O restaurante " + self.nome_restaurante
              + " está aberto!")

class RestauranteQuatro():

    def __init__(self, nome_restaurante, tipo_cozinha, num_servidos=0):
        self.nome_restaurante = nome_restaurante
        self.tipo_cozinha = tipo_cozinha
        self.num_servidos = num_servidos

    def descrever_restaurante(self):
        print("O restaurante " + self.nome_restaurante
              + " trabalha com o tipo de cozinha "
              + self.tipo_cozinha)

    def abrir_restaurante(self):
        print("O restaurante " + self.nome_restaurante
              + " está aberto!")