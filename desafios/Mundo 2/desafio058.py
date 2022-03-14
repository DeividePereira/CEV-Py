import random
r = random.randint(1, 10)
tries = 0
n = 0
print('Adivinhe no número que estou pensando!')
while n != r:
    n = int(input('Escolha um número inteiro \033[34mentre 0 e 10\033[m: '))
    tries += 1
    if n > 10:
        print('Você deve digitar um número menor, entre 0 e 10!')
    if n < 0:
        print('Você deve digitar um número maior, entre 0 e 10!')

    if r == n:
        print('\033[30;42mVocê ganhou! Parabéns!\033[m')

    else:
        print('\033[33mVocê não ganhou! Tente novamente.\033[m')

print(f'Foram necessárias \033[31m{tries} tentativas\033[m para acertar!')
