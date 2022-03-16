from random import randint
from time import sleep
lista = list()
def contador(a, b, r):
    print(f' P.A. de {a} até {b}, razão {r}:')
    if r > 0:   # r positivo
        if a <= b:      #1,10,1 -> 1,2,...,10
            while a <= b:
                print(f'{a}', end=' ', flush=True)
                a += r
                sleep(0.2)
        elif a >= b:    #10,0,1 -> 10,9,...,0
            while a >= b:
                print(f'{a}', end=' ', flush=True)
                a -= r
                sleep(0.2)
        print()
    elif r < 0: # r negativo
        if a >= b:      #15,5,-1 -> 15,14,...,5
            while a >= b:
                print(f'{a}', end=' ', flush=True)
                a += r
                sleep(0.2)
        elif a <= b:    #10,20,-1 -> 10,9,...,impossível.
            print(f'   \033[31mErro!\033[m É impossível {a} virar {b} com razão {r}.')
            print(f'   Se a razão for positiva, fica: ')
            while a <= b:   #10-(-1) = 10+1=11
                print(f'{a}', end=' ', flush=True)
                a -= r      
                sleep(0.2)
        print()
    else: #r == 0
        print(f'   Erro! É impossível {a} virar {b} com razão {r}.')
        user_r = int(input(f'  Nova razão: '))
        print('-' * 10)
        contador(user_a, user_b, user_r)
        
    print('-' * 50) #está acumulando '-' se a razão for 0 mais de uma vez.
print('-' * 50)
contador(1, 10, 1)      #a<b, p>0
contador(10, 0, 2)     #a>b, p>0
contador(15, 5, -1)    #a>b, p<0
contador(10, 20, -1)   #a<b, p<0

print('P.A. aleatória!')
contador(randint(-100,100), randint(-100,100), randint(-10,10))

print('Sua vez de criar uma PA!')
user_a = int(input('  Primeiro termo: '))
user_b = int(input('  Último termo: '))
user_r = int(input('  Razão: '))
print('-' * 10)
contador(user_a, user_b, user_r)
