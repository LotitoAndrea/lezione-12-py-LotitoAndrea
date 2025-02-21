import random

numero = int(input("Inserisci un numero: "))
lista = []
for numeri in range(numero):
    numeri = random.randint(-20, 20)
    lista.append(numeri)

print("lista originale:", lista)
print("somma lista positivi:", sum(numeri for numeri in lista if numeri >= 0))
print("somma lista negativi:", sum(numeri for numeri in lista if numeri < 0))