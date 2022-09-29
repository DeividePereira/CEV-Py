import random


def fatorial(num=1):  # show dentro do def e não é opcional
    """fatorial(n, show=False)
        # Calcula o fatorial de um número
        - N -> O número a ser calculado.
        - return -> O valor do fatorial de um número."""

    show = str(input('Deseja visualizar o cálculo?\033[40m[S/N]\033[m ')).strip().upper()[0]
    while show != 'S' and show != 'N':
        print('   \033[31mErro! Tente novamente.\033[m')
        show = str(input('Deseja visualizar o cálculo?\033[40m[S/N]\033[m ')).strip().upper()[0]

    calc = 1
    for c in range(num, 1, -1):
        calc *= c

    if show == 'S':
        for a in range(num, 1, -1):  # Acaba no 2
            num *= a
            print(f'{a}', end=' X ')
        print(f'1 = {calc}')  # Continua do 2

    else:
        print(f'O fatorial de {num} é {calc}.')


fatorial(int(input('\033[40mDigite um número para calcular o fatorial:\033[m ')))
print('-' * 50)

print('\033[40mCálculo do fatorial de algum número aleatório entre 3 e 25:\033[m')
fatorial(random.randint(3, 25))
