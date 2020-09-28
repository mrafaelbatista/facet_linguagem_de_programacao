#Variável com (path + nome do arquivo)
path = './path_file_sample/'
file = 'welcome_to_the_jungle.txt'
filename = path + file

#Pulando linha
# with open(filename) as file_object:
#     for abacate in file_object:
#         print(abacate)

#Sem pular linha
with open(filename) as file_object:
    for linha in file_object:
        print(linha.rstrip())
