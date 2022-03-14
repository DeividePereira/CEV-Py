import random
r = random.randint(1, 5)
n = int(input('Digite um número inteiro entre 0 e 5: '))
if r == n:
    print('Você ganhou!')
else:
    print('Você não ganhou! Tente novamente.')
if n > 10:
    print('Você deve digitar um número menor, entre 0 e 10!')
if n < 0:
    print('Você deve digitar um número maior, entre 0 e 10!')
