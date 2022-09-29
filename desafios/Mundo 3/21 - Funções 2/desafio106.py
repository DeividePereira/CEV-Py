from time import sleep


def ajuda(user):
    if user == 'ajuda':
        print("""\033[41mMini-sistema interativo de ajuda.      \033[m
\033[41m help(user)                            \033[m
\033[41m   user: objeto python a ser explicado.\033[m""")

    elif user != 'fim':
        help(user)
    else:
        print('\033[47mEncerrando...\033[m', flush=True)
        sleep(1)
    while user != 'fim':
        ajuda(str(input('\033[40mDigite o nome de uma função ou biblioteca:   \033[m '
                        '\n\033[40m(Ou digite \"fim\" para encerrar)\033[m ')).strip())
        break


print('\033[44m-\033[m' * 36)
print('\033[44m Sistema de Ajuda de Funções Python \033[m')
print('\033[44m-\033[m' * 36)

ajuda(str(input('\033[40mDigite o nome de uma função ou biblioteca:   \033[m '
                '\n\033[40m(Ou digite \"fim\" para encerrar)\033[m ')).strip())
