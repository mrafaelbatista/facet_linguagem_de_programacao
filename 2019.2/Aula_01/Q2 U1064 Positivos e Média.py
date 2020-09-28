from random import randint
lista = []
media = 0
positivos = 0

for i in range(0,6):
    lista.append(randint(-50, 50))

print(lista)

for item in lista:
    if item > 0 :
        positivos += 1

    media += item

print(positivos)
print(media/len(lista))