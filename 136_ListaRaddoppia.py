import random

lista = []
for i in range(10):
    i = random.randint(1, 10)
    lista.append(i)
print("lista originale:", lista)

for j in range(len(lista)):
    if lista[j] % 2 != 0:
        lista[j] = lista[j] * 2
print("lista modificata:", lista)