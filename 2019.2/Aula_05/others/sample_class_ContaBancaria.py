class ContaBancaria():

    def __init__(self, titular, num_conta, agencia):
        self.titular = titular
        self.num_conta = num_conta
        self.agencia = agencia
        self.saldo = 0

    def depositar(self, valor):
        if valor > 0:
            self.saldo += valor
            print("Seu saldo é : R$ " + str(self.saldo))
        else:
            print(self.titular.title() + " , você é um liso.")

    def sacar(self, valor):
        if self.saldo > 0 and self.saldo >= valor:
            self.saldo -= valor
            print(self.titular.title() + " seu saldo atual é R$ "
                  + str(self.saldo))
        else:
            print("Valor excedido do limite.")


conta1 = ContaBancaria("Junior Oswaldo", 123456, 7894)

conta1.depositar(8000)
conta1.sacar(3458)