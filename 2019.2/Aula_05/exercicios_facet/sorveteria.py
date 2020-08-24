from q1_restaurante import Restaurante

class Sorveteria(Restaurante):

    def __init__(self, nome_restaurante, tipo_cozinha, sabores):
        super().__init__(nome_restaurante, tipo_cozinha)
        self.sabores = sabores

    def mostrar_sabores(self):
        return self.sabores

    def mostrar_sabores2(self, lsabores):
        return lsabores
