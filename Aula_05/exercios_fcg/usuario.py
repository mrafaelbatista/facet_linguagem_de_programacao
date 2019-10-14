class Usuario():

    def __init__(self, primeiro_nome, ultimo_nome,\
         idade, sexo, cpf):

        self.primeiro_nome = primeiro_nome
        self.ultimo_nome = ultimo_nome
        self.idade = idade
        self.sexo = sexo
        self.cpf = cpf
    
    def descrever_usuario(self):
        nome_completo = self.primeiro_nome + " " + self.ultimo_nome
        
        msg = "Seu nome é " + nome_completo +\
            " , e sua idade é " + str(self.idade) +\
            " você é do sexo " + self.sexo + " e tem o cpf "\
                + str(self.cpf)

        return msg

    def saudacao_usuario(self):
        msg = "Olá " + self.primeiro_nome + "!"
