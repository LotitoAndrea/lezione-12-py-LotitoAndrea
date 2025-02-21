import random

numero = int(input("Inserisci un numero: "))
lista = []
for i in range(numero):
    i = random.randint(1, 20)
    lista.append(i)
print("lista originale:", lista)
print("numeri pari: ", sum(1 for i in lista if i % 2 == 0))
print("numeri dispari: ", sum(1 for i in lista if i % 2 != 0))