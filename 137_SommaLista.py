import random

numero = int(input("Inserisci un numero: "))
lista = []
for i in range(numero):
    i = random.randint(1, 20)
    lista.append(i)
print("lista originale:", lista)
print("somma lista:", sum(lista))