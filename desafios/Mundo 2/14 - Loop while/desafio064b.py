""" Obs.: Feito com flag != 0"""

print('==-== \033[36mSomatório de números inteiros\033[m ==-==')
print('\033[40m[Digite 999 para parar]\033[m')
cont = soma = n = 0

while n != 999:
    n = int(input('Digite um número inteiro: '))
    if n != 999:
        soma += n
        cont += 1
print(f'\033[31mForam {cont} números;')
print(f'\033[31mE a soma de todos os números é:\033[m \033[41m{soma}\033[m')
