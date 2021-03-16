""" fatorial com repetição while - desafio060 com menu """
from time import sleep

print('==-== \033[36mCálculo de Fatorial\033[m ==-==')
num = int(input('Digite um número inteiro: '))
a = 0
c = num
f = fat = 1
print(f'\033[36m{c}!\033[m = ', end='')
while c > 0:
    print(f'{c}', end='')
    print(f' x ' if c > 1 else ' = ', end='')
    f *= c
    c -= 1
print(f'\033[36m{f}\033[m')

while not a == 2:
    print('\033[7;40m[1]\033[m Novo número\n\033[7;40m[2]\033[m Fechar')
    a = int(input('Sua escolha: '))

    if a == 1:
        n = int(input('Digite um número inteiro: '))
        print(f'\033[36m{n}!\033[m = ', end='')
        c2 = n
        while c2 > 0:
            print(f'{c2}', end='')
            print(' x ' if c2 > 1 else ' = ', end='')
            fat *= c2
            c2 -= 1
        print(f'\033[36m{fat}\033[m')
        sleep(1)

    if a < 1 or a > 2:
            print('Valor inválido, tente novamente.')

    if a == 2:
        print('\n\033[36mFinalizando...\033[m')
        sleep(1)
        a = 2
