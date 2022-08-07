#Usando desempacotamento(* num). Substituí "contador"
# por len(num); E "maior" por max(lista).
from random import randint
from time import sleep
lista = list()
def ranking(* num):
    print('-' * 50)
    print(f' Sorteando {len(num)} números:')
    for valor in num:
        lista.append(valor)
        print(f'{valor} ', end='', flush=True)
        sleep(0.2)
    sleep(1)
    print()

    if len(lista) != 0: 
        print('-' * 25, f'\n   O maior é: {max(lista)}', flush=True)
    else:
        print('Nenhum número!')
    sleep(1)
    lista.clear()
    
ranking(randint(1,100),randint(1,100),randint(1,100))
ranking(randint(1,100),randint(1,100),randint(1,100),randint(1,100),randint(1,100),randint(1,100),randint(1,100),randint(1,100))
ranking(randint(1,100))
ranking()
print('-' * 50, '\nEncerrando...')
sleep(0.2)
