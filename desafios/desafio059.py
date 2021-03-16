import time
menu = 0
a = float(input('\033[30;47mDigite um valor:\033[m '))
b = float(input('\033[30;47mDigite outro valor:\033[m '))

while menu != 5:
    print('\n\033[7;40m[1]\033[m Somar\n\033[7;40m[2]\033[m Multiplicar\n\033[7;40m[3]\033[m Maior\n', end="")
    print('\033[7;40m[4]\033[m Novos números\n\033[7;40m[5]\033[m Sair do programa')
    typed = int(input('Selecione: '))

    if typed < 1 or typed > 5:
        print('Valor inválido, tente novamente.')

    elif typed == 1:
        print(f'{a} \033[31m+\033[m {b} = \033[31m{a + b}\033[m')
        time.sleep(1)

    elif typed == 2:
        print(f'{a} \033[34m*\033[m {b} = \033[32m{a * b}\033[m')
        time.sleep(1)

    elif typed == 3:
        if a > b:
            print(f'{a} \033[33m>\033[m {b}')
        elif a == b:
            print(f'{a} \033[33m=\033[m {b}')
        else:
            print(f'{b} \033[33m>\033[m {a}')
        time.sleep(1)

    elif typed == 4:
        a = float(input('\033[30;47mDigite um novo valor:\033[m '))
        b = float(input('\033[30;47mDigite outro novo valor:\033[m '))
        time.sleep(1)

    elif typed == 5:
        menu = 5
        print('\033[4;36mAgradeçemos a preferência! Tenha um dia classe A-1!\033[m')
        time.sleep(1)
