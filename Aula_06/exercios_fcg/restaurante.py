class Restaurante():

    def __init__(self, nome_restaurante, tipo_cozinha):
        self.nome_restaurante = nome_restaurante
        self.tipo_cozinha = tipo_cozinha

    def descrever_restaurante(self):
        msg = "O restaurante " + self.nome_restaurante +\
                   " trabalha com a cozinha " + self.tipo_cozinha
        return msg

    def abrir_restaurante(self):
        msg = "O restaurante " + self.nome_restaurante + " está aberto!"
        return msg