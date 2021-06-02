from random import randint
a = randint(1, 1000)
b = randint(1, 1000)
c = randint(1, 1000)
d = randint(1, 1000)
e = randint(1, 1000)
lista = (a, b, c, d, e)
print(lista)
print(f'O menor valor é: {sorted(lista)[0]}\nO maior valor é: {sorted(lista)[-1]}')
