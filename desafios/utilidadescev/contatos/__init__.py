def titulo_centralizado(mensagem, vezes, cor=''):
    """Alinhamento centralizado."""
    vezes = int(vezes)
    if cor == '':
        fim_da_cor = ''
    else:
        fim_da_cor = '\033[m'

    print(f'-' * vezes)
    print(f'{cor}{mensagem:^{vezes}}{fim_da_cor}')
    print(f'-' * vezes)


def arquivo_existe(user):
    try:
        a = open(user, 'rt')
        a.close()
    except FileNotFoundError:
        return False
    else:
        return True


def criar_arquivo(user):
    try:
        a = open(user, 'wt+')
        a.close()
    except:
        print('\033[31mErro! A criação do arquivo falhou.\033[m')
    else:
        print(f'\033[32mArquivo {user} criado com sucesso!\033[m')
        print('-' * 40, flush=True)


def ler_arquivo(arquivo_de_texto):
    from time import sleep
    n = 0
    with open(arquivo_de_texto) as f:
        for line in f:
            n += 1
            if n % 2 != 0:
                sleep(0.1)
                print(f'Nome: {line.strip()}', flush=True)

            else:
                sleep(0.1)
                print(f'Idade: {line.strip()}', flush=True)
                print('-' * 40, flush=True)
            sleep(0.15)


def ler_arquivo_v2(arquivo_de_texto, spacing=40):
    from time import sleep
    n = 0
    with open(arquivo_de_texto) as f:
        for line in f:
            n += 1
            if n % 2 != 0:
                sleep(0.1)
                print(f'{line.strip():<{spacing - 8}}', end='', flush=True)

            else:
                print(f'{line.strip()} anos', flush=True)
            sleep(0.15)
