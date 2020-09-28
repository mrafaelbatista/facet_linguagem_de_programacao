class Carro():

    def __init__(self, modelo, ano_fabricacao, ano_modelo, tanque):
        self.modelo = modelo
        self.ano_fabricacao = ano_fabricacao
        self.ano_modelo = ano_modelo
        self.tanque = tanque
    
    def acelerar(self):
        print('O carro está ACELERANDO.')

    def frear(self):
        print('O carro está FREANDO.')
    
    def consumir_combustivel(self, gasto_de_combustivel):
        self.tanque = self.tanque - gasto_de_combustivel
        print(self.tanque)