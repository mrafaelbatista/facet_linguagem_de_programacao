class Carro():

    def __init__(self, fabricante, ano, modelo):
        self.fabricante = fabricante
        self.ano = ano
        self.modelo = modelo

    def acelerar(self):
        print(self.fabricante + ' - ' + self.modelo +  ' acelerou!')
    
    def frear(self):
        print('Este carro brekou!')


fiat_vivace = Carro('Fiat', 2010, 'Vivace')
reanult_sandero = Carro('Renault', 2016, 'Sandero')
ferrari = Carro('Ferrari', 2020, 'Ferrari 360')

fiat_vivace.acelerar()
reanult_sandero.acelerar()
ferrari.acelerar()

fiat_vivace.frear()
