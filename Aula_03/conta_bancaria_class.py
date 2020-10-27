class Conta():

    def __init__(self, titular, numero_conta, agencia, saldo):
        self.titular = titular
        self.numero_conta = numero_conta
        self.agencia = agencia
        self.saldo = saldo

    def depositar(self, valor_dep):
        self.saldo = self.saldo + valor_dep
        print('Saldo: ' + str(self.saldo))
    
    def sacar(self, valor_saq):
        if valor_saq > self.saldo:
            print('Valor superior ao disponível!')
            print('Seu saldo é: ' + str(self.saldo))
        else:
            self.saldo = self.saldo - valor_saq
            print('Seu saldo é: ' + str(self.saldo))