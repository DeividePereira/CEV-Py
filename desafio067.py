from time import sleep
print('==-== \033[34mTabuada\033[m ==-==')
print(f'\033[40mDigite um número negativo para parar o programa!\033[m')
while True:
    n = int(input('Digite o \033[34mnúmero inteiro\033[m que deseja a tabuada: '))
    if n < 0:
        break

    print(f'==-== \033[36mTabuada de {n}\033[m ==-==')
    for v in range(1, 11, 1):
        print(f'{n} x {v:^2} = \033[36m{n * v:^3}\033[m')
print('\033[40mFinalizando...\033[m')
sleep(1)
print('=-=-=-='*5)
