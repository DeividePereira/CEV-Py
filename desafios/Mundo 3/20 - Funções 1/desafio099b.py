#desafio099 só que melhor
from random import randint
from time import sleep
lista = list()
def ranking(n):
    print('-' * 50)
    print(f' Sorteando {n} números:')
    for n in range(0, n):
        m = randint(1,100)
        lista.append(m)

    for z in lista:
        print(f'{z}', end=' ', flush=True)
        sleep(0.1)
    print()

    lista.sort()
    lista.reverse()
    print('-' * 25, '\n   Ranking:')
    for z2 in lista:
        print(f'{z2}', end=' ', flush=True)
        sleep(0.15)
    sleep(0.75)
    print()
    lista.clear()
    

ranking(randint(1,30))
ranking(randint(1,30))
ranking(randint(1,30))
print('-' * 50, '\nEncerrando...')
sleep(1)
