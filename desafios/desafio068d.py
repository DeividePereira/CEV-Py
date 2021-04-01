"""Versão infinita; e n como str."""
import random
consec = 0
print('=-='*10, '\n', '\033[36mVamos jogar \033[35mpar \033[36mou \033[37mímpar\033[36m!\033[m')
print('=-=' * 10)

while True:
    c = random.randint(1, 1000000000)  # 1 bilhão
    j = str(input('\033[35mPar\033[m ou \033[37mímpar\033[m? ')).strip().upper()[0]

    if j.isnumeric():  #Validando se está inválido.
        print('Resposta inválida! Tente novamente!')

    elif j != 'P' and j != 'I' and j != "Í":
        print('Resposta inválida! Tente novamente!')

    else:  #Caso não esteja incorreto, prossiga.
        n = str(input('Digite seu número inteiro: '))

        if not str(n).isnumeric():  #Validando se está inválido.
            print('Resposta inválida! Tente novamente!')

        else:  #Caso não esteja incorreto, prossiga.
            if (int(n) + c) % 2 == 0:  # Caso dê Par!
                print(f'{int(n)} + {c} = {int(n) + c} → \033[35mDeu par!\033[m')

                if j == 'P':
                    print('\033[32mVocê venceu!\033[m')

                    consec += 1
                    if consec == 2:
                        print('\033[46mVocê está com sorte!\033[m')
                    if consec == 3:
                        print('\033[46mVocê está com MUITA sorte!\033[m')
                    if consec == 4:
                        print('\033[46mVocê está numa maré de sorte!\033[m')
                    if consec >= 5:
                        print('\033[46mVocê DEVE jogar na loteria!\033[m')

                else:  #O jogador escolheu ímpar.
                    print('\033[31mVocê perdeu!\033[m')
                    print(f'Você teve \033[33m{consec} vitórias consecutivas\033[m.')

                    nov = str(input('Continuar/Desistir: ')).strip().upper()[0]

#                    if nov != 'C' and 'D':
                    if nov not in 'CcDd':
                        print('Resposta inválida! Tente novamente!')
                        while nov != 'C' and 'D':
                            print('Resposta inválida! Tente novamente!')
                            nov = str(input('Continuar/Desistir: ')).strip().upper()[0]
                    elif nov == 'C':
                        consec = 0
                    elif nov == 'D':
                        break

            else:  # Caso dê ímpar
                print(f'{int(n)} + {c} = {int(n) + c} → \033[37mDeu ímpar!\033[m')
                if j == 'I' or j == 'Í':
                    print('\033[32mVocê venceu!\033[m')

                    consec += 1
                    if consec == 2:
                        print('\033[46mVocê está com sorte!\033[m')
                    if consec == 3:
                        print('\033[46mVocê está com MUITA sorte!\033[m')
                    if consec == 4:
                        print('\033[46mVocê está numa maré de sorte!\033[m')
                    if consec >= 5:
                        print('\033[46mVocê DEVE jogar na loteria!\033[m')

                else:
                    print('\033[31mVocê perdeu!\033[m')
                    print(f'Você teve \033[33m{consec} vitórias consecutivas\033[m.')
                    nov = str(input('Continuar/Desistir: ')).strip().upper()[0]

                    #                    if nov != 'C' and 'D':
                    if nov not in 'CcDd':
                        print('Resposta inválida! Tente novamente!')
                        while nov != 'C' and 'D':
                            print('Resposta inválida! Tente novamente!')
                            nov = str(input('Continuar/Desistir: ')).strip().upper()[0]
                    elif nov == 'C':
                        consec = 0
                    elif nov == 'D':
                        break

print('\033[34mEsperamos que você tenha se divertido! Tenha um bom dia!\033[m')
