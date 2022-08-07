from time import sleep
brasileirao = ('Palmeiras', 'Flamengo', 'Internacional', 'Grêmio', 'São Paulo', 'Atlético Mineiro', 'Atlético-PR',
               'Cruzeiro', 'Botafogo', 'Santos', 'Bahia', 'Corinthians', 'Fluminense', 'Ceará', 'Vasco da Gama',
               'Sport Recife', 'América-MG', 'Chapecoense', 'Vitória', 'Paraná')
print(f'\n{" Brasileirão 2018 ":=^30}')
while True:
    print('''Escolha uma das opções abaixo para exibir:
\033[40m[ A ]\033[m Os 5 primeiros colocados
\033[40m[ B ]\033[m Os últimos 4 colocados
\033[40m[ C ]\033[m Colocação em ordem alfabética
\033[40m[ D ]\033[m Em que posição o Chapecoense está
\033[40m[ E ]\033[m Sair''')
    opcao = str(input('Digite a opção desejada: ')).upper().strip()
    if opcao == 'A':
        for c in (brasileirao[0:5]):
            print(f'\033[43m{c}', end=', \033[m')
        print('\n\033[37mProcessando...\033[m')
    elif opcao == 'B':
        print(f'\033[31m{brasileirao[-4:]}\033[m')
        print('\033[37mProcessando...\033[m')
    elif opcao == 'C':
        print(f'{sorted(brasileirao)}')
    elif opcao == 'D':
        print(f'O Chapecoense está em \033[m{brasileirao.index("Chapecoense")+1}°\033[m lugar.')
    elif opcao == 'E':
        break
    else:
        print('\033[31mTente novamente!\033[m')
    sleep(1)
