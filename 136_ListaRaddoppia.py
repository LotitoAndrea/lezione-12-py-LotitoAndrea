import random

lista = []
for i in range(10):
    i = random.randint(1, 10)
    lista.append(i)

for i in lista:
    if i % 2 != 0:
        lista[i] = lista[i] * 2
print(lista)