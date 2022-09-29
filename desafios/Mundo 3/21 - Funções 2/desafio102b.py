import random


def fatorial2(num, show='N'):  # show fora do def e é opcional.
    """fatorial(n, show=False)
        # Calcula o fatorial de um número
        - N -> O número a ser calculado.
        - return -> O valor do fatorial de um número."""

    calc = 1
    for c in range(num, 1, -1):
        calc *= c

    if show == 'S':
        for a in range(num, 1, -1):
            num *= a
            print(f'{a}', end=' X ')
        print(f'1 = {calc}')

    else:
        print(f'O fatorial de {num} é {calc}.')


print('\033[40mCálculo do fatorial de algum número aleatório entre 3 e 25:\033[m')
fatorial2(random.randint(3, 25), 'S')
print('-' * 50)

fat = int(input('\033[40mDigite um número para calcular o fatorial:\033[m '))
visualizar = str(input('Deseja visualizar o cálculo?\033[40m[S/N]\033[m ')).strip().upper()[0]
while visualizar != 'S' and visualizar != 'N':
    print('   \033[31mErro! Tente novamente.\033[m')
    visualizar = str(input('Deseja visualizar o cálculo?\033[40m[S/N]\033[m ')).strip().upper()[0]
fatorial2(fat, visualizar)
