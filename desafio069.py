from time import sleep
print(f'==-==-==-==-==-==-==-==-==-==\n\033[34m{"Cadastro de Pessoas":^29}\033[m\n==-==-==-==-==-==-==-==-==-==')
maior = menor = i = p_maiores = men = mu_menores = 0
cont = 1

while True:
    print(f'\033[36mCadastro de Número {cont}\033[m')
    sexo = str(input('Sexo \033[40m[M/F]\033[m: ')).strip().upper()

    while sexo != 'M' and sexo != 'F' or sexo.isspace():
        print('\033[31mResposta inválida! Tente novamente!\033[m')
        sexo = str(input('Sexo \033[40m[M/F]\033[m: ')).strip().upper()
        sleep(0.1)

    else:
        i = str(input('Idade: ')).strip()

        while i.isalpha() or i.isspace() or i == '':
            print('\033[31mResposta inválida! Tente novamente!\033[m')
            i = str(input('Idade: '))
            sleep(0.1)

        else:
            if int(i) > 18:
                p_maiores += 1

            if sexo == 'M':
                men += 1

            if sexo == 'F' and int(i) < 20:
                mu_menores += 1

            cont += 1
            pro = str(input('Deseja prosseguir?\033[40m[S/N]\033[m ')).upper()[0]

            while pro != 'S' and pro != "N" or pro.isspace() or pro == '':
                print('\033[31mResposta inválida! Tente novamente!\033[m')
                pro = str(input('Deseja prosseguir?\033[40m[S/N]\033[m ')).upper()[0]

                if pro == 'N':
                    break
            if pro == 'N':
                break
print('\033[37mFinalizando...\033[m')
sleep(1)
