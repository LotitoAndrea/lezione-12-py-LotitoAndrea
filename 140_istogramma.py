import random

numeri = int(input("Inserisci un numero: "))
lista = []
istogramma = ""
for i in range(numeri):
    i = random.randint(1, 10)
    lista.append(i)
print("lista originale:", lista)
for j in range(len(lista)):
    istogramma += "*" * lista[j] + "\n"
print(istogramma)