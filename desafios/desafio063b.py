"""Feito por luis"""

n = int(input("numero: "))

lista = [1, 1]

for i in range(n-2):
      lista.append(lista[-1]+lista[-2])

print(lista)
