from math import factorial
from time import sleep
print('==-== \033[36mCálculo de Fatorial\033[m ==-==')
a = 0

n = int(input('Digite um número inteiro: '))
print(f'{n}! = {factorial(n)}')
sleep(1)

while not a == 2:
    print('\033[7;40m[1]\033[m Novo número\n\033[7;40m[2]\033[m Fechar')
    a = int(input('Sua escolha: '))
    if a == 1:
        n = int(input('Digite um número inteiro: '))
        print(f'{n}! = {factorial(n)}')
        sleep(1)

    if a == 2:
        print('Finalizando...')
        sleep(1)
        a = 2

    if a < 1 or a > 2:
        print('Valor inválido, tente novamente.')
