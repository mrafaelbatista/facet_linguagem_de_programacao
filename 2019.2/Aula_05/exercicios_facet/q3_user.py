class User():

    def __init__(self, primeiro_nome, sobrenome):
        self.primeiro_nome = primeiro_nome
        self.sobrenome = sobrenome
        self.email = "email@email.com"
        self.tel = "24 81120040"
        self.sexo = "Pouco"

    def descrever_usuario(self):
        nome = self.primeiro_nome + " " + self.sobrenome
        mensagem = "O sr(a) " + nome.title() + " faz "\
             + self.sexo + " sexo por dia"
        return mensagem
    
    def saudacao(self):
        mensagem = "Iaê blz? " + self.primeiro_nome.title()
        return mensagem