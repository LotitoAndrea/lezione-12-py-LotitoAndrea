import random

lista = []
for i in range(10):
    numeri = random.randint(1, 10)
    lista.append(numeri)
print("lista originale:", lista)

media = sum(lista) / len(lista)
print("media lista:", media)
lista = [num for num in lista if num >= media]
print("lista modificata:", lista)
