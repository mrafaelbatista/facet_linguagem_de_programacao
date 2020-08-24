from q1_restaurante import Restaurante

class Lanchonete(Restaurante):

    def __init__(self, nome, tipo, cardapio):
        super().__init__(nome, tipo)
        self.cardapio = cardapio

    def mostrar_cardapio(self):
        for prato in self.cardapio:
            print(" - " + prato)
