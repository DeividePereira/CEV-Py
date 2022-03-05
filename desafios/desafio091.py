#1-4jogadores: cada um joga um dado. 2-Guarde os resultados em dicionários.
#3-Organize os dados em ordem decrescente. #4-Print os resultados dos dados e o ranking.
from random import randint
from time import sleep
dici = dict()
for n in range(1,5): #4 jogadores = 4 rolagens de dado
    dici[f'Jogador {n}'] = randint(1,6) #o dado tem 6 lados

print('Nota: Dado de 6 lados.\n----- Ranking -----')
ranking = sorted(dici.items(), key=lambda x: x[1], reverse=True) #tupla
for i in ranking:
    print(f'O {i[0]} tirou {i[1]}.')
    sleep(1)
