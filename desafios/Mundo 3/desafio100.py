from random import randint
from time import sleep
numbers = list()
def sorteia():
    print('Sorteando 5 números de 1 a 100...')
    for e in range(0,5):
        s = randint(1,100)
        numbers.append(s)
        print(f'{s}', end=' ', flush=True)
        sleep(0.3)
    print()


def somaPar():
    sumeven = 0
    for p in numbers:
        if p % 2 == 0:
            sumeven += p
    print('-' * 18)
    print(f'A soma dos números pares é:', f'\n{sumeven}')
    sleep(1)
    print('~' * 36)
    numbers.clear()


print('~' * 36)
sorteia()
somaPar()
sleep(1)