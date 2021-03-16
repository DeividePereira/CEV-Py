"""Versão finita(quando perder, acaba); n como int -> erro: finaliza quando n não é número inteiro"""
import random
consec = 0
print('=-='*10, '\n', '\033[36mVamos jogar \033[35mpar \033[36mou \033[37mímpar\033[36m!\033[m')
print('=-=' * 10)

while True:
    c = random.randint(1, 1000000000)  # 1 bilhão
    j = str(input('\033[35mPar\033[m ou \033[37mimpar\033[m? ')).strip().upper()[0]

    if j.isnumeric():
        print('Resposta inválida! Tente novamente!')

#    elif j != 'P' and j != 'I' and j != "Í":
#        print('Resposta inválida! Tente novamente!')
    elif j not in 'PIÍ':
        print('Resposta inválida! Tente novamente!')
    else:
        n = int(input('Digite seu número inteiro: '))

        if not str(n).isnumeric():  # Mesmo estando certo, o programa finaliza.
            print('Resposta inválida! Tente novamente!')

        if (n + c) % 2 == 0:
            print(f'{n} + {c} = {n + c} → \033[35mDeu par!\033[m')

            if j == 'P':
                print('\033[32mVocê venceu!\033[m')
                consec += 1
            else:
                print('\033[31mVocê perdeu!\033[m')
                break

        else:
            print(f'{n} + {c} = {n + c} → \033[37mDeu ímpar!\033[m')
            if j == 'I' or j == 'Í':
                print('\033[32mVocê venceu!\033[m')
                consec += 1
            else:
                print('\033[31mVocê perdeu!\033[m')
                break

    if consec == 2:
        print('\033[46mVocê está com sorte!\033[m')
    if consec == 3:
        print('\033[46mVocê está com MUITA sorte!\033[m')
    if consec == 4:
        print('\033[46mVocê está numa maré de sorte!\033[m')

print(f'Você teve \033[33m{consec} vitórias consecutivas\033[m.')
