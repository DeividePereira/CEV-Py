print('--------------------------------'
      '\n\033[40m Sistema de Registro de Pessoas \033[m'
      '\n--------------------------------')
while True:
    check_name = False
    n = 0
    print('\033[40m              Menu              \033[m'
          '\n\033[40m[1]\033[m Cadastrar uma nova pessoa'
          '\n\033[40m[2]\033[m Listar todo o cadastro'
          '\n\033[40m[3]\033[m Encerrar programa')

    try:
        user = str(input('Opção: '))

        if user != '1' and user != '2' and user != '3':
            print('\033[31mErro! Tente novamente.\033[m')

        if user == '1':
            print('--------------------------------'
                  '\n\033[40m      Cadastrar Uma Pessoa      \033[m'
                  '\n--------------------------------')
            while True:
                if not check_name:
                    try:
                        name = str(input('Nome: ')).strip()

                        if name.isnumeric():
                            print('\033[31mErro! Foram digitados apenas caracteres numéricos.\033[m')
                            while name.isnumeric():
                                name = str(input('Nome: '))
                    except KeyboardInterrupt:
                        print('\033[33mInterrompido manualmente.\033[m')
                        break
                    else:
                        check_name = True

                try:
                    age = int(input('Idade: '))

                except ValueError:  # 1.0 \ #! \   \ æ \ abc
                    print('\033[31mErro! Foi digitado algum caractere não-numérico.\033[m')
                    continue
                except KeyboardInterrupt:
                    print('\033[33mInterrompido manualmente.\033[m')
                    break

                else:
                    more_lines = ['', name, str(age)]
                    with open('contatos.txt', 'a') as f:
                        f.write('\n'.join(more_lines))

                    print(f'O/A {name} de {age} anos foi adicionado(a) com \033[32msucesso\033[m.')
                    break

        if user == '2':
            print('--------------------------------'
                  '\n\033[40m   Lista de todos cadastrados   \033[m'
                  '\n--------------------------------')

            with open('contatos.txt') as f:
                for line in f:
                    n += 1
                    if n % 2 != 0:
                        print(f'Nome: {line.strip()}')
                    else:
                        print(f'Idade: {line.strip()}')
                        print('--------------------------------')

        if user == '3':
            print('\nEncerrando...')
            break

    except KeyboardInterrupt:
        print('\033[33m\nInterrompido manualmente.\033[m'
              '\n\nEncerrando...')
        break
