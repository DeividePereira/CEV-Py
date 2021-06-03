from random import randint
n = (randint(1, 1000), randint(1, 1000), randint(1, 1000), randint(1, 1000), randint(1, 1000))
print(n)
print(f'O menor valor é: {sorted(n)[0]}\nO maior valor é: {sorted(n)[-1]}')
