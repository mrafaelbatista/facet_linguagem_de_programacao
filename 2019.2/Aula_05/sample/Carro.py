class Carro():

    def __init__(self, modelo, ano_fab, ano_modelo):
        self.modelo = modelo
        self.ano_fab = ano_fab
        self.ano_modelo = ano_modelo
        self.odometro = 0

    def acelerar(self, km):

        if km > 0:
            self.odometro += km
            print("O carro acelerou!")
        else:
            print("Valor igual ou menor que zero!")


    def frear(self):
        print("O carro freou")

    def consumirCombustivel(self):
        print("O carro consumiu combustível")


# Criando um objeto do tipo carro
carro1 = Carro("Fusca", 1965, 1968)

#Imprimindo na tela o valor inicial do odometro
print("Odometro inicial:" + carro1.odometro)

#Pedindo um valor de km percorrido
km_andado = int(input("Quanto o seu carro andou?"))

#Executando o método acelerar
carro1.acelerar(km_andado)

#Imprimindo na tela o valor final do odometro
print(carro1.odometro)
