#1-4jogadores: cada um joga um dado.
#2-Guarde os resultados em dicionários.
#3-Organize os dados em ordem decrescente.
#4-Print os resultados dos dados e o ranking.
from random import randint
all = list()
dices = dict()
all.append(dices)
for n in range(1, 5):
    dices[f'{n}'] = randint(1,7)
    all.append(dices.copy())
    print(f'O jogador {n} tirou {dices.values()[f"{n}"]}.')
    #{dices}->está mostrando as keys
    n += 1

print(all)
print(dices)