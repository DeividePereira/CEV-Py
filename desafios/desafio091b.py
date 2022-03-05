#desafio091 mas com o usuário selecionando o número de jogadores, o nome dos jogadores e quantos lados tem o dado.
from random import randint
from time import sleep
dici = dict()

rolagens = int(input('Digite o número de jogadores: '))
while rolagens <= 0:
    print('Erro! Tente novamente.')
    rolagens = int(input('Digite o número de jogadores: '))

num_lado = int(input('Digite o número de lados do dado: '))
while num_lado <= 1:
    print('Erro! Tente novamente.')
    num_lado = int(input('Digite o número de lados do dado: '))

jogador = 'a'
for n in range(1, rolagens + 1):
    jogador = str(input(f'Digite o nome do jogador nº{n}: '))
    while len(jogador) == 0 or jogador.isnumeric or jogador.isspace:
        print('Erro! Tente novamente.')
        jogador = str(input(f'Digite o nome do jogador nº{n}: '))
    dici[f'{jogador}'] = randint(1,num_lado)

print(f'Nota: Dado de {num_lado} lados.\n----- Ranking -----')
ranking = sorted(dici.items(), key=lambda x: x[1], reverse=True) #tupla
for i in ranking:
    print(f'O {i[0]} tirou {i[1]}.')
    sleep (1)
