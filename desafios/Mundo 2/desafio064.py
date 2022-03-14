""" Esse exercicio não foi feito com '999' de modo que não precisasse remover o flag da soma"""

print('==-== \033[36mSomatório de números inteiros\033[m ==-==')
print('\033[40m[Digite 0 para parar]\033[m')
cont = soma = 0
n = 1
while n != 0:
    n = int(input('Digite um número inteiro: '))
    soma += n
    if n != 0:
        cont += 1

print(f'\033[31mForam {cont} números;')
print(f'\033[31mE a soma de todos os números é:\033[m \033[41m{soma}\033[m')
