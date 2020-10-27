from pessoa import Pessoa

class Cliente(Pessoa):

    def __init__(self, nome, cpf, telefone):
        super().__init__(nome, cpf)
        self.telefone = telefone