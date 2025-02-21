import random

lista = []
prodotto = 1

for i in range(10):
    i = random.randint(1, 10)
    lista.append(i)
print("lista originale:", lista)

for j in lista:
    prodotto *= j
print("prodotto lista:", prodotto)