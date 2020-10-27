class Restaurante():
    def __init__(self, restaurant_name, cuisine_type):
        self.restaurant_name=restaurant_name
        self.cuisine_type =cuisine_type
    def describe_restaurant(self):
        print(self.restaurant_name.title() + str(self.cuisine_type))
    def open_restaurant(self):
        print("O restaurante está aberto:" )
restaurante1=Restaurante("Du japonei", "Churrasco")

print(restaurante1.restaurant_name)

print(restaurante1.cuisine_type)

restaurante1.open_restaurant()

restaurante1.describe_restaurant()

restaurante2=Restaurante("Du chinei", "frutos do mar")

restaurante2.describe_restaurant()

restaurante3=Restaurante("Du Negão", "Doce de banana")

restaurante3.describe_restaurant()

restaurante4=Restaurante("Du nena", "goiabada")

restaurante4.describe_restaurant()
