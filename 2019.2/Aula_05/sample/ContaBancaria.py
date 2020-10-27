class ContaBancaria():

    def __init__(self, titular, nConta, agencia):

        self.titular = titular
        self.nConta = nConta
        self.agencia = agencia
        self.saldo = 0

    def depositar(self, valor):
        if valor > 0:
            self.saldo += valor
            print("Seu saldo atual é: R$ " + str(self.saldo))
        else:
            print("O valor de deposito é inválido...")

    def sacar(self, valor):
        if valor > 0 and valor <= self.saldo:
            self.saldo -= valor
            print("Seu saldo atual é: R$ " + str(self.saldo))
        else:
            print("O valor de saque é inválido...")

conta1 = ContaBancaria("Messih", 123, 456)
conta1.depositar(2500)
conta1.sacar(600)
conta1.depositar(789)
conta1.sacar(6789)
