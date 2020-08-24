# filename = 'alice.txt'
#
# with open(filename) as f_obj:
#     conteudo = f_obj.read()

#Corrigindo com Exceptions
filename2 = 'bible.txt'

try:
    with open(filename2) as f_obj:
        conteudo = f_obj.read()
except FileNotFoundError:
    print("Desculpe, o arquivo %s não foi encontrado." % filename2)


