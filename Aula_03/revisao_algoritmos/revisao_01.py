# Vamos criar uma lista de nomes e depois
# vamos imprimir essa lista, apenas para
# relembrar os conceitos de programação

# Criando lista
lista_de_nomes = []
x = 1
while x != 0:
    nome = input('Digite um nome para a sua lista: ')
    lista_de_nomes.append(nome.upper())

    print('Deseja adicionar um novo nome na lista?')
    exit = int(input('1 - Sim\n0 - Não\n' ))
    if exit == 0:
        x = 0

for nome in lista_de_nomes:
    print(nome)