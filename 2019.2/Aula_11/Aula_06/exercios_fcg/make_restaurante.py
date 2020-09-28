from restaurante import Restaurante

rest1 = Restaurante("Feijoada do Negão", "Brasileira")
print(rest1.nome_restaurante)
print(rest1.tipo_cozinha)
print(rest1.descrever_restaurante())
print(rest1.abrir_restaurante())

rest2 = Restaurante("Matsu", "Oriental")
print(rest2.descrever_restaurante())

rest3 = Restaurante("Buraco da Gia", "Frutos do Mar")
print(rest3.descrever_restaurante())