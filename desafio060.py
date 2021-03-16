""" fatorial com repetição while   """

print('==-== \033[36mCálculo de Fatorial\033[m ==-==')
num = int(input('Digite um número inteiro: '))
c = num
f = 1
print(f'\033[36m{c}!\033[m = ', end='')
while c > 0:
    print(f'{c}', end='')
    print(f' x ' if c > 1 else ' = ', end='')
    f *= c
    c -= 1
print(f'\033[36m{f}\033[m')
