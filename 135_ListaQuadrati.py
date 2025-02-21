import random

numeri = int(input("Inserisci un numero: "))
lista = []
for i in range(numeri):
    i = random.randint(1, 20)
    lista.append(i)
print(lista)
for i in lista:
    print(i**2, end=", ")