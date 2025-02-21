import random

lista = []
for i in range(10):
    i = random.randint(1, 10)
    lista.append(i)
print(lista)

for i in lista:
    if i % 2 != 0:
        i = i * 2
print(lista)