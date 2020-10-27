from random import randint
from cliente import Cliente

class Banco():

    def __init__(self, contas={}):
        self.contas = contas
        self.saldo = 0
    
    def calcular_saldo(self, operacao, valor):
        if valor > 0:
            #Depósito do banco
            if operacao == 1:
                self.saldo += valor
            #Saque do banco
            elif operacao == 2 and valor <= self.saldo:
                self.saldo -= valor
        else:
            print("O valor digitado inválido.")
    
    def criar_conta(self, cliente):
        nova_conta = randint(1000, 9999)
        self.contas[nova_conta] = [cliente.nome, cliente.cpf, cliente.telefone]
        print(self.contas[nova_conta][0])
