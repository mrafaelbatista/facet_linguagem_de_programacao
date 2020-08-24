from q1_restaurante import RestauranteQuatro

restaurante = RestauranteQuatro("Vicktor Akiba", "Mexicana")

restaurante.descrever_restaurante()
restaurante.abrir_restaurante()

print(restaurante.num_servidos)
restaurante.num_servidos = 10
print(restaurante.num_servidos)