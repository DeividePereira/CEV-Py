from utilidadescev import contatos
from utilidadescev.dados import leia_int

spacing = 50
arquivo = 'contatos.txt'
menu1 = 'Menu'

contatos.titulo_centralizado('Sistema de Registro de Pessoas', spacing, '\033[40m')

if not contatos.arquivo_existe(arquivo):
    contatos.criar_arquivo(arquivo)

while True:
    check_name = 0
    n = 0

    print(f'\033[40m{menu1:^{spacing}}\033[m'
          '\n\033[36;40m[1]\033[m Cadastrar uma nova pessoa'
          '\n\033[36;40m[2]\033[m Listar todo o cadastro'
          '\n\033[36;40m[3]\033[m Encerrar sistema')

    try:
        user = str(input('\033[36mSua Opção: \033[m'))

        if user == '1':
            contatos.titulo_centralizado('Cadastrar Uma Pessoa', spacing, '\033[40m')

            while not check_name == 2:
                try:
                    name = str(input('Nome: ')).strip()

                    while name.isnumeric():
                        print('\033[31mErro! Foram digitados apenas caracteres numéricos.\033[m')
                        name = str(input('Nome: ')).strip()
                    else:
                        check_name += 1

                    while name == '':
                        print('\033[31mErro! Nada foi inserido.\033[m')
                        name = str(input('Nome: ')).strip()
                    else:
                        check_name += 1

                except KeyboardInterrupt:
                    print('\033[33m\nInterrompido manualmente.\033[m')
                    break

                else:
                    try:
                        age = leia_int()
                    except KeyboardInterrupt:
                        print('\033[33m\nInterrompido manualmente.\033[m')
                        break

                    else:
                        mais_contatos = ['', name, str(age)]
                        with open('contatos.txt', 'a') as f:
                            f.write('\n'.join(mais_contatos))

                        print(f'\033[32mSucesso!\033[m {name} foi registrado(a).')
                        print('-' * spacing)
                        break

        elif user == '2':
            contatos.titulo_centralizado('Lista de todos cadastrados', spacing, '\033[40m')

            #contatos.ler_arquivo(arquivo)
            contatos.ler_arquivo_v2(arquivo, spacing)
            print('-' * spacing)

        elif user == '3':
            print('\nEncerrando...')
            break

        else:  #if user != '1' and user != '2' and user != '3':
            print('\033[31mErro! Tente novamente.\033[m')

    except KeyboardInterrupt:
        print('\033[33m\nInterrompido manualmente.\033[m'
              '\n\nEncerrando...')
        break
