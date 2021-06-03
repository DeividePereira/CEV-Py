from random import randint
n = (randint(1, 1000), randint(1, 1000), randint(1, 1000), randint(1, 1000), randint(1, 1000))
print('Os valores sorteados foram: ', end='')
for num in n:
    print(f'{num} ', end='')
print(f'\nO menor valor é: {min(n)}\nO maior valor é: {max(n)}')
