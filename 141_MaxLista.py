import random

lista = []
for i in range(20):
    i = random.randint(1, 100)
    lista.append(i)
print("lista originale:", lista)
print("numero massimo:", max(lista))