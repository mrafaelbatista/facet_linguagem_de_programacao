file_name = './path_file_sample/welcome_to_the_jungle.txt'

with open(file_name) as file_object:
    linhas = file_object.readlines()

for linha in linhas:
    print(linha.rstrip())


