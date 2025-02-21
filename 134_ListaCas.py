import random

listaNumeri = []
for i in range(10):
    listaNumeri.append(random.randint(1, 100))
print("Lista: ", listaNumeri)
print("Lista al contrario: ", listaNumeri[::-1])