def count_words(filename):
    """Conta o número de palavras de um arquivo"""
    try:
        with open(filename) as f_obj:
            conteudo = f_obj.read()
    except FileNotFoundError:
        msg = "O arquivo %s não foi encontrado." % filename
        print(msg)
    else:
        palavras = conteudo.split()
        num_palavras = len(palavras)
        print("O arquivo %s tem um valor em torno de %d de palavras" % (filename, num_palavras))
