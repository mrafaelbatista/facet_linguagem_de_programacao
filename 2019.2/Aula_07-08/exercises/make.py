from cliente import Cliente
from banco import Banco

cli1 = Cliente("Miguel", "06458963245", "83996098456")
agencia = Banco()
agencia.criar_conta(cli1)
print(agencia.contas)