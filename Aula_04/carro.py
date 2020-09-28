class Carro():

    def __init__(self, modelo, fabricante, ano):
        self.modelo = modelo
        self.fabricante = fabricante
        self.ano = ano
    
    def acelerar(self):
        print(self.modelo + ' está acelerando.')

    def frear(self):
        print(self.modelo + ' está freando.')

class Carro_Eletrico(Carro):

    def __init__(self, modelo, fabricante, ano):
        super().__init__(modelo, fabricante, ano)
        self.bateria = 100
    
    def acelerar(self):
        print('ESTE TEXTO É DIFERENTE DA CLASSE CARRO')

carro_eletrico = Carro_Eletrico('tesla', 'tesla', '2020')

carro_eletrico.acelerar()
carro_eletrico.frear()