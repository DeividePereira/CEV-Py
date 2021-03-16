# n % a == 0 and n % n == 0
# a != n
b = 2  # Por quantos números n é divisível. Não conta-se a divisão por 1 nem por n, então começa do 2.
c = 1  # Como o range começa no 2, então os números seriam -1. Ex.: 16/4 == 3
n = int(input('Digite um número inteiro: '))

for a in range(2, n, 1):
    c += 1
    if a != n and n % a == 0:
        print(f'É divisível por \033[34m{c}\033[m. Portanto, {n} \033[31mnão\033[m é primo.')
        b += 1

if b == 2 and n != 1:
    print(f'{n} é primo, pois só é divisível por \033[31m1\033[m e ele mesmo.')

if n == 1:
    print(f'{n} \033[31mnão\033[m é primo, pois só atende uma das duas condições para ser considerado primo.')

elif n != 1:
    print(f'O número {n} pode ser divisível por \033[36m{b}\033[m números.')
